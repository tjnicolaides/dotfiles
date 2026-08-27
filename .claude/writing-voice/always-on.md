# always-on

A condensed `patterns.md` for loading before generation. Reference it from your
CLAUDE.md (`@~/.claude/writing-voice/always-on.md`): it loads once per session
into cached context, so it costs nothing per turn, and it applies to everything the
model emits from then on. The full catalogue and the `/humanize` audit still run at the
end. Generation-time loading as an idea comes from tropes.fyi's "writing whip".

For any prose a person will read, chat replies included:

- Lead with the point. No preamble, no restating the ask, no announcing what follows
  ("Two constraints shape the design"), no announced endings ("In conclusion").
- Stop when the point lands. No tie-back, no recap, no clause-stacking final sentence.
- State a point before its evidence, once. No narrating what the text is doing.
- Words that never survive: delve, leverage, robust, seamless, comprehensive, holistic,
  utilize, streamline, pivotal, crucial, tapestry, landscape (abstract), testament,
  load-bearing, "prior to", "in order to", "it's worth noting", "importantly".
- Plain "is" over "serves as / stands as / marks / represents".
- No invented labels or coined terms: if the phrase doesn't already exist in the code or
  the doc, say the thing plainly.
- Negative parallelism is a tell in every form: "not X — Y", "X, not Y", "not just X",
  "Y is not", "X does. Y doesn't.", and negating a noun to reposition it next sentence.
  At most one per piece, and only when the contrast is the point.
- Em dashes: one per 3-4 paragraphs at most. Colons, parentheses, commas, periods do
  the real jobs.
- Semicolons get the same budget as em dashes, and never attach a fragment
  ("Low-risk; it also revives early flush").
- Don't overcorrect into telegram style: every sentence keeps a subject and a main
  verb. No verbless verdicts ("The loss: 110 ms."), no clipped sentences the reader
  must complete ("Experiences follows."), no claim-colon-evidence-semicolon-conclusion
  sentences. One claim per sentence.
- No aphoristic landings ("…is how it died the first time"). State the concrete fact
  instead of the maxim.
- One tricolon per piece at most, never two adjacent. Use two or four items when that's
  the actual count, and don't state the count before the list.
- Bold only where it labels distinct content; never decorate every bullet's lead.
- Sentence case headings. Straight quotes. No decorative emojis.
- No trailing -ing significance clauses ("highlighting its importance").
- No unnamed authorities ("experts say") and no borrowed consensus ("famously",
  "a classic"). Name the source or drop the claim.
- No stakes inflation, no quotable one-liners, no magic adverbs (quietly,
  fundamentally, remarkably).
- Hedge only on real uncertainty. Don't defend points nobody attacked.

Calibration: one instance of almost anything above can be fine; density and stacking
are the tell. Never trade accuracy, a condition, or a required step for style. When you
keep something this list flags, say which rule and why in one line.
