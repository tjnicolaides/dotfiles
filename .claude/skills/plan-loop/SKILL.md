---
name: plan-loop
version: 1.0.0
description: Multi-lens parallel planning loop (fan out to N agents with different lenses, fan in to a single plan doc). Invoke when the user asks to "do a plan loop".
allowed-tools: "*"
---

# Plan Loop

**Arguments:** `N` iterations (default 2), `M` agents (default 3)

- fan out: spawn M parallel agents with different lenses, pick from:
  - grug-architect (simplicity, architecture)
  - code-critic (complexity, risks)
  - product-owner (user value, scope)
  - jared-biz-strategist (business, GTM)
  - game-designer (if game-related)
- fan in: synthesize findings, identify conflicts/consensus
- repeat for N iterations or early break when:
  - all agents converge on approach
  - no UNCONFIRMED items remain
  - implementation steps are concrete & sequenceable
- final output: single plan doc with dissenting notes if any
