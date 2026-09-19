"use client";

import QuotePopup from "../shopify/QuotePopup";
import MaintenanceForm from "./MaintenanceForm";

/** Every CTA on the maintenance page opens the three-step form. A client
 *  wrapper because the render function cannot cross from a server component. */
export default function MaintenancePopup() {
  return (
    <QuotePopup
      label="Request website maintenance"
      render={(plan) => <MaintenanceForm key={plan ?? ""} initialPlan={plan} compact />}
    />
  );
}
