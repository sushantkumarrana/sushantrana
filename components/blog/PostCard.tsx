import Image from "next/image";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { formatDate, readingTime, type Post } from "@/lib/blog";

/** Article card. Used on /blog, in the "Keep reading" row, and on the home
 *  page teaser, so all three stay identical by construction. */
export default function PostCard({
  post,
  /** `sizes` must match where the card is used or the browser downloads the
   *  wrong candidate — the listing grid is narrower than the home page's. */
  sizes = "(max-width: 768px) 100vw, 33vw",
  priority = false,
}: {
  post: Post;
  sizes?: string;
  priority?: boolean;
}) {
  return (
    <article className="card group flex h-full flex-col overflow-hidden">
      <Link href={`/blog/${post.slug}`} className="relative block aspect-[16/10] overflow-hidden">
        <Image
          src={post.img}
          alt={post.title}
          fill
          sizes={sizes}
          priority={priority}
          className="object-cover transition duration-500 group-hover:scale-105"
        />
      </Link>
      <div className="flex flex-1 flex-col p-6">
        <div className="flex flex-wrap items-center gap-2 font-[family-name:var(--font-display)] text-xs font-semibold uppercase tracking-wide text-orange">
          {post.cat}
          <span className="text-muted">
            · {formatDate(post.date)} · {readingTime(post)} min read
          </span>
        </div>
        <h3 className="mt-3 text-lg font-extrabold leading-snug text-ink">
          <Link href={`/blog/${post.slug}`} className="transition group-hover:text-orange">
            {post.title}
          </Link>
        </h3>
        <p className="mt-3 text-sm text-body">{post.excerpt}</p>
        <Link
          href={`/blog/${post.slug}`}
          className="mt-auto inline-flex items-center gap-2 pt-5 font-[family-name:var(--font-display)] text-sm font-semibold text-ink transition group-hover:gap-3 group-hover:text-orange"
        >
          Read article
          <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </article>
  );
}
