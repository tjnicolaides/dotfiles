---
name: verify-loop
version: 1.0.0
description: Implement-then-adversarially-verify loop against a source of truth (spec, prototype, punch list), iterating fixes until all items verify clean. Invoke when the user asks to "do a verify loop".
allowed-tools: "*"
---

# Verify Loop

**Arguments:** `N` iterations (default 2). Requires at least one source of truth (prototype URL, spec doc, Slate punch list, Figma, etc.)

- phase 1 (implement): spawn super-coder agent to do the work
- phase 2 (verify): spawn adversarial verifier agent that:
  - reads the punch list / spec / acceptance criteria
  - reads the actual code diff (not commit messages)
  - runs validation (types, lint, tests)
  - pass 1: logic-only (code review against spec, trace math, check enum values)
  - pass 2+: visual (Playwright screenshots of prototype vs implementation, element-by-element)
  - cross-references spec in the available doc tool (Slate / Google Docs / local markdown)
  - produces per-item verdicts: VERIFIED / PARTIAL / INCORRECT / REGRESSION / CANNOT-VERIFY
  - for non-VERIFIED: states what's wrong + minimal fix
- phase 3 (fix): feed non-VERIFIED items back to implementer agent, who fixes and commits
- phase 4 (re-verify): verifier runs again on the fixes only (not full re-review)
- repeat phases 3-4 for N iterations or early break when:
  - all items VERIFIED or explicitly deferred with justification
  - no regressions introduced by fixes
  - validation commands pass clean
- final output:
  - updated punch list doc (checkmarks on verified, status on deferred)
  - remaining work section with blockers and follow-ups
  - ship/no-ship recommendation
- key principles:
  - verifier is ADVERSARIAL — assumes implementer is wrong until proven otherwise
  - verifier never trusts commit messages; reads actual code
  - verifier checks for deleted test assertions, stubbed mocks, suppressed lint
  - escalate to visual only when logic pass is clean (saves tokens)
  - prototype comparison uses Playwright side-by-side, not memory of what it looked like
