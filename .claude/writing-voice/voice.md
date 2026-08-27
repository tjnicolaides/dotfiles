# TJ's writing voice

Derived from 4 samples (PR descriptions, Slack messages, a tech-design doc, a review-feedback
pattern guide) on 2026-08-26. Read by the `humanize` and `technical-writing` skills.
Correct anything wrong here — this file wins over the shipped pattern list.

Base: tj-review-voice

## Target voice

- Opens with the concrete problem or fact, not a topic sentence: "For users with 64-bit user IDs, the properties list was failing." Context and stakes follow, not precede.
- States the decision made and names the alternative not taken, often with a self-aware aside: "I took the cowardly way." Direct about trade-offs without over-explaining them.
- Uses "we" for team decisions and shared history, "I" for personal choices and feedback: "we've run into a couple of stumbling blocks," "I'm working on a skill."
- In long-form docs (tech designs), lays out each alternative as: what it is → how it would work, step by step → risks, as a bulleted list, often ending on the business/operational consequence ("could cause friction for our partners downstream").
- Asks real rhetorical questions when weighing a design trade-off, rather than asserting the answer outright: "does 'transparent' count as the dominant color?"
- Quotes a word in scare quotes when using it loosely or provisionally: "severs" the tie, "intelligent" enough, "content-aware".
- In Slack, keeps team announcements short and functional — one line of ask, one line of logistics — and signs off casually on personal notes ("Thanks!").

## Hard rules

- No hedging or softening direct feedback unnecessarily (from tj-review-voice base).
- No flowery language, excessive adjectives, or corporate buzzwords.
- No generic praise or generic statements that could apply to anyone/anything — ground claims in specifics.
- Use parentheses for inline clarifications, not em dashes, in prose (per tj-review-voice base) — Slack messages are the exception; they use em dashes freely for asides.
- Substantiate claims with links instead of folding detail into prose: Sourcegraph/GHE code pointers, Slack threads, agent session links, Superset/data queries, docs. Give the reader a click-through, don't restate what the link already shows.

## Words to cut

- "leverage" / "leveraging" as a verb outside of describing existing technical patterns (e.g. "leverage a pre-existing extension type" is fine as technical description, but avoid it as filler for "use")
- Corporate buzzwords generally (per tj-review-voice base)
- Generic hedge openers like "I think" or "just wanted to" before a direct statement

## Structure

- PR descriptions: minimal prose, often just a Summary paragraph (1-3 sentences) plus links (Asana, Slack thread, Sourcegraph). Reviewer and test-plan sections are terse or just a link/command, not narrative.
- Tech-design docs: heavy structure — headings per alternative, bulleted risk lists, bold for options being weighed. Each alternative gets: description, workflow steps (bulleted), risks (bulleted), ending on real-world/operational consequence.
- Slack: short paragraphs, no headings. Uses bold sparingly for the one thing that matters in an announcement (a headline word or the ask). Bullets appear when listing more than one link/item.

## Registers

| Type | Register | Structure |
| ---- | -------- | --------- |
| Design docs | Formal but plain; states risks directly, uses scare quotes for provisional terms, ends each alternative on a concrete consequence | Heading per alternative → prose description → bulleted workflow/risks |
| PR descriptions | Terse, functional; real prose only in the Summary, everything else is links or a one-line test note | Summary (1-3 sentences) + links; no narrative in reviewer/test sections |
| Slack messages | Casual, direct, warm in personal notes ("hope everyone's week has been going well"); functional and brief in team announcements | Short paragraphs, minimal headings, bullets for multi-link lists |
| Performance feedback | See tj-review-voice base — direct, warm, specific, no hedging | Project context → role → why it mattered → specific behaviors |
