/**
 * The document block format shared by the blog and the legal pages.
 *
 * Long-form text on this site is stored as data, not MDX or HTML strings:
 * one renderer (components/blog/Prose.tsx) styles every document, and headings
 * get stable ids so any page can build a table of contents from its own body.
 */

export type Block =
  | { t: "p"; text: string }
  | { t: "h2"; text: string }
  | { t: "h3"; text: string }
  | { t: "ul"; items: string[] }
  | { t: "ol"; items: string[] }
  | { t: "quote"; text: string }
  | { t: "callout"; title: string; text: string };

/** Slug for a heading, so a contents list can link into the body. */
export const headingId = (text: string) =>
  text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

/** The h2s of a document, in order. */
export const tocOf = (blocks: Block[]) =>
  blocks
    .filter((b): b is Extract<Block, { t: "h2" }> => b.t === "h2")
    .map((b) => ({ id: headingId(b.text), text: b.text }));

/** Words we actually render — used for reading time. */
export const wordCount = (blocks: Block[]) =>
  blocks.reduce((n, b) => {
    const text = "text" in b ? b.text : "items" in b ? b.items.join(" ") : "";
    const title = "title" in b ? b.title : "";
    const s = `${title} ${text}`.trim();
    return n + (s ? s.split(/\s+/).length : 0);
  }, 0);
