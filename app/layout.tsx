import type { Metadata } from "next";
import { Plus_Jakarta_Sans, Ephesis, Mukta, Playwrite_TZ } from "next/font/google";
import Script from "next/script";
import "./globals.css";
import SmoothScroll from "@/components/SmoothScroll";

const GTM_ID = "GTM-KRLQ36TK";

// Plus Jakarta Sans = premium Cal Sans lookalike (swap for real Cal Sans woff2 later)
const jakarta = Plus_Jakarta_Sans({
  variable: "--font-jakarta",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
  display: "swap",
});

const ephesis = Ephesis({
  variable: "--font-ephesis",
  subsets: ["latin"],
  weight: ["400"],
  display: "swap",
});

// Devanagari for the faded सुशांत राणा signature in the footer
const mukta = Mukta({
  variable: "--font-deva",
  subsets: ["devanagari", "latin"],
  weight: ["800"],
  display: "swap",
});

// Playwrite Tanzania — cursive handwriting for section labels
const cookie = Playwrite_TZ({
  variable: "--font-cookie",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://sushantrana.com"),
  title:
    "Sushant Rana — Business Growth Consultant | Revenue Systems, Not Just Campaigns",
  description:
    "I build revenue systems, not just marketing campaigns — strategy, performance marketing, and AI automation working as one engine. 8+ years, 4 markets.",
  openGraph: {
    title: "Sushant Rana — Business Growth Consultant",
    description:
      "Revenue systems, not just campaigns. Strategy, performance marketing, and AI automation as one engine.",
    url: "https://sushantrana.com",
    siteName: "Sushant Rana",
    type: "website",
  },
  robots: { index: true, follow: true },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`${jakarta.variable} ${ephesis.variable} ${mukta.variable} ${cookie.variable}`}>
      <head>
        {/* Google Tag Manager — lives in the root layout, so every route
            (current and any page added later) is tagged automatically. */}
        <Script id="gtm-init" strategy="afterInteractive">
          {`(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','${GTM_ID}');`}
        </Script>
        <noscript>
          <style>{`[style*="opacity"]{opacity:1!important;} [style*="translate"]{transform:none!important;}`}</style>
        </noscript>
      </head>
      <body>
        {/* GTM noscript fallback — must be the first thing inside <body> */}
        <noscript>
          <iframe
            src={`https://www.googletagmanager.com/ns.html?id=${GTM_ID}`}
            height="0"
            width="0"
            style={{ display: "none", visibility: "hidden" }}
          />
        </noscript>
        <SmoothScroll>{children}</SmoothScroll>
      </body>
    </html>
  );
}
