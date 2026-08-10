import Link from "next/link";
import type { Metadata } from "next";
import SimplePage from "@/components/SimplePage";

export const metadata: Metadata = {
  title: "Page not found | Sushant Rana",
  description: "The page you were looking for doesn't exist.",
  robots: { index: false, follow: true },
};

export default function NotFound() {
  return (
    <SimplePage
      label="404"
      title="That page"
      accent="doesn't exist."
      actions={
        <>
          <Link href="/" className="btn btn-primary">
            Back to home
          </Link>
          <a href="#contact" className="btn btn-outline">
            Book an Appointment
          </a>
        </>
      }
    >
      <p>
        The link may be broken or the page may have moved. Head back to the
        homepage, or book a free call and I&apos;ll point you to what you need.
      </p>
    </SimplePage>
  );
}
