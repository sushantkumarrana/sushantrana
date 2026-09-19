import type { Metadata } from "next";
import MaintenanceThankYou from "@/components/maintenance/ThankYou";

// Confirmation screens have no search value and must never be indexed.
export const metadata: Metadata = {
  title: "Thank you | Website maintenance request | Sushant Rana",
  description: "Your website maintenance request has been received.",
  robots: { index: false, follow: false },
};

export default function Page() {
  return <MaintenanceThankYou />;
}
