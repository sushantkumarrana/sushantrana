"use client";

/** Sticky "Book an Appointment" bar — mobile only. Opens the consult popup
 *  (text starts with "Book", caught by ConsultPopup's delegated listener). */
export default function MobileBookBar() {
  return (
    <div className="fixed inset-x-0 bottom-0 z-[80] border-t border-[var(--color-line)] bg-white/90 p-3 backdrop-blur-lg sm:hidden">
      <a href="#contact" className="btn btn-primary w-full">
        Book an Appointment
      </a>
    </div>
  );
}
