# Asana Integration

## Common Claude Tasks

- When asked to show tasks, list them with their project context
- When asked to create tasks, assign them to me by default. But don't do so when creating sub-tasks.
- By default do not set due dates for tasks nor sub-tasks
- Include task permalink URLs when referring to specific tasks
  - Format permalinks as: <https://app.asana.com/1/{workspace_id}/project/{project_id}/task/{task_id}>
  - NEVER use the incorrect format: <https://app.asana.com/1/{project_id}/{task_id}>
- When asked to mark tasks complete or incomplete, use the complete-task/uncomplete-task commands
- Only work with the starred projects listed below unless explicitly requested
- When creating new tasks, default to the primary project configured in Workspace Information below
- Interpret references to "my pod" as the primary project
- Always include the following in italics at the bottom of task descriptions (when creating or modifying a task) using HTML rich text: <em>🤖 Co-created with Claude via Claude Code</em> or <em>🤖 Co-created with Claude and [Other Model Names] via Claude Code</em> when other models were used
- IMPORTANT: For comments, use plain text only as HTML formatting is NOT supported in Asana comments via API. Simply append this text without HTML tags: "🤖 Co-created with Claude via Claude Code"
- If I provide a task ID or name, find the task (check project TJ Pod first), display its summary
- If the task is in project TJ Pod and is not a sub-task, set its "Target Sprint" to the current sprint (by date) and "Status" to "In Progress" if not already set
- When we finish working on a task or switch to another, change its status to "Planned" unless I specify a different status
- ALWAYS ask for confirmation before marking an asana task or subtask complete.
- When asked to "backdate an asana task for ...", create a task that describes the work in present tense, as if it hasn't been done yet, even though the work has already been completed. If "..." refers to a git branch, add the branch as a comment to the task after creating it; likewise if it refers to a PR.

## Git and Asana Integration

- If unsure which Asana task is being referenced, check the git branch
- The branch should start with `tj-nicolaides--` (that's my name)
- Comment in Asana task only when I ask you to or when a new branch is pushed to origin

## Asana API Usage

  Use the MCP Asana server to interact with the Asana API directly through Claude Code.

### Key Guidelines

- For searching, use `assignee.any` NOT `assignee_any` (similarly for `project.any` not `project_any`)
- Main operations: list workspaces, search projects/tasks, create/update tasks and subtasks
- Manage task relationships with dependencies and stories
- Task operations always require the appropriate task ID (gid)
  
  All task descriptions should follow this format:

  ```html
  <strong>Background</strong>
  Context here with proper formatting.

  <strong>Acceptance Criteria</strong>
  - Criteria 1
  - Criteria 2

  <em>🤖 Co-created with Claude via Claude Code</em>
  ```

  Remember to include appropriate attribution as specified in the General Settings.

## Workspace Information

- Workspace ID: YOUR_WORKSPACE_ID
- User ID: YOUR_USER_ID

## Starred Projects (Primary)

- Configure your starred projects here with their IDs
