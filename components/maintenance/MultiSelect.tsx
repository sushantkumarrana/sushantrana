"use client";

import { useEffect, useId, useRef, useState } from "react";
import { Check, ChevronDown } from "lucide-react";

/**
 * Dropdown with checkboxes. Native <select multiple> needs Ctrl-click on
 * desktop and renders as a tall list box, so this keeps the closed state as
 * compact as a normal select. Closes on outside click and Escape.
 */
export default function MultiSelect({
  options,
  value,
  onChange,
  placeholder,
  invalid = false,
}: {
  options: string[];
  value: string[];
  onChange: (next: string[]) => void;
  placeholder: string;
  invalid?: boolean;
}) {
  const [open, setOpen] = useState(false);
  const box = useRef<HTMLDivElement>(null);
  const listId = useId();

  useEffect(() => {
    if (!open) return;
    const away = (e: MouseEvent) => {
      if (!box.current?.contains(e.target as Node)) setOpen(false);
    };
    const esc = (e: KeyboardEvent) => {
      // Stop Escape reaching the popup's own listener, which would close it.
      if (e.key === "Escape") {
        e.stopPropagation();
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", away);
    document.addEventListener("keydown", esc, true);
    return () => {
      document.removeEventListener("mousedown", away);
      document.removeEventListener("keydown", esc, true);
    };
  }, [open]);

  const toggle = (o: string) =>
    onChange(value.includes(o) ? value.filter((v) => v !== o) : [...value, o]);

  return (
    <div ref={box} className="relative">
      <button
        type="button"
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-controls={listId}
        onClick={() => setOpen((o) => !o)}
        className={`flex w-full items-center justify-between gap-3 rounded-xl border bg-white px-4 py-2.5 text-left outline-none transition ${
          invalid ? "border-red-500" : open ? "border-orange" : "border-[var(--color-line)] hover:border-orange"
        }`}
      >
        <span className={`truncate ${value.length ? "text-ink" : "text-muted"}`}>
          {value.length === 0
            ? placeholder
            : value.length === 1
              ? value[0]
              : `${value[0]} +${value.length - 1} more`}
        </span>
        <ChevronDown
          aria-hidden
          className={`h-4 w-4 shrink-0 text-muted transition-transform ${open ? "rotate-180" : ""}`}
        />
      </button>

      {open && (
        <ul
          id={listId}
          role="listbox"
          aria-multiselectable="true"
          data-lenis-prevent
          className="absolute inset-x-0 top-full z-30 mt-1.5 max-h-64 list-none overflow-y-auto overscroll-contain rounded-xl border border-[var(--color-line)] bg-white p-1.5 shadow-2xl"
        >
          {options.map((o) => {
            const on = value.includes(o);
            return (
              <li key={o} role="option" aria-selected={on}>
                <button
                  type="button"
                  onClick={() => toggle(o)}
                  className={`flex w-full items-center gap-3 rounded-lg px-3 py-2 text-left text-sm transition hover:bg-orange/5 ${
                    on ? "font-semibold text-ink" : "text-body"
                  }`}
                >
                  <span
                    className={`grid h-4 w-4 shrink-0 place-items-center rounded border ${
                      on ? "border-orange bg-orange text-white" : "border-ink/25"
                    }`}
                  >
                    {on && <Check aria-hidden className="h-3 w-3" strokeWidth={3} />}
                  </span>
                  {o}
                </button>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
