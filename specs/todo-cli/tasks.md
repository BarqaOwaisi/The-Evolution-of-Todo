# Tasks: Phase I — In-Memory Interactive Todo CLI

Version: v1.0
Status: Ready for implementation
Constitution: /sp.constitution
Specification: /sp.specify
Plan: /sp.plan

## Objective
Decompose the approved plan into small, atomic, verifiable tasks that can be executed sequentially by Claude Code to generate a fully functional interactive Todo CLI application.

---

## Phase 0 — Project Initialization

### T0.1 Create project structure
- Generate `/src` directory and subpackages as defined in /sp.plan
- Add `__init__.py` files where required
- Create placeholder modules with no logic

### T0.2 Define configuration constants
- Create `config.py`
- Define:
  - Menu option mappings
  - Exit keywords
  - Status indicators
  - Authentication retry limits (if any)

---

## Phase 1 — Data Models & Repositories

### T1.1 Implement Task model
- Create Task data structure
- Fields: id, title, description, completed
- Ensure defaults and readability

### T1.2 Implement in-memory Task repository
- Store tasks in a list or dictionary
- Provide methods:
  - add_task
  - get_all_tasks
  - get_task_by_id
  - update_task
  - delete_task
  - toggle_task_status

---

## Phase 2 — Authentication System

### T2.1 Define in-memory user store
- Create a simple user model
- Hardcode at least one valid user
- Store credentials in memory only

### T2.2 Implement authenticator
- Prompt for user name and password
- Validate credentials
- Loop until valid input is provided
- Return authenticated user object

---

## Phase 3 — CLI Interaction Components

### T3.1 Implement greetings module
- Define a list of greeting templates
- Randomly select greeting per session
- Support user name interpolation

### T3.2 Implement prompt utilities
- Centralize all user-facing text
- Ensure clarity and friendly tone
- Standardize error messages

### T3.3 Implement menu rendering
- Display numbered menu options
- Ensure consistent formatting
- Redisplay menu after each action

---

## Phase 4 — Intent Parsing

### T4.1 Implement input normalization
- Trim whitespace
- Convert to lowercase
- Safely handle empty input

### T4.2 Implement intent parser
- Map numeric inputs to actions
- Map keyword-based inputs to actions
- Handle exit intents explicitly
- Return structured intent result

---

## Phase 5 — Task Service Layer

### T5.1 Implement add task flow
- Prompt for title and description
- Validate title presence
- Call repository add method
- Display confirmation

### T5.2 Implement view tasks flow
- Retrieve all tasks
- Format output with status indicators
- Handle empty task list

### T5.3 Implement update task flow
- Prompt for task ID
- Validate existence
- Prompt for new values
- Apply updates

### T5.4 Implement delete task flow
- Prompt for task ID
- Confirm deletion
- Remove task from repository

### T5.5 Implement toggle completion flow
- Prompt for task ID
- Toggle completed state
- Display updated status

---

## Phase 6 — Application Control Loop

### T6.1 Implement main event loop
- Display menu
- Capture user input
- Resolve intent
- Dispatch to appropriate service
- Loop until exit intent

### T6.2 Implement exit flow
- Display personalized goodbye message
- Terminate application cleanly

---

## Phase 7 — Error Handling & Validation

### T7.1 Input validation
- Guard against invalid task IDs
- Handle non-numeric ID input
- Prevent crashes from bad input

### T7.2 Friendly error recovery
- Display helpful error messages
- Always return to menu after error

---

## Phase 8 — Integration & Final Assembly

### T8.1 Wire modules in main.py
- Initialize repositories
- Run authentication flow
- Start main event loop

### T8.2 Smoke test interactive flows
- Login
- Add, view, update, delete tasks
- Toggle completion
- Exit cleanly

---

## Acceptance Checklist

- All tasks executable by Claude Code without manual edits
- All five core features fully functional
- Menu-based interaction only
- Natural language and numeric inputs supported
- In-memory state only
- Fully compliant with constitution and specification

---

## End of Tasks