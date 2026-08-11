import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Image from "next/image";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import ConsultPopup from "@/components/ConsultPopup";
import BackToTop from "@/components/BackToTop";
import MobileBookBar from "@/components/MobileBookBar";
import Reveal from "@/components/Reveal";
import Breadcrumbs from "@/components/Breadcrumbs";
import Prose from "@/components/blog/Prose";
import PostCard from "@/components/blog/PostCard";
import BlogSidebar, { BookPanel } from "@/components/blog/BlogSidebar";
import {
  POSTS,
  formatDate,
  getPost,
  readingTime,
  relatedPosts,
  tableOfContents,
} from "@/lib/blog";
import { SITE_URL, canonicalUrl } from "@/lib/seo";

// Every post is known at build time, so all three pages are prerendered and
// any other slug 404s instead of rendering an empty shell.
export function generateStaticParams() {
  return POSTS.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const post = getPost(slug);
  if (!post) return { title: "Article not found | Sushant Rana" };

  const url = canonicalUrl(`/blog/${post.slug}`);
  return {
    title: `${post.title} | Sushant Rana`,
    description: post.excerpt,
    alternates: { canonical: url },
    openGraph: {
      title: post.title,
      description: post.excerpt,
      url,
      type: "article",
      publishedTime: post.date,
      authors: ["Sushant Rana"],
      images: [{ url: post.img }],
    },
    twitter: {
      card: "summary_large_image",
      title: post.title,
      description: post.excerpt,
      images: [post.img],
    },
  };
}

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = getPost(slug);
  if (!post) notFound();

  const url = canonicalUrl(`/blog/${post.slug}`);
  const toc = tableOfContents(post);
  const more = relatedPosts(post.slug);

  const structuredData = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BlogPosting",
        "@id": `${url}#article`,
        headline: post.title,
        description: post.excerpt,
        url,
        mainEntityOfPage: url,
        datePublished: post.date,
        dateModified: post.date,
        image: `${SITE_URL}${post.img}`,
        articleSection: post.cat,
        author: { "@id": `${SITE_URL}/#person` },
        publisher: { "@id": `${SITE_URL}/#person` },
        isPartOf: { "@id": `${SITE_URL}/#website` },
        inLanguage: "en",
      },
      {
        // Breadcrumbs let Google render "Home > Blog > Title" instead of a
        // bare URL in the result.
        "@type": "BreadcrumbList",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Home", item: canonicalUrl("/") },
          { "@type": "ListItem", position: 2, name: "Blog", item: canonicalUrl("/blog") },
          { "@type": "ListItem", position: 3, name: post.title, item: url },
        ],
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
      />
      <Nav />

      <main className="bg-section pb-20 pt-32 md:pt-36">
        <div className="wrap-wide">
          {/* jsonLd={false}: the BreadcrumbList is already declared in the
              @graph above, and two copies would be a duplicate entity. */}
          <Breadcrumbs
            jsonLd={false}
            trail={[{ label: "Blog", href: "/blog" }, { label: post.title }]}
          />

          {/* No items-start: the sidebar column has to stretch to the row
              height for its sticky panel to have anywhere to travel. */}
          <div className="mt-6 grid gap-10 lg:grid-cols-[minmax(0,1fr)_340px]">
            {/* ---------- article ---------- */}
            <article>
              <Reveal>
                <div className="flex flex-wrap items-center gap-2 font-[family-name:var(--font-display)] text-xs font-semibold uppercase tracking-wide text-orange">
                  {post.cat}
                  <span className="text-muted">
                    ·{" "}
                    <time dateTime={post.date}>{formatDate(post.date)}</time> ·{" "}
                    {readingTime(post)} min read
                  </span>
                </div>
                <h1 className="mt-4 text-[clamp(1.9rem,4.4vw,3rem)] font-extrabold leading-[1.08] text-ink">
                  {post.title}
                </h1>
                <p className="mt-5 max-w-2xl text-lg text-muted">{post.excerpt}</p>
              </Reveal>

              <div className="relative mt-9 aspect-[16/10] overflow-hidden rounded-3xl">
                {/* LCP image on this route — eager, and sized for the article
                    column rather than the full viewport. */}
                <Image
                  src={post.img}
                  alt={post.title}
                  fill
                  priority
                  sizes="(max-width: 1024px) 100vw, 62vw"
                  className="object-cover"
                />
              </div>

              {toc.length > 1 && (
                <nav
                  aria-label="On this page"
                  className="mt-9 rounded-2xl border border-[var(--color-line)] bg-white/70 p-6"
                >
                  <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-[0.14em] text-muted">
                    In this article
                  </p>
                  <ol className="mt-3 grid gap-2">
                    {toc.map((h, i) => (
                      <li key={h.id} className="flex gap-3 text-sm">
                        <span className="font-semibold text-orange">
                          {String(i + 1).padStart(2, "0")}
                        </span>
                        <a href={`#${h.id}`} className="text-body transition hover:text-orange">
                          {h.text}
                        </a>
                      </li>
                    ))}
                  </ol>
                </nav>
              )}

              <div className="mt-10">
                <Prose blocks={post.body} />
              </div>

              {/* author / close */}
              <div className="mt-14 flex flex-wrap items-center gap-5 rounded-3xl border border-[var(--color-line)] bg-white/70 p-6">
                <Image
                  src="/about/about.png"
                  alt="Sushant Rana"
                  width={72}
                  height={72}
                  className="h-16 w-16 rounded-full object-cover"
                />
                <div className="min-w-[220px] flex-1">
                  <p className="font-[family-name:var(--font-display)] font-bold text-ink">
                    Sushant Rana
                  </p>
                  <p className="text-sm text-muted">
                    Business Growth Consultant. 8+ years building revenue systems across
                    India, the USA, Canada and Australia.
                  </p>
                </div>
                {/* Text starts with "Book" — ConsultPopup's delegated listener
                    catches it and opens the consultation form. */}
                <a href="#contact" className="btn btn-primary !min-h-[46px] !px-6 text-sm">
                  Book a free call
                </a>
              </div>
            </article>

            {/* ---------- sticky sidebar ---------- */}
            <BlogSidebar />
          </div>

          {/* Sidebar is lg-only; on phones the booking panel sits inline here. */}
          <div className="mt-12 lg:hidden">
            <BookPanel />
          </div>

          {more.length > 0 && (
            <section className="mt-20">
              <h2 className="text-[clamp(1.4rem,3vw,2.1rem)] font-extrabold text-ink">
                Keep <span className="text-orange">reading</span>
              </h2>
              <div className="mt-8 grid gap-6 sm:grid-cols-2">
                {more.map((p, i) => (
                  <Reveal key={p.slug} delay={i * 0.08}>
                    <PostCard post={p} sizes="(max-width: 640px) 100vw, 45vw" />
                  </Reveal>
                ))}
              </div>
            </section>
          )}
        </div>
      </main>

      <Footer />
      <ConsultPopup />
      <BackToTop />
      <MobileBookBar />
    </>
  );
}
