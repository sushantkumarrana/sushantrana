"use client";

import { useId, useState } from "react";
import { useRouter } from "next/navigation";
import { COUNTRIES, COUNTRY_BY_ISO, DEFAULT_COUNTRY, flagOf } from "@/lib/countries";
import { validateEmail, validatePhone } from "@/lib/validation";
import { SHOPIFY_LEAD_KEY } from "@/lib/whatsapp";
import { pushLead } from "@/lib/datalayer";

/**
 * Three-step hero enquiry form, matching the reference page the client asked
 * me to copy: contact, project, timeline.
 *
 * It posts to the same /api/lead endpoint as the popup form. The extra
 * qualifying answers (platform, revenue, products, timeline, budget, source)
 * are folded into the `message` field rather than added as columns — the route
 * allow-lists `service` against the shared catalogue, so this form always sends
 * "Shopify Store Development" there and keeps the detail in the message. That
 * means no database migration and no second endpoint to keep in sync.
 */

const SERVICES = [
  "New Shopify store",
  "Store redesign",
  "Migration to Shopify",
  "Speed optimisation",
  "Custom app",
  "Cart / checkout work",
  "UX / UI audit",
  "Product page content",
  "Other",
];
const PLATFORMS = ["No store yet", "Shopify", "WooCommerce", "Magento", "BigCommerce", "Other"];
const REVENUE = ["Pre-launch", "Under ₹1L", "₹1L - 5L", "₹5L - 25L", "₹25L - 1Cr", "₹1Cr+"];
const PRODUCTS = ["1 - 50", "51 - 200", "201 - 500", "500+"];
const TIMELINE = ["ASAP", "Within 2 weeks", "Within 1 month", "Within 3 months", "Just exploring"];
const BUDGET = ["Under ₹25K", "₹25K - 50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+"];
const SOURCE = ["Google", "Social media", "Referral", "LinkedIn", "Other"];

const STEPS = ["Contact", "Project", "Timeline"];

/** Where a completed Shopify enquiry lands: this page's own confirmation
 *  screen, which hands the visitor on to WhatsApp with their answers typed. */
const THANK_YOU = "/thank-you-shopify-store-development";

type Errors = Partial<Record<"name" | "email" | "phone" | "company" | "form", string>>;

export default function HeroForm() {
  const router = useRouter();
  const uid = useId();

  const [step, setStep] = useState(0);
  const [busy, setBusy] = useState(false);
  const [errors, setErrors] = useState<Errors>({});

  const [country, setCountry] = useState(DEFAULT_COUNTRY);
  const [v, setV] = useState({
    name: "",
    email: "",
    phone: "",
    company: "",
    service: "",
    platform: "",
    revenue: "",
    products: "",
    timeline: "",
    budget: "",
    details: "",
    source: "",
    website: "", // honeypot
  });

  const set = (k: keyof typeof v) => (e: { target: { value: string } }) => {
    setV((p) => ({ ...p, [k]: e.target.value }));
    setErrors((p) => ({ ...p, [k]: undefined, form: undefined }));
  };

  const dial = COUNTRY_BY_ISO.get(country)?.dial ?? "91";

  const inputCls = (bad?: string) =>
    `w-full rounded-xl border bg-white px-4 py-2.5 text-ink outline-none transition ${
      bad ? "border-red-500" : "border-[var(--color-line)] focus:border-orange"
    }`;

  const selectCls = `${inputCls()} appearance-none bg-[length:12px] bg-[right_1rem_center] bg-no-repeat pr-10`;
  const chevron = {
    backgroundImage:
      "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235a5a5a' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='m6 9 6 6 6-6'/></svg>\")",
  };

  const label = (text: string, required = false) => (
    <span className="mb-1 block text-sm font-semibold text-ink">
      {text} {required && <span className="text-orange">*</span>}
    </span>
  );

  const err = (k: keyof Errors) =>
    errors[k] ? (
      <p role="alert" className="mt-1 text-xs font-medium text-red-600">
        {errors[k]}
      </p>
    ) : null;

  /** Step 1 is the only step with free text, so it is the only one that needs
   *  the shared email and phone validators. */
  async function validateStep1() {
    const next: Errors = {};
    if (!v.name.trim()) next.name = "Please tell me your name.";
    if (!v.company.trim()) next.company = "Please add your business or brand name.";

    const e = validateEmail(v.email);
    if (!e.ok) next.email = e.error;
    const p = await validatePhone(country, v.phone);
    if (!p.ok) next.phone = p.error;

    setErrors(next);
    return Object.keys(next).length === 0;
  }

  function validateStep2() {
    if (!v.service || !v.platform || !v.revenue) {
      setErrors({ form: "Please answer the required questions." });
      return false;
    }
    return true;
  }

  async function next() {
    if (busy) return;
    if (step === 0) {
      setBusy(true);
      const ok = await validateStep1();
      setBusy(false);
      if (!ok) return;
    }
    if (step === 1 && !validateStep2()) return;
    setStep((s) => s + 1);
  }

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    if (busy) return;
    if (!v.timeline || !v.budget) {
      setErrors({ form: "Please pick a timeline and a budget range." });
      return;
    }
    setBusy(true);
    setErrors({});

    // Everything the shared endpoint has no column for travels in the message,
    // so the notification email still carries the full qualification.
    const message = [
      `What they need: ${v.service}`,
      `Current platform: ${v.platform}`,
      `Monthly revenue: ${v.revenue}`,
      v.products && `Number of products: ${v.products}`,
      `Timeline: ${v.timeline}`,
      `Budget: ${v.budget}`,
      v.source && `Heard about me via: ${v.source}`,
      v.details && `\nProject notes:\n${v.details}`,
    ]
      .filter(Boolean)
      .join("\n");

    try {
      const res = await fetch("/api/lead", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: v.name,
          email: v.email,
          phone: v.phone,
          phoneCountry: country,
          business: v.company,
          service: "Shopify Store Development",
          enquiryType: "service",
          message,
          company_website: v.website,
          sourcePath: window.location.pathname,
        }),
      });
      const data = await res.json().catch(() => ({}));

      if (!res.ok || !data.ok) {
        // A rejected email or phone belongs back on step 1 next to the field.
        if (data.field === "email" || data.field === "phone") {
          setErrors({ [data.field]: data.error } as Errors);
          setStep(0);
        } else {
          setErrors({ form: data.error || "Could not send. Please try again." });
        }
        setBusy(false);
        return;
      }
      pushLead(
        "shopify_store_development",
        {
          company: v.company,
          service: v.service,
          platform: v.platform,
          revenue: v.revenue,
          products: v.products,
          timeline: v.timeline,
          budget: v.budget,
          source: v.source,
          details: v.details,
        },
        { name: v.name, email: v.email, phone: `+${dial}${v.phone.replace(/\D/g, "")}` }
      );

      try {
        sessionStorage.setItem(
          SHOPIFY_LEAD_KEY,
          JSON.stringify({
            name: v.name,
            company: v.company,
            email: v.email,
            phone: `+${dial} ${v.phone}`,
            service: v.service,
            platform: v.platform,
            revenue: v.revenue,
            products: v.products,
            timeline: v.timeline,
            budget: v.budget,
            details: v.details,
          })
        );
      } catch {
        // Private mode or a full quota: the lead is already saved server-side,
        // so the thank-you page just falls back to a generic message.
      }
      router.push(THANK_YOU);
    } catch {
      setErrors({ form: "Network problem. Please check your connection and retry." });
      setBusy(false);
    }
  }

  return (
    <div className="card p-5 md:p-6">
      <h2 className="text-xl font-extrabold text-ink">Start your store build</h2>
      <p className="mt-1.5 text-sm text-muted">
        Free consultation. I will scope your project within 24 hours.
      </p>

      {/* step indicator */}
      <ol className="mt-5 flex list-none items-center gap-2">
        {STEPS.map((s, i) => (
          <li key={s} className="flex flex-1 items-center gap-2">
            <span
              className={`grid h-7 w-7 shrink-0 place-items-center rounded-full text-xs font-bold transition ${
                i <= step ? "bg-orange text-white" : "bg-ink/10 text-muted"
              }`}
            >
              {i + 1}
            </span>
            <span
              className={`text-xs font-semibold uppercase tracking-wide ${
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

      <form noValidate onSubmit={submit} className="mt-5 grid gap-3">
        {/* honeypot */}
        <input
          value={v.website}
          onChange={set("website")}
          tabIndex={-1}
          autoComplete="off"
          aria-hidden="true"
          className="absolute left-[-9999px] h-0 w-0 opacity-0"
        />

        {step === 0 && (
          <>
            <label>
              {label("Full name", true)}
              <input
                value={v.name}
                onChange={set("name")}
                placeholder="Your name"
                autoComplete="name"
                className={inputCls(errors.name)}
              />
              {err("name")}
            </label>

            <label>
              {label("Business email", true)}
              <input
                value={v.email}
                onChange={set("email")}
                type="email"
                inputMode="email"
                autoComplete="email"
                placeholder="you@company.com"
                className={inputCls(errors.email)}
              />
              {err("email")}
            </label>

            <div>
              {label("Phone number", true)}
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
                  value={v.phone}
                  onChange={set("phone")}
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
              {label("Company / brand name", true)}
              <input
                value={v.company}
                onChange={set("company")}
                placeholder="Your brand name"
                autoComplete="organization"
                className={inputCls(errors.company)}
              />
              {err("company")}
            </label>
          </>
        )}

        {step === 1 && (
          <>
            <label>
              {label("What do you need?", true)}
              <select value={v.service} onChange={set("service")} className={selectCls} style={chevron}>
                <option value="">Select a service</option>
                {SERVICES.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
            <label>
              {label("Current platform", true)}
              <select value={v.platform} onChange={set("platform")} className={selectCls} style={chevron}>
                <option value="">Select your platform</option>
                {PLATFORMS.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
            <label>
              {label("Monthly revenue", true)}
              <select value={v.revenue} onChange={set("revenue")} className={selectCls} style={chevron}>
                <option value="">Select range</option>
                {REVENUE.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
            <label>
              {label("Number of products")}
              <select value={v.products} onChange={set("products")} className={selectCls} style={chevron}>
                <option value="">Select range</option>
                {PRODUCTS.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
          </>
        )}

        {step === 2 && (
          <>
            <label>
              {label("Timeline", true)}
              <select value={v.timeline} onChange={set("timeline")} className={selectCls} style={chevron}>
                <option value="">When do you want to start?</option>
                {TIMELINE.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
            <label>
              {label("Budget range", true)}
              <select value={v.budget} onChange={set("budget")} className={selectCls} style={chevron}>
                <option value="">Select your budget</option>
                {BUDGET.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
            <label>
              {label("Tell me more about your project")}
              <textarea
                value={v.details}
                onChange={set("details")}
                rows={3}
                placeholder="Current challenges, goals, specific requirements..."
                className={inputCls()}
              />
            </label>
            <label>
              {label("How did you hear about me?")}
              <select value={v.source} onChange={set("source")} className={selectCls} style={chevron}>
                <option value="">Select</option>
                {SOURCE.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </label>
          </>
        )}

        {errors.form && (
          <p role="alert" className="rounded-xl bg-red-50 px-4 py-2.5 text-sm font-medium text-red-700">
            {errors.form}
          </p>
        )}

        <div className="mt-2 flex gap-3">
          {step > 0 && (
            <button
              type="button"
              onClick={() => setStep((s) => s - 1)}
              className="btn btn-outline flex-1"
            >
              Back
            </button>
          )}
          {step < 2 ? (
            <button
              type="button"
              onClick={next}
              disabled={busy}
              className="btn btn-primary flex-1 disabled:opacity-70"
            >
              {busy ? "Checking…" : "Next step"}
            </button>
          ) : (
            <button
              type="submit"
              disabled={busy}
              className="btn btn-primary flex-1 disabled:opacity-70"
            >
              {busy ? "Sending…" : "Get free consultation"}
            </button>
          )}
        </div>

        <p id={`${uid}-note`} className="text-center text-xs text-muted">
          No obligation. Your details stay with me.
        </p>
      </form>
    </div>
  );
}
