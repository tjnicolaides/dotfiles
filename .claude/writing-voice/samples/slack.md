## Team announcement — event reminder (2026-06-25)

A4RE Eng Show & Tell today @here! Climb aboard here: [Signup link] (and while you're at it, don't forget to sign up for [Hotels Eng Demos], too)

---

## Team announcement — sprint planning reminder (2026-05-12)

Reminder to @here about [Sprint planning] today - 2PM Eastern, 11AM Pacific. Please take a moment to update your tickets with the right statuses, and prep any new tickets for assignment in this upcoming 2-week sprint. (Last week's planning for a 1-week sprint was part of a quick schedule correction after Real Estate Gather had landed on our original 4/28 date.)

Questions or concerns about prioritization? We're happy to answer questions in the thread below, or feel free to check in with your EM privately.

---

## Sick day notice (2026-05-29)

Hey folks, hope everyone's week has been going well. Our trip was great, but unfortunately a few people are under the weather here.

I'm gonna take a sick day for them, but still attending a few alignment meetings I don't want to move. Available on Slack with slower responses. Thanks!

---

## Tech-design process update, thread (2026-06-09 to 2026-06-12)

In eng workshop today, I'm presenting a spec for the Viaduct read path to serve the marketplace changes we're making for #a4re-fee-transparency. This document was co-authored and reviewed by multiple Claude agents - steered by decisions Ryder and I made offline, and informed by the same PRD, backend tech spec, and design prototypes we're using. Should be an interesting review - hope you'll join us.

[Slate doc link]

Reply 1:
for those following along at home, we've run into a couple of stumbling blocks where the generated spec was not as thorough or considered as we'd usually expect. Instead of amending the main spec, I'm writing companion docs to call out where there were gaps, and what the improved decisions looked like.

- re: the best way of exposing Total Monthly Prices in the Browse page property card list: [link]
- addressing a naive `UdsBackedNode` design for exposing Ozols Fees on the graph: [link]

Reply 2:
At the end, maybe we'll find a way to synthesize the shortcomings into some kind of plugin / skill / subagent that will be more capable next time.

---

## Tool announcement, thread (2026-06-17)

For anyone following along, I've prompted `airchat` to evaluate the gaps and rough patches in the Fee Transparency Viaduct/frontend spec, capturing changes / feedback in companion docs as we went. [This has been synthesized here], and I'm working on a skill for airbnb/ergo to help us generate better technical designs going forward.

Reply (after a correction about channel name):
:github-octocat: [ergo PR link]
> *One-time setup*
> /plugin add airbnb-ergo/a4re    # adds (or updates) the a4re plugin
> Prereq: a Treehouse checkout at ~/repos/treehouse (or set $TREEHOUSE) — the skill reads the multifamily tenant guides + service context from there.
>
> *Using it* — invoke in a Claude Code session by intent or by name:
> /a4re-tech-design <PRD link | tech-spec link | file path | one-line idea>
> Triggers also fire on natural phrasing: "a4re tech design", "write an a4re spec", "multifamily tech design", etc.
>
> *What it does* (7 steps, with you in the loop):
> 1. Loads A4RE context (oncall-flow service map + tenant guides)
> 2. Proposes research areas → *waits for your approval*
> 3. Fans out parallel research, forcing each area through checklist A–E
> 4. Drafts the spec (A4RE template + spec-writing-guidelines)
> 5. Self-enforces checklist A–E
> 6. Runs the design-time review council
> 7. *Checkpoint for your sign-off* → publishes a cross-linked Slate doc
>
> *The mental model:* it's the productized version of that copy-paste kickoff prompt in the Slate doc. Instead of pasting the constellation + checklist by hand, the skill injects them and runs the research-first flow for you. Net: the half-sprint of investigate-and-synthesize collapses into a guided session that lands a gap-anticipating first draft — which A4RE owners then review.
>
> Two practical notes:
> - It's *interactive* (approval gates at steps 2 and 7) — not fire-and-forget.
> - It leans on the Treehouse /docs:tech-design engine when present, and falls back to running the phases itself if not.
