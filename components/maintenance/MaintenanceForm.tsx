"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Check, Lock } from "lucide-react";
import { COUNTRIES, COUNTRY_BY_ISO, DEFAULT_COUNTRY, flagOf } from "@/lib/countries";
import { validateEmail, validatePhone } from "@/lib/validation";
import { MAINTENANCE_LEAD_KEY } from "@/lib/whatsapp";
import { pushLead } from "@/lib/datalayer";
import {
  ACCESS_ANSWERS,
  FORM_ACCESS,
  FORM_PROBLEMS,
  FORM_REASONS,
  PLATFORMS,
} from "@/lib/maintenance";
import MultiSelect from "./MultiSelect";

/**
 * Three-step website maintenance enquiry: the site, access to it, then
 * contact details. Contact comes last on purpose: by then the visitor has
 * already invested in the first two steps and is far less likely to drop off.
 *
 * Posts to the shared /api/lead endpoint (which emails the lead), with every
 * answer the route has no column for folded into `message`. The thank-you page
 * then opens WhatsApp with the same answers typed out.
 */

const STEPS = ["Your website", "Access", "Contact"];
const THANK_YOU = "/thank-you-website-maintenance";

type Errors = Partial<
  Record<"platform" | "problems" | "reason" | "access" | "name" | "email" | "phone" | "form", string>
>;

const CHEVRON = {
  backgroundImage:
    "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235a5a5a' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='m6 9 6 6 6-6'/></svg>\")",
};

export default function MaintenanceForm({
  initialPlan = "",
  compact = false,
}: {
  initialPlan?: string;
  /** Tighter heading when shown inside the popup. */
  compact?: boolean;
}) {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [busy, setBusy] = useState(false);
  const [errors, setErrors] = useState<Errors>({});

  const [website, setWebsite] = useState("");
  const [platform, setPlatform] = useState("");
  const [problems, setProblems] = useState<string[]>([]);
  const [reasons, setReasons] = useState<string[]>([]);
  // No plan picker in the form: the plan is only known when the visitor came
  // in through a plan's "Choose" button, and then it rides along silently.
  const plan = initialPlan;
  const [access, setAccess] = useState<Record<string, string>>({});
  const [country, setCountry] = useState(DEFAULT_COUNTRY);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [honeypot, setHoneypot] = useState("");

  const dial = COUNTRY_BY_ISO.get(country)?.dial ?? "91";
  const clear = (k: keyof Errors) => setErrors((p) => ({ ...p, [k]: undefined, form: undefined }));

  const inputCls = (bad?: string) =>
    `w-full rounded-xl border bg-white px-4 py-2.5 text-ink outline-none transition ${
      bad ? "border-red-500" : "border-[var(--color-line)] focus:border-orange"
    }`;

  const label = (text: string, required = false, hint?: string) => (
    <span className="mb-2 block text-sm font-semibold text-ink">
      {text} {required && <span className="text-orange">*</span>}
      {hint && <span className="ml-1 font-normal text-muted">{hint}</span>}
    </span>
  );

  const err = (k: keyof Errors) =>
    errors[k] ? (
      <p role="alert" className="mt-1.5 text-xs font-medium text-red-600">
        {errors[k]}
      </p>
    ) : null;

  function validate(s: number): boolean {
    const next: Errors = {};
    if (s === 0) {
      if (!platform) next.platform = "Pick the platform your site runs on.";
      if (!problems.length) next.problems = "Pick at least one.";
      if (!reasons.length) next.reason = "Pick at least one reason.";
    }
    if (s === 1) {
      if (FORM_ACCESS.some((a) => !access[a.key])) next.access = "Please answer all three.";
    }
    setErrors(next);
    return Object.keys(next).length === 0;
  }

  async function validateContact(): Promise<boolean> {
    const next: Errors = {};
    if (!name.trim()) next.name = "Please tell me your name.";
    const e = validateEmail(email);
    if (!e.ok) next.email = e.error;
    const p = await validatePhone(country, phone);
    if (!p.ok) next.phone = p.error;
    setErrors(next);
    return Object.keys(next).length === 0;
  }

  function next() {
    if (validate(step)) setStep((s) => s + 1);
  }

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    if (busy) return;
    // Enter in a step 1 or 2 field submits the form; treat it as "Next".
    if (step < 2) return next();

    setBusy(true);
    if (!(await validateContact())) {
      setBusy(false);
      return;
    }

    const accessText = FORM_ACCESS.map(
      (a) => `${a.key[0].toUpperCase()}${a.key.slice(1)} login: ${access[a.key]}`
    ).join(", ");

    const body = [
      website && `Website: ${website}`,
      `Platform: ${platform}`,
      `Problems: ${problems.join(", ")}`,
      `Why maintenance: ${reasons.join(", ")}`,
      plan && `Plan picked on the page: ${plan}`,
      `Access: ${accessText}`,
    ]
      .filter(Boolean)
      .join("\n");

    try {
      const res = await fetch("/api/lead", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          email,
          phone,
          phoneCountry: country,
          business: website,
          service: "Website Maintenance",
          enquiryType: "service",
          message: body,
          company_website: honeypot,
          sourcePath: window.location.pathname,
        }),
      });
      const data = await res.json().catch(() => ({}));

      if (!res.ok || !data.ok) {
        if (data.field === "email" || data.field === "phone") {
          setErrors({ [data.field]: data.error } as Errors);
        } else {
          setErrors({ form: data.error || "Could not send. Please try again." });
        }
        setBusy(false);
        return;
      }

      pushLead(
        "website_maintenance",
        {
          website,
          platform,
          problems,
          reasons,
          plan: plan || "",
          domain_login: access.domain,
          hosting_login: access.hosting,
          backend_login: access.backend,
        },
        { name, email, phone: `+${dial}${phone.replace(/\D/g, "")}` }
      );

      try {
        sessionStorage.setItem(
          MAINTENANCE_LEAD_KEY,
          JSON.stringify({
            name,
            email,
            phone: `+${dial} ${phone}`,
            website,
            platform,
            problems: problems.join(", "),
            reason: reasons.join(", "),
            plan,
            access: accessText,
          })
        );
      } catch {
        // Storage blocked: the lead is already emailed, the thank-you page just
        // falls back to a generic WhatsApp message.
      }
      router.push(THANK_YOU);
    } catch {
      setErrors({ form: "Network problem. Please check your connection and retry." });
      setBusy(false);
    }
  }

  return (
    <div className="card p-5 hover:[transform:none] md:p-6">
      <h2 className={`${compact ? "pr-10 text-lg" : "text-xl"} font-extrabold text-ink`}>
        Get your website looked after
      </h2>
      <p className="mt-1.5 text-sm text-muted">Three quick steps. Free site check, no obligation.</p>

      <ol className="mt-5 flex list-none items-center gap-2">
        {STEPS.map((s, i) => (
          <li key={s} className="flex flex-1 items-center gap-2">
            <span
              className={`grid h-7 w-7 shrink-0 place-items-center rounded-full text-xs font-bold transition ${
                i <= step ? "bg-orange text-white" : "bg-ink/10 text-muted"
              }`}
            >
              {i < step ? <Check aria-hidden className="h-3.5 w-3.5" strokeWidth={3} /> : i + 1}
            </span>
            <span
              className={`hidden text-[11px] font-semibold uppercase leading-tight tracking-wide sm:block ${
                i <= step ? "text-ink" : "text-muted"
              }`}
            >
              {s}
            </span>
            {i < STEPS.length - 1 && (
              <span className={`h-px flex-1 ${i < step ? "bg-orange" : "bg-ink/10"}`} />
            )}
          </li>
        ))}
      </ol>
      <p className="mt-2 text-xs font-semibold uppercase tracking-wide text-muted sm:hidden">
        Step {step + 1} of 3: {STEPS[step]}
      </p>

      <form noValidate onSubmit={submit} className="mt-5 grid gap-5">
        <input
          value={honeypot}
          onChange={(e) => setHoneypot(e.target.value)}
          tabIndex={-1}
          autoComplete="off"
          aria-hidden="true"
          className="absolute left-[-9999px] h-0 w-0 opacity-0"
        />

        {step === 0 && (
          <>
            <label>
              {label("Website address", false, "(if it is live)")}
              <input
                value={website}
                onChange={(e) => setWebsite(e.target.value)}
                type="url"
                inputMode="url"
                placeholder="yourwebsite.com"
                className={inputCls()}
              />
            </label>

            <label>
              {label("Which platform is your website on?", true)}
              <select
                value={platform}
                onChange={(e) => {
                  setPlatform(e.target.value);
                  clear("platform");
                }}
                className={`${inputCls(errors.platform)} appearance-none bg-[length:12px] bg-[right_1rem_center] bg-no-repeat pr-10 ${platform ? "" : "text-muted"}`}
                style={CHEVRON}
              >
                <option value="">Select your platform</option>
                {[...PLATFORMS.map((p) => p.name), "Not sure"].map((p) => (
                  <option key={p} className="text-ink">
                    {p}
                  </option>
                ))}
              </select>
              {err("platform")}
            </label>

            <div>
              {label("What problems are you facing?", true, "(select all that apply)")}
              <MultiSelect
                options={FORM_PROBLEMS}
                value={problems}
                onChange={(v) => {
                  setProblems(v);
                  clear("problems");
                }}
                placeholder="Select problems"
                invalid={!!errors.problems}
              />
              {err("problems")}
            </div>

            <div>
              {label("Why do you want website maintenance?", true, "(select all that apply)")}
              <MultiSelect
                options={FORM_REASONS}
                value={reasons}
                onChange={(v) => {
                  setReasons(v);
                  clear("reason");
                }}
                placeholder="Select reasons"
                invalid={!!errors.reason}
              />
              {err("reason")}
            </div>
          </>
        )}

        {step === 1 && (
          <>
            <fieldset>
              <legend>{label("Which logins do you have?", true)}</legend>
              <div className="divide-y divide-[var(--color-line)] rounded-xl border border-[var(--color-line)]">
                {FORM_ACCESS.map((a) => (
                  <div key={a.key} className="flex items-center justify-between gap-2 px-3 py-2">
                    <span className="text-sm text-ink">{a.q}</span>
                    <span className="flex shrink-0 overflow-hidden rounded-lg border border-[var(--color-line)]" role="radiogroup" aria-label={a.q}>
                      {ACCESS_ANSWERS.map((ans) => {
                        const on = access[a.key] === ans;
                        return (
                          <button
                            key={ans}
                            type="button"
                            role="radio"
                            aria-checked={on}
                            onClick={() => {
                              setAccess((cur) => ({ ...cur, [a.key]: ans }));
                              clear("access");
                            }}
                            className={`px-2.5 py-1 text-xs font-semibold transition ${
                              on ? "bg-orange text-white" : "bg-white text-muted hover:text-ink"
                            }`}
                          >
                            {ans}
                          </button>
                        );
                      })}
                    </span>
                  </div>
                ))}
              </div>
              <p className="mt-2 flex items-center gap-1.5 text-xs text-muted">
                <Lock aria-hidden className="h-3 w-3 shrink-0" />
                Never type passwords here. No login? I will help you recover it.
              </p>
              {err("access")}
            </fieldset>
          </>
        )}

        {step === 2 && (
          <>
            <label>
              {label("Your name", true)}
              <input
                value={name}
                onChange={(e) => {
                  setName(e.target.value);
                  clear("name");
                }}
                autoComplete="name"
                placeholder="Full name"
                className={inputCls(errors.name)}
              />
              {err("name")}
            </label>

            <div>
              {label("Phone / WhatsApp number", true)}
              <div
                className={`flex overflow-hidden rounded-xl border bg-white transition ${
                  errors.phone ? "border-red-500" : "border-[var(--color-line)] focus-within:border-orange"
                }`}
              >
                <div className="relative shrink-0">
                  <span
                    aria-hidden
                    className="pointer-events-none flex h-full items-center gap-1 border-r border-[var(--color-line)] pl-3 pr-2"
                  >
                    <span className="text-base leading-none">{flagOf(country)}</span>
                    <span className="font-medium text-ink">+{dial}</span>
                  </span>
                  <select
                    aria-label="Country calling code"
                    value={country}
                    onChange={(e) => setCountry(e.target.value)}
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
                  value={phone}
                  onChange={(e) => {
                    setPhone(e.target.value);
                    clear("phone");
                  }}
                  type="tel"
                  inputMode="tel"
                  autoComplete="tel-national"
                  placeholder="98765 43210"
                  className="min-w-0 flex-1 bg-transparent px-4 py-2.5 text-ink outline-none"
                />
              </div>
              {err("phone")}
            </div>

            <label>
              {label("Email", true)}
              <input
                value={email}
                onChange={(e) => {
                  setEmail(e.target.value);
                  clear("email");
                }}
                type="email"
                inputMode="email"
                autoComplete="email"
                placeholder="you@company.com"
                className={inputCls(errors.email)}
              />
              {err("email")}
            </label>

          </>
        )}

        {errors.form && (
          <p role="alert" className="rounded-xl bg-red-50 px-4 py-2.5 text-sm font-medium text-red-700">
            {errors.form}
          </p>
        )}

        <div className="flex gap-3">
          {step > 0 && (
            <button type="button" onClick={() => setStep((s) => s - 1)} className="btn btn-outline flex-1">
              Back
            </button>
          )}
          {step < 2 ? (
            <button type="button" onClick={next} className="btn btn-primary flex-1">
              Next step
            </button>
          ) : (
            <button type="submit" disabled={busy} className="btn btn-primary flex-1 disabled:opacity-70">
              {busy ? "Sending…" : "Submit request"}
            </button>
          )}
        </div>

        <p className="-mt-2 text-center text-xs text-muted">
          Your details go only to me, by email and WhatsApp.
        </p>
      </form>
    </div>
  );
}
