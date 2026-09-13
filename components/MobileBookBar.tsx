"use client";

/** Sticky mobile call-to-action bar.
 *
 *  Defaults to "Book an Appointment", which the site-wide ConsultPopup catches
 *  by its leading "Book". A page with its own popup passes its own label and
 *  relies on data-consult, which both popups listen for. */
export default function MobileBookBar({
  label = "Book an Appointment",
}: {
  label?: string;
}) {
  return (
    <div className="fixed inset-x-0 bottom-0 z-[80] border-t border-[var(--color-line)] bg-white/90 p-3 backdrop-blur-lg sm:hidden">
      <a href="#contact" data-consult className="btn btn-primary w-full">
        {label}
      </a>
    </div>
  );
}
