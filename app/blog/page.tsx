import type { Metadata } from "next";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import ConsultPopup from "@/components/ConsultPopup";
import BackToTop from "@/components/BackToTop";
import MobileBookBar from "@/components/MobileBookBar";
import Reveal from "@/components/Reveal";
import Breadcrumbs from "@/components/Breadcrumbs";
import PostList from "@/components/blog/PostList";
import BlogSidebar, { BookPanel } from "@/components/blog/BlogSidebar";
import { POSTS_BY_DATE } from "@/lib/blog";
import { SITE_URL, canonicalUrl } from "@/lib/seo";

const TITLE = "Blog | Sushant Rana";
const DESCRIPTION =
  "Essays on revenue systems, performance marketing, lead quality and practical AI automation — written from live client accounts, not theory.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: canonicalUrl("/blog") },
  openGraph: {
    title: TITLE,
    description: DESCRIPTION,
    url: canonicalUrl("/blog"),
    type: "website",
  },
};

// Blog is a CollectionPage listing the posts, tied back to the same Person and
// WebSite @ids the home page declares so the entity graph stays one graph.
const structuredData = {
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": `${canonicalUrl("/blog")}#webpage`,
  url: canonicalUrl("/blog"),
  name: TITLE,
  description: DESCRIPTION,
  isPartOf: { "@id": `${SITE_URL}/#website` },
  publisher: { "@id": `${SITE_URL}/#person` },
  inLanguage: "en",
  mainEntity: {
    "@type": "ItemList",
    itemListElement: POSTS_BY_DATE.map((p, i) => ({
      "@type": "ListItem",
      position: i + 1,
      url: canonicalUrl(`/blog/${p.slug}`),
      name: p.title,
    })),
  },
};

export default function Page() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
      />
      <Nav />
      <main className="bg-section pb-20 pt-32 md:pt-36">
        <div className="wrap-wide">
          <Breadcrumbs trail={[{ label: "Blog" }]} className="mb-6" />
          <Reveal>
            <span className="script-label">Latest insights</span>
            <h1 className="mt-4 max-w-4xl text-[clamp(2rem,5vw,3.4rem)] font-extrabold text-ink">
              Thinking you can <span className="text-orange">use</span>
            </h1>
            <p className="mt-4 max-w-2xl text-lg text-muted">{DESCRIPTION}</p>
          </Reveal>

          {/* No items-start: the sidebar column has to stretch to the row
              height for its sticky panel to have anywhere to travel. */}
          <div className="mt-12 grid gap-10 lg:grid-cols-[minmax(0,1fr)_340px]">
            <PostList posts={POSTS_BY_DATE} />
            <BlogSidebar />
          </div>

          {/* Below lg the sidebar is hidden, so the booking panel renders here
              in normal flow — the CTA must not disappear on a phone. */}
          <div className="mt-12 lg:hidden">
            <BookPanel />
          </div>
        </div>
      </main>
      <Footer />
      <ConsultPopup />
      <BackToTop />
      <MobileBookBar />
    </>
  );
}
