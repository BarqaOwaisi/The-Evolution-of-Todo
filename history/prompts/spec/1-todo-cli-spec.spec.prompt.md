---
id: 1
title: Todo CLI Specification
stage: spec
date: 2025-12-31
surface: agent
model: Claude Sonnet 4.5
feature: todo-cli
branch: master
user: barqaowaisi
command: /sp.specify
labels: ["spec", "todo", "cli"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/todo-cli/spec.md
tests:
 - null
---

## Prompt

Specification: Phase I — In-Memory Interactive Todo CLI

Version: v1.0
Status: Approved for implementation
Constitution: /sp.constitution

Overview:
This specification defines the functional behavior, user interaction flow, and system boundaries for Phase I of the "Evolution of Todo" project. The system is a fully interactive, menu-driven command-line application that manages todo tasks entirely in memory and is implemented exclusively through AI-assisted, spec-driven development.

Target users:
- Beginners learning software architecture evolution
- Students acting as Product Architects
- Reviewers evaluating spec-to-code alignment

---

Authentication & Session Flow

Startup sequence:
1. Application launches in terminal.
2. System prompts:
   - User name (required)
   - Password (required)
3. Authentication:
   - Credentials are validated using an in-memory user store.
   - No persistence or encryption required.
4. On success:
   - User is greeted by name.
   - Greeting message is randomly selected from a predefined set to ensure variation per session.
5. On failure:
   - User is informed of invalid credentials.
   - Prompt repeats until valid input is provided.

---

Main Menu Behavior

Menu display:
- After successful login, the system displays a numbered menu:

  1. Add a new task
  2. View all tasks
  3. Update a task
  4. Delete a task
  5. Mark task complete / incomplete
  6. Exit

Input handling:
- System must accept:
  - Numeric input (e.g., `1`)
  - Natural language intent (e.g., "add task", "delete", "mark complete")
- Input matching is case-insensitive.
- Invalid input results in a friendly error message and menu redisplay.

---

Task Model

Task attributes:
- id: auto-incremented integer (unique per session)
- title: string (required, non-empty)
- description: string (optional)
- completed: boolean (default: false)

Storage:
- All tasks are stored in memory only.
- Data resets when the application exits.

---

Feature Specifications

1. Add Task
- Triggered by menu option 1 or equivalent intent.
- System prompts for:
  - Title (required)
  - Description (optional)
- On success:
  - Task is added to memory.
  - Confirmation message is displayed with task ID.

2. View Tasks
- Triggered by menu option 2.
- Displays:
  - Task ID
  - Title
  - Completion status
- Status indicators:
  - Completed → ✔ or [Done]
  - Incomplete → ✖ or [Pending]
- If no tasks exist:
  - System displays a clear "No tasks found" message.

3. Update Task
- Triggered by menu option 3.
- System prompts for task ID.
- If ID exists:
  - User may update title, description, or both.
- If ID does not exist:
  - System displays an error and returns to menu.

4. Delete Task
- Triggered by menu option 4.
- System prompts for task ID.
- Before deletion:
  - System asks for confirmation (yes/no).
- On confirmation:
  - Task is removed from memory.
- On cancellation:
  - No changes are made.

5. Mark Complete / Incomplete
- Triggered by menu option 5.
- System prompts for task ID.
- Behavior:
  - If task is incomplete → mark complete.
  - If task is complete → mark incomplete.
- Confirmation message reflects new status.

6. Exit
- Triggered by:
  - Menu option 6
  - Typing `exit` or `quit`
- System displays a friendly goodbye message including user name.
- Application terminates cleanly.

---

Error Handling Rules

- Application must never crash due to invalid input.
- All errors must:
  - Be human-readable
  - Explain what went wrong
  - Suggest the next valid action
- After any error, system returns to main menu.

---

Non-Functional Constraints

- No argument-based CLI flags.
- No file or database persistence.
- No networking or external APIs.
- No manual code writing.
- Code must follow clean separation:
  - UI / interaction layer
  - Business logic
  - Data models

---

Acceptance Criteria

- User can complete all five core operations successfully.
- Menu-driven flow is intuitive without instructions.
- Natural language and numeric inputs both work.
- Session greeting varies between runs.
- All behaviors trace directly to this specification.
- Implementation fully complies with /sp.constitution.

---

End of Specification

## Response snapshot

Specification for Phase I In-Memory Interactive Todo CLI has been created and documented. This specification covers all necessary aspects including authentication flow, main menu behavior, task model, feature specifications, error handling rules, non-functional constraints, and acceptance criteria.

## Outcome

- ✅ Impact: Created complete specification for the Todo CLI application
- 🧪 Tests: Not applicable at spec stage
- 📁 Files: Created spec file at specs/todo-cli/spec.md
- 🔁 Next prompts: Implementation planning and development
- 🧠 Reflection: The specification is comprehensive and ready for implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin implementation planning