## [team][module] Fix user ID truncation in properties query (2024-10-07)

For users with 64-bit user IDs, the properties list was failing. This was because the query relied on a current-user helper that returned a string containing an incorrectly rounded integer value.

Our options here were to fix the upstream helper to expose the untruncated string form, or leverage a pre-existing extension type and let the resolver correctly determine the user ID. I took the cowardly way.

---

## [team][module] Expand window for "background jobs are not running on the default branch!" (2025-02-24)

These alerts fire every morning: [slack thread link]

In part because they are configured not to run during the staging restore window that takes place around 4AM-7AM Pacific ([sourcegraph link])

So this branch expands that window to 6 hours. Should reduce the amount of noise in the alerts channel.

---

## [team][module] Decompose ReviewModal component (2025-03-21)

Ahead of some assorted Review Modal fixes, and introducing new routing logic - wanted to refactor ReviewModal to live as discrete modules in a standalone directory

---

## [team][module] Various settings visual changes (2025-03-12)

Tackled in tandem with a teammate

(Body was otherwise a numbered list of ticket links — no other prose.)
