/**
 * sushantrana.com — Google Ads script (paste into Google Ads → Tools → Bulk actions → Scripts).
 *
 * Runs daily. It
 *  1. uploads the leads Sushant marked "Qualified lead" / "Won deal" in the panel
 *     as offline click conversions (by gclid), then tells the panel what it sent;
 *  2. sends the panel yesterday's spend per campaign and ad group, which click
 *     (gclid) came from which campaign / ad group / keyword, and the last 7 days'
 *     search terms.
 *
 * Before the first run:
 *  - In Google Ads create two conversion actions, source "Import → CRMs, files or
 *    other sources → Track conversions from clicks", named exactly "Qualified lead"
 *    and "Won deal" (value: use the value from the import).
 *  - Put the same long random key here and in api/config.php (GOOGLE_ADS_SCRIPT_KEY).
 *  - Authorise the script, run "Preview" once, then schedule it Daily.
 */

var PANEL_URL = 'https://sushantrana.com/api/ads-google.php';
var KEY = 'PASTE_GOOGLE_ADS_SCRIPT_KEY_HERE';
var CHUNK = 1500; // rows per push, keeps each request well under the panel's 2 MB limit

function call(action, body) {
  var res = UrlFetchApp.fetch(PANEL_URL + '?a=' + action, {
    method: 'post',
    contentType: 'application/json',
    headers: { 'X-Key': KEY },
    payload: JSON.stringify(body || {}),
    muteHttpExceptions: true
  });
  if (res.getResponseCode() !== 200) {
    throw new Error(action + ': HTTP ' + res.getResponseCode() + ' ' + res.getContentText().slice(0, 200));
  }
  return JSON.parse(res.getContentText());
}

function rows(query, map) {
  var out = [];
  var it = AdsApp.search(query);
  while (it.hasNext()) out.push(map(it.next()));
  return out;
}

function day(offset) {
  var tz = AdsApp.currentAccount().getTimeZone();
  return Utilities.formatDate(new Date(Date.now() - offset * 864e5), tz, 'yyyy-MM-dd');
}

function uploadConversions() {
  var list = call('pull').conversions;
  if (!list.length) return Logger.log('No conversions to upload.');
  var upload = AdsApp.bulkUploads().newCsvUpload(
    ['Google Click ID', 'Conversion Name', 'Conversion Time', 'Conversion Value', 'Conversion Currency'],
    { moneyInMicros: false, timeZone: 'Asia/Kolkata' }
  );
  upload.forOfflineConversions();
  list.forEach(function (c) {
    upload.append({
      'Google Click ID': c.gclid,
      'Conversion Name': c.name,
      'Conversion Time': c.time,
      'Conversion Value': c.value === null ? '' : c.value,
      'Conversion Currency': c.currency || ''
    });
  });
  upload.apply();
  // Row-level results appear in Google Ads → Uploads; the panel marks these as sent.
  call('ack', { sent: list.map(function (c) { return c.id; }), failed: [] });
  Logger.log('Uploaded ' + list.length + ' conversions.');
}

function pushReports() {
  var yesterday = day(1);
  var spend = rows(
    "SELECT segments.date, campaign.name, ad_group.name, metrics.cost_micros, metrics.clicks, metrics.impressions, customer.currency_code " +
      "FROM ad_group WHERE segments.date DURING YESTERDAY AND metrics.impressions > 0",
    function (r) {
      return { day: r.segments.date, platform: 'google', campaign: r.campaign.name, ad_group: r.adGroup.name,
        cost: Number(r.metrics.costMicros) / 1e6, clicks: Number(r.metrics.clicks), impressions: Number(r.metrics.impressions),
        currency: r.customer.currencyCode };
    }
  );
  var clicks = rows(
    "SELECT click_view.gclid, click_view.keyword_info.text, campaign.name, ad_group.name, segments.date " +
      "FROM click_view WHERE segments.date = '" + yesterday + "'",
    function (r) {
      return { click_id: r.clickView.gclid, day: r.segments.date, campaign: r.campaign.name, ad_group: r.adGroup.name,
        keyword: (r.clickView.keywordInfo && r.clickView.keywordInfo.text) || '' };
    }
  );
  var terms = rows(
    "SELECT search_term_view.search_term, campaign.name, ad_group.name, metrics.clicks, metrics.cost_micros, metrics.conversions, segments.date " +
      "FROM search_term_view WHERE segments.date DURING LAST_7_DAYS AND metrics.clicks > 0",
    function (r) {
      return { day: r.segments.date, campaign: r.campaign.name, ad_group: r.adGroup.name, term: r.searchTermView.searchTerm,
        clicks: Number(r.metrics.clicks), cost: Number(r.metrics.costMicros) / 1e6, conversions: Number(r.metrics.conversions) };
    }
  );
  [['spend', spend], ['clicks', clicks], ['terms', terms]].forEach(function (pair) {
    for (var i = 0; i < pair[1].length; i += CHUNK) {
      var body = {};
      body[pair[0]] = pair[1].slice(i, i + CHUNK);
      call('push', body);
    }
  });
  Logger.log('Pushed ' + spend.length + ' spend rows, ' + clicks.length + ' clicks, ' + terms.length + ' search terms.');
}

function main() {
  uploadConversions();
  pushReports();
}
