---
description: Analyze logs to identify slash command opportunities (requires devai-gateway MCP server)
author: Adam Bloomston (@adam-bloomston)
---

Your goal is to analyze recent Claude Code conversation logs to identify common patterns that could be automated as custom slash commands. Follow the steps below EXACTLY and IN ORDER:

1. **List models available**
   We do this to ensure you have proper context for MCP tools available for use below.

2. **Find recent JSONL log files**
   Find all Claude Code conversation logs that were created or modified in the past month with at least 100 lines, automatically selecting 9 at random if more than 9 are found, by running this command:

   ```
   find $HOME/.claude/projects -name "*.jsonl" -mtime -30 -exec wc -l {} + | awk '$1 >= 100 {print $2}' | grep -v total | { files=$(cat); count=$(echo "$files" | wc -l); if [ "$count" -ge 9 ]; then echo "$files" | shuf -n 9; else echo "$files"; fi; }
   ```

3. **Analyze logs with batchProcess tool**
   Call the `batchProcess` tool with these parameters:

   - **aggregatedMaxTokensThreshold**: 75000
   - **requests**: Array with one request per JSONL file from step 2, each containing:
     - **type**: "completion"
     - **model**: Use "gpt-4.1" for the first 3 files, "gpt-4.1-mini" for the next 3 files, and "gpt-4.1-nano" for the last 3 files
     - **filepaths**: Array containing exactly two elements: the single JSONL file path and !`echo ~/.claude/commands/**/zzz-reference-claude-commands-guide.md`
     - **content**:
       ```
       Analyze this Claude Code conversation log to identify repetitive user workflows that could be automated as custom slash commands. Focus on USER messages to find patterns where the user repeatedly:

       - Gives the same multi-step instructions across conversations
       - Asks for similar code analysis, review, or generation tasks
       - Follows consistent workflows for testing, building, or deployment
       - Requests similar project management or documentation tasks
       - Uses similar prompts for AI model polling or analysis

       CONTEXT: Claude Code slash commands are shortcuts that allow users to define frequently-used prompts as reusable commands. For detailed guidance, reference the comprehensive guide provided below `zzz-reference-claude-commands-guide.md`.

       TASK: For each repetitive pattern you find, provide:

       1. **Pattern Description**: What workflow or task the user repeats
       2. **Frequency**: How often this appears in the conversation
       3. **Command Name**: Suggested slash command name (e.g., /user:task-name)
       4. **Automation Potential**: How much time this would save if automated
       5. **Command Content**: The exact markdown content for the slash command

       Focus on patterns that appear multiple times and involve consistent multi-step workflows that would provide significant time savings if automated.
       ```

4. **Review results and create command recommendations**
   After analyzing all the logs, read !`echo ~/.claude/commands/**/zzz-reference-claude-commands-guide.md` for context on Claude Commands, then review existing commands in `~/.claude/commands/` to de-duplicate and suggest ones to use (rather than suggesting new ones). For each recommendation, provide:

   1. **Pattern Identified**: What repetitive workflow was found
   2. **Command Name**: The suggested slash command name
   3. **Ready-to-Use Markdown**: Complete command file content that can be saved directly
   4. **Expected Impact**: How much repetitive work this would eliminate
   5. **Location**: Whether it should be personal (`~/.claude/commands/`) or project-specific (`.claude/commands/`)

   Focus on the most impactful automations that would eliminate the most repetitive typing and workflow steps.
