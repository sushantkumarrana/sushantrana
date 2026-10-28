// Which browser time zones get the consent banner (site.js europeZone).
// Run: node dev/tests/consent_zone_test.js
const fs = require("fs");
const src = fs.readFileSync(__dirname + "/../../assets/js/site.js", "utf8");
const m = src.match(/const europeZone = [\s\S]*?;\n/);
if (!m) {
  console.error("FAIL: europeZone not found in site.js");
  process.exit(1);
}
const europeZone = new Function(m[0] + "return europeZone;")();
const yes = ["Europe/Berlin", "Europe/London", "Europe/Zurich", "Asia/Nicosia", "Asia/Famagusta", "Atlantic/Canary", "Africa/Ceuta",
  "Atlantic/Madeira", "Atlantic/Azores", "Atlantic/Reykjavik", "Arctic/Longyearbyen", "Indian/Reunion", "America/Guadeloupe",
  "America/Martinique", "America/Cayenne", "Indian/Mayotte", "UTC", "Etc/UTC", "Etc/GMT", ""];
const no = ["Asia/Kolkata", "Asia/Dubai", "America/New_York", "America/Toronto", "Australia/Sydney"];
for (const tz of yes) if (!europeZone(tz)) { console.error(`FAIL: ${tz} should get the banner`); process.exit(1); }
for (const tz of no) if (europeZone(tz)) { console.error(`FAIL: ${tz} should not get the banner`); process.exit(1); }
console.log("consent zones ok");
