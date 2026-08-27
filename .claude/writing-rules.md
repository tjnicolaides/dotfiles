[Team writing standard loaded]

These rules apply to everything you write from here on, with no separate editing pass and
no reminder needed: PR titles and bodies, commit messages, code and config comments, docs,
Slack replies, and run reports. The full rule list is the `unslop` skill; this is the
generation-time subset, loaded once so it applies to every reply.

## Be concise — the rule that matters most

Default to the terse version. Fragments are fine. Sacrifice grammar for concision in
reports, tables, and status updates. Reviewer time is the scarcest resource on this team,
and padding spends it.

- Lead with the finding. First sentence carries the conclusion; evidence follows. No
  preamble, no restating the ask, no announced endings.
- Delete any sentence whose removal loses no information. Prefer the shorter phrasing
  whenever meaning survives.
- Give the terse version first, unprompted. Do not make the reader ask you to trim the same
  document twice.
- State facts, tables, and links without restating rationale already visible in the linked
  code or data. Add only explanation the reader cannot get from the artifact itself.
- Substantiate with links, not prose: code pointers, Slack threads, session links, queries,
  docs. Give a click-through instead of folding the detail into the text.
- Concrete nouns and numbers over qualifiers. "45 listings had an erroneous LANDLORD rule"
  beats "a significant number of listings were affected".
- State uncertainty as fact, not as hedge. "unconfirmed — did not verify against prod"
  beats "this may possibly be the case".

Concision applies to output, never to investigation. Be thorough in the work, terse in the
writing. Being brief is not permission to check less.

## No slop

- Do not write: crucial, delve, leverage, robust, seamless, comprehensive, holistic,
  utilize, streamline, pivotal, tapestry, landscape (abstract), testament, load-bearing,
  "prior to", "in order to", "it's worth noting", "importantly", "notably".
- No self-congratulatory framing ("this is the key insight"), no marketing adjectives for
  your own work, no summaries that repeat the body.
- Negative parallelism ("not X but Y", "not just X") is a tell. At most one per piece, and
  only when the contrast is the point.
- No rule-of-three flourishes. Use the actual count.
- Plain "is" over "serves as / stands as / represents".
- Sentence case headings. Straight quotes. No decorative emoji.
- Do not overcorrect into telegram style: every sentence keeps a subject and a main verb.

Comments: the default is no comment. Rename, extract, or restructure so the comment is
unnecessary. Only a comment explaining WHY (non-obvious business or regulatory rationale, a
workaround with a link, a deliberate tradeoff that reads as a mistake) earns its place.

Invoke the `unslop` skill for the full 31-pattern editing pass over a finished artifact, and
`/no-comments` to audit a diff's comments.
