"use client";

import Link from "next/link";
import SimplePage from "./SimplePage";

/** Placeholder shown for nav/footer links whose page isn't built yet. */
export default function ComingSoon({ pageName }: { pageName?: string }) {
  return (
    <SimplePage
      label="Under development"
      title="This page is"
      accent="coming soon."
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
      {pageName ? (
        <p>
          <span className="font-semibold text-ink">{pageName}</span>{" "}
          is currently being built and will be live in a few days. In the meantime,
          book a free call and I&apos;ll answer anything you need about it directly.
        </p>
      ) : (
        <p>
          This page is currently being built and will be live in a few days. In the
          meantime, book a free call and I&apos;ll answer anything you need directly.
        </p>
      )}
    </SimplePage>
  );
}
