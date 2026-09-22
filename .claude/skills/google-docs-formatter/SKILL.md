---
name: google-docs-formatter
description: Fix or apply native Google Docs formatting (headings, lists, tables, hyperlinks) through the Extended Google Drive MCP. Use when a Doc shows literal markdown ("[text](url)", "| a | b |"), blank rows between every block, or headings and paragraphs rendered as bullets, or when rebuilding a tab from markdown. Content-only; never runs a theme pass on docs TJ styled.
---

# Google Docs formatter

Google Docs does not render markdown. `gdrive_edit_doc appendText format=markdown`
converts headings, bullets, numbered lists, bold, italic and strikethrough, and nothing
else: links stay literal `[text](url)`, tables stay literal `| a | b |`, backticks are
stripped, nested bullets flatten. Everything appended inherits the paragraph style of the
paragraph it lands in. Those two facts explain every broken doc this skill fixes.

Adapted from a pasted skill written for a different MCP (`mcp__gdrive__getGoogleDocContent`,
`formatGoogleDocParagraph`, `formatGoogleDocText`). Those tools are not connected in this
setup. The index-based approach still applies; the tools below are what exist here.

## Tools (Extended Google Drive MCP)

| Need | Tool |
|---|---|
| Tab ids | `gdrive_read_file listTabsOnly=true` |
| Headings + tables with indices | `gdrive_doc_get_structure` (tabId to scope) |
| Read a tab | `gdrive_read_file format=markdown tabId=...` (real links and literal links look the same) |
| Full-fidelity check | `gdrive_read_file format=html` (whole doc, all tabs; count `<a href` vs `](http`) |
| Append / replace / delete | `gdrive_edit_doc` (appendText, replaceAllText, deleteText, deleteRange) |
| Hyperlinks, headings, bold, lists by text match | `gdrive_format_doc` |
| Real table | `gdrive_doc_insert_table` with `data` and `location.endOfSegment` |

All edit tools take `tabId` at call level. Omit it and you edit the first tab.

## Diagnose first

Export html once, strip styles, count: empty `<p></p>` and `<li></li>`, `](http`
(literal links), `<li><h2>` (headings inside lists), `<table` vs `| --- |` (literal
tables). The counts tell you which recipe below applies. Re-run the same counts after.

## Recipe 1: literal links to hyperlinks (no other damage)

Three passes per tab, every step 2 call finished before any step 3 call:

1. `replaceAllText` each `[text](url)` with a unique token (`LNKA0001`, ...). Regex must
   allow brackets in text and parentheses in URLs (Jira JQL links have them).
2. `gdrive_format_doc type=link text=<token> url=<url> allOccurrences=true`.
3. `replaceAllText` token to text. Link formatting carries over. Batch about 40 ops a call.

## Recipe 2: rebuild a tab (blank rows, bulleted headings, literal tables)

Deleting blank paragraphs one by one is not possible with text-match tools, so rebuild
the tab. Docs version history keeps the old state.

1. Get the tab's markdown. Prefer converting the html export yourself so bold,
   strikethrough and real links survive (`gdrive_read_file format=markdown` drops none of
   these, but the html is the only way to tell a real link from a literal one).
2. Tokenise links in the markdown before appending (Recipe 1 step 1 done locally).
   Remove all blank lines between blocks. A heading directly after a list item is fine;
   a blank line becomes an empty paragraph.
3. Learn the tab end index: call `deleteRange startIndex=1 endIndex=9999999`. The error
   says `must be less than the end index of the referenced segment, N`.
4. `deleteRange startIndex=1 endIndex=N-1`. One empty paragraph survives.
5. **Check that surviving paragraph is not a bullet.** Everything you append inherits its
   style, and no tool here removes bullets (`heading level 0`, `bulletList`,
   `numberedList` all leave or re-add them). If the old tab ended in an empty bullet, the
   only fix is a human click: put the cursor on that empty last line and toggle bullets
   off (Cmd+Shift+8). Then continue. This is also why a daily routine that appends into a
   tab whose last line is a bullet produces a fully bulleted doc.
6. Append in chunks: markdown up to a table (no trailing newline), then
   `gdrive_doc_insert_table rows cols data location={tabId, endOfSegment:true}`, then the
   rest. Each markdown chunk should end with `\n` except the one right before a table.
   The converter still leaves one empty paragraph before an inserted table; remove it by
   deleting the newline of the paragraph before it (`deleteRange [table.startIndex-2,
   table.startIndex-1)`), which merges the two and keeps the first paragraph's style.
7. Recipe 1 steps 2 and 3 for the tokens.
8. Verify: html counts (Diagnose) and a plain-text diff of before vs after per tab.

Merged paragraphs keep the style of the first paragraph. The final paragraph of a tab
cannot be deleted, so one trailing empty paragraph per tab is expected.

## Preflight and postflight (mandatory for any routine that writes a tab)

Preflight: html export, strip styles, confirm the target tab's last paragraph is `<p></p>`.
A trailing `<li></li>` means stop and get the human click before writing. Postflight: same
export, expect zero `](http`, zero `<li><h`, zero `LNK` tokens, and no empty paragraph other
than the mandatory trailing one per tab. A routine that skips these produces the fully
bulleted, blank-row, literal-link doc this skill exists to fix.

## Smart chips (people, files, dates, dropdowns)

The Docs API cannot create smart chips, and neither can any tool here. Reads are lossy:
a person chip exports as `<a href="mailto:...">Name</a>` (markdown: `[Name](mailto:...)`),
a file chip as a plain link, date and dropdown chips as plain text. Consequences:

- Never run Recipe 2 (rebuild) on a tab that has chips; they come back as mailto links
  and plain text. Use replaceAllText and gdrive_format_doc on that tab instead.
- replaceAllText does not match chip text. To change a chip, ask the human.
- To keep chips in a generated doc, put them in a hand-made block the routine never
  clears (for example a roster table with person chips at the top of the tab) and have the
  routine delete only from that table's endIndex to the tab end.
- Reference docs that use chips well: A4RE Tech Spec Template
  `1KZNHPvDhja5mt2CjCKIj9S8WceEv8ikvvo08ILI_PbQ` (owner lines, reviewer table with
  person and status chips, file chips in a related-designs table), Flex Night Limits PRD
  `1vd0TyX4ucqE5rARJL1coCgt_n59ZY6K4b2Pks_sedCQ` (header line PM | Eng | Status | Last
  updated, RACI table, one tab per requirement surface).

## Rules

- Never `gdrive_doc_apply_theme` or `applyTheme: true` on docs TJ styled by hand
  (IC checklist `1eY1HnnzhBjQ__frkA7bK3yaB7JUc0ASvrQsL5euvHhw`, prioritization tracker
  `1pnWYYUVe2EYhBHrlSst3-mlJB2R0Wsf91JI1dWx2_Hk`). Content only.
- Tables through `gdrive_doc_insert_table` only. Markdown tables never convert on append.
- Heading ids change on rebuild; deep links with `#heading=` break. Say so.
- Multi-tab docs: `gdrive_update_file_content` replaces the whole file and loses tabs.
- Keep markdown payloads out of chat: write them to the scratchpad and pass the file text
  into the tool call.

## Worked example

2026-09-22: IC checklist and TJ prioritization tracker. Before: 123 empty paragraphs,
151 literal links, 16 headings inside `<li>`, one table as literal pipes. After Recipe 2 on
six tabs: 0 literal links, 245 real links, only the mandatory trailing paragraph per tab,
text identical per tab. The IC Current tab needed the human click in step 5.
