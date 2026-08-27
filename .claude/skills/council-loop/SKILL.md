---
name: council-loop
version: 1.0.0
description: Parallel review-council loop across product/coder/architect/critic lenses, synthesized into one review doc. Invoke when the user asks to "do a council loop".
allowed-tools: "*"
---

# Council Loop (Review Council)

- fan out: spawn agents in parallel, each with a review lens:
  - product-owner (completeness, user value alignment)
  - super-coder (correctness, implementation quality)
  - grug-architect (clarity, simplicity, maintainability)
  - code-critic (risks, edge cases, test coverage)
- fan in: synthesize findings into:
  - consensus items (all agree)
  - concerns (with severity: blocker/major/minor)
  - recommendations (prioritized)
- output: single review doc, dissenting notes preserved
