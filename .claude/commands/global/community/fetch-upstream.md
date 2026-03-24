---
description: Fetch upstream, rebase, test and push
author: Adam Bloomston (@adam-bloomston)
---

<task>
Fetch upstream changes, rebase current branch, run tests and linting, then push changes to maintain branch currency with the main branch.
</task>

<context>
This command automates the common workflow of keeping a feature branch up-to-date with the main branch while ensuring code quality through testing and linting.
</context>

<instructions>
Follow these steps in order:

1. **Fetch Changes**
   - Use Bash tool: `git fetch origin`
   - Check if there are new commits on the main branch

2. **Check for Updates**
   - Use Bash tool: `git log HEAD..origin/main --oneline`
   - If no changes, inform user and exit
   - If changes exist, proceed with rebase

3. **Rebase Current Branch**
   - Use Bash tool: `git rebase origin/main`
   - Handle any merge conflicts if they occur
   - Abort if conflicts cannot be resolved automatically

4. **Run Tests**
   - Detect project type and run appropriate tests
   - Use Bash tool: Check for package.json, requirements.txt, etc.
   - Run tests using project-native commands (npm test, pytest, etc.)
   - Stop if tests fail

5. **Lint Code**
   - Run project linting tools
   - Use Bash tool: Run linter (eslint, ruff, etc.)
   - If linting fixes files, commit those fixes with message "Fix linting issues"

6. **Push Changes**
   - Use Bash tool: `git push --force-with-lease origin HEAD`
   - Confirm successful push
</instructions>

<error_handling>
- If rebase conflicts occur, provide clear guidance on resolution
- If tests fail, show output and stop the process
- If push fails, check for force-push safety and retry if appropriate
</error_handling>

<output_format>
Report the status of each step:
- ✅ Fetched changes from origin
- ✅ Rebased successfully (X commits ahead)
- ✅ Tests passed
- ✅ Linting completed (fixed Y files)
- ✅ Pushed changes to origin
</output_format>
