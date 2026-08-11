"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import Reveal from "../Reveal";
import PostCard from "./PostCard";
import { CATEGORIES, formatDate, readingTime, type Post } from "@/lib/blog";

const ALL = "All";

/**
 * The /blog listing: newest post as a wide feature, the rest as cards, with a
 * client-side category filter. Filtering in the browser (rather than
 * /blog?cat=) keeps every article on one indexable URL — with three posts
 * there is nothing to paginate and nothing worth a second crawlable page.
 */
export default function PostList({ posts }: { posts: Post[] }) {
  const [cat, setCat] = useState(ALL);
  const shown = cat === ALL ? posts : posts.filter((p) => p.cat === cat);

  const [feature, ...rest] = shown;

  return (
    <div>
      <div className="flex flex-wrap gap-2">
        {[ALL, ...CATEGORIES].map((c) => {
          const on = c === cat;
          return (
            <button
              key={c}
              type="button"
              onClick={() => setCat(c)}
              aria-pressed={on}
              className={`rounded-full border px-4 py-2 font-[family-name:var(--font-display)] text-sm font-semibold transition ${
                on
                  ? "border-orange bg-orange text-white shadow-[0_10px_24px_-14px_rgba(var(--orange-rgb),0.8)]"
                  : "border-[var(--color-line)] bg-white/70 text-body hover:border-orange hover:text-orange"
              }`}
            >
              {c}
            </button>
          );
        })}
      </div>

      {/* Featured — the newest post in the active category */}
      {feature && (
        <Reveal>
          <article className="card group mt-8 grid overflow-hidden md:grid-cols-2">
            <Link
              href={`/blog/${feature.slug}`}
              className="relative block aspect-[16/10] overflow-hidden md:aspect-auto md:min-h-[280px]"
            >
              <Image
                src={feature.img}
                alt={feature.title}
                fill
                sizes="(max-width: 768px) 100vw, 45vw"
                priority
                className="object-cover transition duration-500 group-hover:scale-105"
              />
            </Link>
            <div className="flex flex-col justify-center p-7 md:p-9">
              <div className="flex flex-wrap items-center gap-2 font-[family-name:var(--font-display)] text-xs font-semibold uppercase tracking-wide text-orange">
                Latest · {feature.cat}
                <span className="text-muted">
                  · {formatDate(feature.date)} · {readingTime(feature)} min read
                </span>
              </div>
              <h2 className="mt-3 text-[clamp(1.3rem,2.4vw,1.8rem)] font-extrabold leading-tight text-ink">
                <Link href={`/blog/${feature.slug}`} className="transition group-hover:text-orange">
                  {feature.title}
                </Link>
              </h2>
              <p className="mt-3 text-body">{feature.excerpt}</p>
              <Link
                href={`/blog/${feature.slug}`}
                className="mt-6 inline-flex items-center gap-2 font-[family-name:var(--font-display)] text-sm font-semibold text-ink transition hover:gap-3 hover:text-orange"
              >
                Read article
                <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </article>
        </Reveal>
      )}

      {rest.length > 0 && (
        <div className="mt-6 grid gap-6 sm:grid-cols-2">
          {rest.map((p, i) => (
            <Reveal key={p.slug} delay={i * 0.08}>
              <PostCard post={p} sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 30vw" />
            </Reveal>
          ))}
        </div>
      )}

      {shown.length === 0 && (
        <p className="mt-10 rounded-2xl border border-[var(--color-line)] bg-white/60 p-8 text-center text-muted">
          Nothing published under {cat} yet.
        </p>
      )}
    </div>
  );
}
