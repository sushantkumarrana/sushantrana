"use client";

import Reveal from "../Reveal";

const POSTS = [
  { cat: "Business Strategy", date: "18 Jun 2026", img: "/blog/post-1.png", title: "Revenue Systems vs Marketing Campaigns: Why One Compounds and the Other Expires", excerpt: "Campaigns end. Systems compound. The structural difference between businesses that grow predictably and businesses that buy growth one month at a time." },
  { cat: "Marketing", date: "4 Jun 2026", img: "/blog/post-2.png", title: "Lead Quality Over Lead Volume: The Metric Shift That Changes Everything", excerpt: "A thousand leads that never answer the phone cost more than a hundred that do. How to rebuild campaigns around qualified conversations." },
  { cat: "AI", date: "21 May 2026", img: "/blog/post-3.png", title: "Practical AI Automation for Businesses That Don't Have a Data Team", excerpt: "You don't need ML engineers. You need five workflows: lead scoring, follow-up, reporting, routing, and reactivation." },
];

export default function Blog() {
  return (
    <section id="blog" className="section">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">Latest insights</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Thinking you can <span className="text-orange">use</span>
          </h2>
        </Reveal>

        <div className="mt-12 grid gap-6 md:grid-cols-3">
          {POSTS.map((p, i) => (
            <Reveal key={p.title} delay={i * 0.08}>
              <article className="card group flex h-full flex-col overflow-hidden">
                <div className="aspect-[16/10] overflow-hidden">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={p.img} alt={p.title} className="h-full w-full object-cover transition duration-500 group-hover:scale-105" />
                </div>
                <div className="flex flex-1 flex-col p-6">
                  <div className="flex items-center gap-2 font-[family-name:var(--font-display)] text-xs font-semibold uppercase tracking-wide text-orange">
                    {p.cat} <span className="text-muted">· {p.date}</span>
                  </div>
                  <h3 className="mt-3 text-lg font-extrabold leading-snug text-ink">{p.title}</h3>
                  <p className="mt-3 text-sm text-body">{p.excerpt}</p>
                  <a href="#" className="mt-auto inline-flex items-center gap-2 pt-5 font-[family-name:var(--font-display)] text-sm font-semibold text-ink transition group-hover:gap-3 group-hover:text-orange">
                    Read article
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
                  </a>
                </div>
              </article>
            </Reveal>
          ))}
        </div>

        <div className="mt-10 text-center">
          <a href="#" className="btn btn-outline">Browse all articles</a>
        </div>
      </div>
    </section>
  );
}
