---
description: Analyze conversation logs for CLAUDE.md improvements (requires devai-gateway MCP server)
author: Adam Bloomston (@adam-bloomston)
---


<task>
Analyze recent Claude Code conversation logs to identify common issues, patterns, and tips that should be documented in the user-level CLAUDE.md file to eliminate repetitive user explanations.
</task>

<context>
This command helps improve user experience by identifying repetitive patterns in conversation logs that could be prevented with better context documentation in CLAUDE.md files.
</context>

<instructions>
Follow these steps EXACTLY and IN ORDER:

1. **List Available Models**
   - Use mcp__devai-gateway__listModels to ensure proper MCP tool context

2. **Find Recent JSONL Log Files**
   - Use Bash tool to find Claude Code conversation logs from past 10 days with 100+ lines
   - Automatically select 9 at random if more than 9 found
   - Command: `find $HOME/.claude/projects -name "*.jsonl" -mtime -10 -exec wc -l {} + | awk '$1 >= 100 {print $2}' | grep -v total | { files=$(cat); count=$(echo "$files" | wc -l); if [ "$count" -ge 9 ]; then echo "$files" | shuf -n 9; else echo "$files"; fi; }`

3. **Analyze Logs with Batch Processing**
   - Use mcp__devai-gateway__batchProcess with specific parameters</instructions>

4. **Generate Final Recommendations**
   - Review results along with current ~/.claude/CLAUDE.md file
   - Make concrete recommendations for context improvements
</instructions>

<mcp_usage>
Use mcp__devai-gateway__batchProcess with parameters:
- aggregatedMaxTokensThreshold: 75000
- requests: Array with one request per JSONL file, each containing:
  - type: "completion"
  - model: Use "gpt-4.1" for first 3 files, "gpt-4.1-mini" for next 3, "gpt-4.1-nano" for last 3
  - filepaths: Single JSONL file path per request
  - content: Analysis prompt below

Analysis prompt:
"Analyze this Claude Code conversation log to identify repetitive user actions and workflow inefficiencies that could be prevented with better context.

**CRITICAL: JSONL Message Parsing**
- Each line is a JSON object with a `type` field
- ONLY analyze lines where `type` == `\"user\"`
- Extract user content from: `message.role == \"user\"` and `message.content`
- IGNORE lines where `type` == `\"assistant\"` or `type` == `\"system\"`
- DO NOT confuse assistant messages with user messages

Focus on USER messages to find patterns where the user has to:
- Repeatedly explain the same preferences or requirements
- Give the same instructions multiple times across conversations
- Correct Claude's assumptions about their workflow or environment
- Provide the same context about their codebase, tools, or processes
- Re-specify testing commands, build processes, or deployment steps
- Repeatedly clarify their coding standards or conventions

TASK: For each repetitive pattern you find, provide:
1. **User Pain Point**: What the user keeps having to repeat or explain
2. **Frequency**: How often this appears in the conversation
3. **Evidence**: Quote 1-2 actual user messages that demonstrate this pattern
4. **Context Solution**: The exact markdown section that would eliminate this repetition
5. **Impact**: How much time/frustration this would save the user

Focus on actionable context that would make Claude immediately more helpful without requiring user explanation."
</mcp_usage>

<deliverables>
For each recommendation, provide:
1. **Repetitive Pattern**: What users keep having to explain/specify across conversations
2. **Evidence**: Quote 2-3 actual user messages from the logs that demonstrate this pattern (REQUIRED - no evidence = no recommendation)
3. **Current Gap**: What's missing or insufficient in the current CLAUDE.md
4. **Ready-to-Copy Markdown**: Complete section with proper headers that can be directly added
5. **Expected Impact**: How much repetition this would eliminate

**IMPORTANT**: Before making final recommendations, show the evidence to the user and confirm the pattern is valid. Do not make recommendations based on assumed or inferred patterns without concrete user message quotes.

Focus on the most impactful additions that would give Claude the right defaults and assumptions from the start.
</deliverables>
