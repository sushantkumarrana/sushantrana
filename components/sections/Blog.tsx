"use client";

import Link from "next/link";
import Reveal from "../Reveal";
import PostCard from "../blog/PostCard";
import { POSTS_BY_DATE } from "@/lib/blog";

/** Home page teaser — the three newest posts, read from the same source as
 *  /blog so a new article appears here without touching this file. */
export default function Blog() {
  const posts = POSTS_BY_DATE.slice(0, 3);

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
          {posts.map((p, i) => (
            <Reveal key={p.slug} delay={i * 0.08}>
              <PostCard post={p} />
            </Reveal>
          ))}
        </div>

        <div className="mt-10 text-center">
          <Link href="/blog" className="btn btn-outline">
            Browse all articles
          </Link>
        </div>
      </div>
    </section>
  );
}
