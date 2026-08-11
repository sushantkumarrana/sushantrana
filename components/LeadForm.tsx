"use client";

import { useId, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import {
  ENQUIRY_TYPES,
  OTHER_SERVICE,
  SERVICE_GROUPS,
  serviceFromPath,
} from "@/lib/services";
import { COUNTRIES, COUNTRY_BY_ISO, DEFAULT_COUNTRY, flagOf } from "@/lib/countries";
import { validateEmail, validatePhone } from "@/lib/validation";

type FieldName = "name" | "email" | "phone" | "service";
type Messages = Partial<Record<FieldName, string>>;

/**
 * The one lead form on the site. Rendered inside the consult popup and in the
 * blog sidebar, so a change to the fields lands everywhere at once.
 *
 * Validation runs three times, deliberately:
 *   1. on blur — so a mistyped address is flagged next to the field, while the
 *      visitor is still looking at it;
 *   2. on submit — nothing leaves the browser until every field passes;
 *   3. in /api/lead — the only one that counts, since the first two can be
 *      skipped by posting directly. The route also does a DNS lookup the
 *      browser can't, and its per-field errors are shown here the same way.
 *
 * `compact` trims the paddings for the narrow sidebar column; everything else
 * is identical between the two.
 */
export default function LeadForm({
  compact = false,
  fields = "full",
  submitLabel = "Request my slot",
  onSuccess,
}: {
  compact?: boolean;
  /** "short" drops business + message so the sticky sidebar panel still fits a
   *  laptop viewport. Both variants post to the same endpoint; the dropped
   *  fields were already optional. */
  fields?: "full" | "short";
  /** Must not start with "Book" — ConsultPopup's delegated listener treats any
   *  such button as a CTA and would reopen the popup instead of submitting. */
  submitLabel?: string;
  onSuccess?: () => void;
}) {
  const router = useRouter();
  const pathname = usePathname() || "/";
  const uid = useId();

  // Preselect the service when the form is opened from a service page, so a
  // visitor on /services/google-ads doesn't hunt through a 33-item dropdown.
  const [service, setService] = useState(() => serviceFromPath(pathname));
  const [enquiryType, setEnquiryType] = useState<string>(ENQUIRY_TYPES[0].value);
  const [country, setCountry] = useState(DEFAULT_COUNTRY);
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  const [errors, setErrors] = useState<Messages>({});
  const [hints, setHints] = useState<Messages>({});
  const [busy, setBusy] = useState(false);
  const [formError, setFormError] = useState<string | null>(null);

  const full = fields === "full";
  const dial = COUNTRY_BY_ISO.get(country)?.dial ?? "91";

  const setError = (f: FieldName, msg?: string) =>
    setErrors((e) => ({ ...e, [f]: msg }));
  const setHint = (f: FieldName, msg?: string) =>
    setHints((h) => ({ ...h, [f]: msg }));

  const checkEmail = (value: string) => {
    if (!value.trim()) return true; // "required" is the browser's job, not ours
    const r = validateEmail(value);
    setError("email", r.ok ? undefined : r.error);
    setHint("email", r.hint);
    return r.ok;
  };

  const checkPhone = async (value: string, iso: string) => {
    if (!value.trim()) return true;
    const r = await validatePhone(iso, value);
    setError("phone", r.ok ? undefined : r.error);
    return r.ok;
  };

  const base = `w-full rounded-xl border bg-white/70 text-ink outline-none transition ${
    compact ? "px-3.5 py-2.5 text-sm" : "px-4 py-3"
  }`;
  const field = (f?: FieldName) =>
    `${base} ${
      f && errors[f]
        ? "border-red-500 focus:border-red-500"
        : "border-[var(--color-line)] focus:border-orange"
    }`;

  /**
   * Error/hint line under a field. A plain function, not a component defined
   * in render — that would be a new component type on every keystroke, so
   * React would unmount and remount the message and the input would lose
   * focus mid-typing.
   */
  const note = (f: FieldName) =>
    errors[f] ? (
      <p id={`${uid}-${f}-msg`} role="alert" className="mt-1 text-xs font-medium text-red-600">
        {errors[f]}
      </p>
    ) : hints[f] ? (
      <p id={`${uid}-${f}-msg`} className="mt-1 text-xs font-medium text-orange">
        {hints[f]}
      </p>
    ) : null;

  const aria = (f: FieldName) => ({
    "aria-invalid": errors[f] ? (true as const) : undefined,
    "aria-describedby": errors[f] || hints[f] ? `${uid}-${f}-msg` : undefined,
  });

  return (
    <form
      noValidate
      className={`grid ${compact ? "gap-2.5" : "gap-3"}`}
      onSubmit={async (e) => {
        e.preventDefault();
        if (busy) return;
        const formEl = e.currentTarget;
        setBusy(true);
        setFormError(null);

        const fd = new FormData(formEl);
        const name = String(fd.get("name") || "").trim();

        // noValidate above means we own the required checks too — the native
        // bubbles can't sit next to our own messages consistently.
        const next: Messages = {};
        if (!name) next.name = "Please tell me your name.";
        if (!String(fd.get("email") || "").trim()) next.email = "Email is required.";
        if (!String(fd.get("phone") || "").trim()) next.phone = "Phone number is required.";
        if (!fd.get("service")) next.service = "Please choose a service.";
        if (Object.keys(next).length) {
          setErrors((prev) => ({ ...prev, ...next }));
          setBusy(false);
          return;
        }

        const [emailOk, phoneOk] = await Promise.all([
          checkEmail(String(fd.get("email"))),
          checkPhone(String(fd.get("phone")), country),
        ]);
        if (!emailOk || !phoneOk) {
          setBusy(false);
          return;
        }

        const payload = {
          name,
          email: fd.get("email"),
          phone: fd.get("phone"),
          phoneCountry: country,
          business: fd.get("business"),
          service: fd.get("service"),
          enquiryType: fd.get("enquiryType"),
          message: fd.get("message"),
          company_website: fd.get("company_website"), // honeypot
          sourcePath: window.location.pathname,
        };

        try {
          const res = await fetch("/api/lead", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
          });
          const data = await res.json().catch(() => ({}));

          if (!res.ok || !data.ok) {
            // Never send them to /thank-you on failure — that would tell them
            // it worked when the lead was lost.
            const msg = data.error || "Could not send. Please try again.";
            // The route names the field it rejected (e.g. a domain with no mail
            // server), so the message lands on the input rather than in a
            // generic banner the visitor has to map back themselves.
            if (data.field === "email" || data.field === "phone") {
              setError(data.field, msg);
            } else {
              setFormError(msg);
            }
            setBusy(false);
            return;
          }

          onSuccess?.();
          router.push("/thank-you");
        } catch {
          setFormError("Network problem. Please check your connection and retry.");
          setBusy(false);
        }
      }}
    >
      <div>
        <input
          name="name"
          placeholder="Your name"
          autoComplete="name"
          className={field("name")}
          {...aria("name")}
          onChange={() => errors.name && setError("name", undefined)}
        />
        {note("name")}
      </div>

      <div>
        <input
          name="email"
          type="email"
          inputMode="email"
          autoComplete="email"
          placeholder="Email"
          value={email}
          className={field("email")}
          {...aria("email")}
          onChange={(e) => {
            setEmail(e.target.value);
            // Clear while typing; re-check on blur. Correcting an error as
            // someone fixes it is helpful; nagging mid-word is not.
            if (errors.email) setError("email", undefined);
          }}
          onBlur={(e) => checkEmail(e.target.value)}
        />
        {note("email")}
      </div>

      <div>
        <div
          className={`flex overflow-hidden rounded-xl border bg-white/70 transition ${
            errors.phone
              ? "border-red-500 focus-within:border-red-500"
              : "border-[var(--color-line)] focus-within:border-orange"
          }`}
        >
          {/* The visible flag + dial code sit on top of a transparent native
              <select>, so the control is a real, keyboard-accessible select
              with searchable options while still matching the form's styling. */}
          <div className="relative shrink-0">
            <span
              aria-hidden
              className={`pointer-events-none flex h-full items-center gap-1 border-r border-[var(--color-line)] pl-3 pr-2 ${
                compact ? "text-sm" : ""
              }`}
            >
              <span className="text-base leading-none">{flagOf(country)}</span>
              <span className="font-medium text-ink">+{dial}</span>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" className="text-muted">
                <path d="m6 9 6 6 6-6" />
              </svg>
            </span>
            <select
              aria-label="Country calling code"
              value={country}
              onChange={(e) => {
                setCountry(e.target.value);
                // The same digits can be valid in one country and not another,
                // so any pending error is stale the moment this changes.
                setError("phone", undefined);
                if (phone.trim()) void checkPhone(phone, e.target.value);
              }}
              className="absolute inset-0 h-full w-full cursor-pointer opacity-0"
            >
              {COUNTRIES.map((c) => (
                <option key={c.iso} value={c.iso}>
                  {c.name} (+{c.dial})
                </option>
              ))}
            </select>
          </div>

          <input
            name="phone"
            type="tel"
            inputMode="tel"
            autoComplete="tel-national"
            placeholder="Phone number"
            value={phone}
            className={`min-w-0 flex-1 bg-transparent text-ink outline-none ${
              compact ? "px-3 py-2.5 text-sm" : "px-4 py-3"
            }`}
            {...aria("phone")}
            onChange={(e) => {
              setPhone(e.target.value);
              if (errors.phone) setError("phone", undefined);
            }}
            onBlur={(e) => void checkPhone(e.target.value, country)}
          />
        </div>
        {note("phone")}
      </div>

      {full && (
        <input
          name="business"
          placeholder="Business / website"
          autoComplete="organization"
          className={field()}
        />
      )}

      {/* What do you need? — the intent behind the enquiry, kept separate from
          the service so a "Google Ads" lead is legible as advice-seeking or
          ready-to-buy without reading the message. */}
      <fieldset className="mt-1">
        <legend className="mb-1.5 text-xs font-semibold uppercase tracking-wide text-muted">
          What do you need?
        </legend>
        <div className="grid grid-cols-2 gap-2">
          {ENQUIRY_TYPES.map((t) => {
            const on = enquiryType === t.value;
            return (
              <label
                key={t.value}
                title={t.hint}
                className={`cursor-pointer rounded-xl border px-3 py-2 text-center transition ${
                  on
                    ? "border-orange bg-orange text-white shadow-[0_10px_24px_-14px_rgba(var(--orange-rgb),0.8)]"
                    : "border-[var(--color-line)] bg-white/70 text-body hover:border-orange hover:text-orange"
                }`}
              >
                <input
                  type="radio"
                  name="enquiryType"
                  value={t.value}
                  checked={on}
                  onChange={() => setEnquiryType(t.value)}
                  className="sr-only"
                />
                <span className="block text-xs font-semibold leading-tight">{t.label}</span>
              </label>
            );
          })}
        </div>
      </fieldset>

      <div>
        <label
          htmlFor={`${uid}-service`}
          className="mb-1.5 block text-xs font-semibold uppercase tracking-wide text-muted"
        >
          Which service?
        </label>
        <select
          id={`${uid}-service`}
          name="service"
          value={service}
          onChange={(e) => {
            setService(e.target.value);
            setError("service", undefined);
          }}
          {...aria("service")}
          /* appearance-none + our own chevron: the native arrow renders grey and
             boxy on Windows and breaks the glass look. */
          className={`appearance-none bg-[length:12px] bg-[right_1rem_center] bg-no-repeat pr-10 ${field(
            "service"
          )} ${service ? "" : "text-muted"}`}
          style={{
            backgroundImage:
              "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235a5a5a' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='m6 9 6 6 6-6'/></svg>\")",
          }}
        >
          <option value="" disabled>
            Select a service…
          </option>
          {SERVICE_GROUPS.map((g) => (
            <optgroup key={g.heading} label={g.heading}>
              {g.items.map((s) => (
                <option key={s} value={s}>
                  {s}
                </option>
              ))}
            </optgroup>
          ))}
          <option value={OTHER_SERVICE}>{OTHER_SERVICE}</option>
        </select>
        {note("service")}
      </div>

      {full && (
        <textarea
          name="message"
          rows={compact ? 2 : 3}
          placeholder="What do you want to grow?"
          className={field()}
        />
      )}

      {/* honeypot — hidden from people, irresistible to bots */}
      <input
        name="company_website"
        tabIndex={-1}
        autoComplete="off"
        aria-hidden="true"
        className="absolute left-[-9999px] h-0 w-0 opacity-0"
      />

      {formError && (
        <p role="alert" className="rounded-xl bg-red-50 px-4 py-2.5 text-sm font-medium text-red-700">
          {formError}
        </p>
      )}

      <button
        type="submit"
        disabled={busy}
        className={`btn btn-primary mt-1 w-full disabled:cursor-not-allowed disabled:opacity-70 ${
          compact ? "!min-h-[46px] text-sm" : ""
        }`}
      >
        {busy ? "Checking…" : submitLabel}
      </button>
    </form>
  );
}
