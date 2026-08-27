## [A4RE][resident-hosting] Belo User ID: use viewer.user.multifamilyProperties in ResidentHostingPropertiesPageQuery (2024-10-07)

For users with 64-bit user IDs, the properties list was failing. This was because ResidentHostingPropertiesPageQuery relied on `AirbnbUser.current().id` from Niobe - which is a string, but contains an incorrectly rounded integer value.

Our options here were to push a fix for Niobe to use `AirbnbUser.current().idStr`, or leverage a pre-existing User extension type called `User.multifamilyProperties` and allow the Viaduct resolver to correctly determine the user ID. I took the cowardly way.

---

## [A4RE][resident-hosting] Expand window for "Playwright jobs are not running on the default branch!" (2025-02-24)

These alerts fire every morning: [slack thread link]

In part because they are configured not to run during the staging restore window that takes place around 4AM-7AM Pacific ([sourcegraph link])

So this branch expands that window to 6 hours. Should reduce the amount of noise in #a4re-eng-alerts in Slack

---

## [A4RE][Property Tools] Decompose ReviewModal component (2025-03-21)

Ahead of some assorted Review Modal fixes, and introducing trebuchet logic - wanted to refactor ReviewModal to live as discrete modules in a standalone directory

---

## [A4RE][Property Tools] Various Property Settings visual changes (2025-03-12)

Tackled in tandem with @jhalaa-tejasvi

(Body was otherwise a numbered list of Asana ticket links — no other prose.)
