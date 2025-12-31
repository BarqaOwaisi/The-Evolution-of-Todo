# Todo CLI Application

A fully interactive, menu-driven command-line application that manages todo tasks entirely in memory.

## Features

- Interactive menu-driven interface
- User authentication with in-memory user store
- Add, view, update, delete, and mark tasks as complete/incomplete
- Support for both numeric and natural language commands
- Randomized session greetings

## Prerequisites

- Python 3.12 or higher

## Installation

1. Clone the repository
2. Navigate to the project directory

## Usage

Run the application:

```bash
python src/main.py
```

### Authentication

On startup, you will be prompted to enter your username and password. The application comes with two default users:

- Username: `admin`, Password: `password`
- Username: `user`, Password: `123456`

### Menu Options

After successful authentication, you will see a menu with the following options:

1. Add a task
2. List all tasks
3. Update a task
4. Delete a task
5. Mark task complete / incomplete
6. Exit

### Natural Language Commands

The application supports natural language commands:

- `add task`, `create`, `new` → Add a task
- `view`, `list`, `show` → List all tasks
- `update`, `edit`, `change` → Update a task
- `delete`, `remove` → Delete a task
- `complete`, `mark`, `done` → Mark task complete / incomplete
- `exit`, `quit` → Exit the application

## Example Workflow

1. Run `python src/main.py`
2. Enter username: `admin`
3. Enter password: `password`
4. Choose menu option 1 to add a task
5. Enter a task title and optional description
6. Use other menu options to manage your tasks
7. Exit when done

## Architecture

The application follows a clean architecture with clear separation of concerns:

- **Entry Layer**: `src/main.py` - Application bootstrap and control loop
- **CLI UI Layer**: `src/cli/` - User prompts and menu rendering
- **Authentication Layer**: `src/auth/` - User authentication
- **Business Logic Layer**: `src/tasks/service.py` - Task operations
- **Data Layer**: `src/tasks/models.py` and `src/tasks/repository.py` - Task models and storage

## Files Structure

```
src/
├── main.py                 # Application entry point
├── config.py               # Configuration constants
├── cli/
│   ├── __init__.py
│   ├── menu.py             # Menu rendering
│   ├── prompt.py           # User prompts and output formatting
│   └── greetings.py        # Session greetings
├── auth/
│   ├── __init__.py
│   └── authenticator.py    # Authentication logic
├── tasks/
│   ├── __init__.py
│   ├── models.py           # Task data model
│   ├── repository.py       # In-memory task storage
│   └── service.py          # Task business logic
└── utils/
    ├── __init__.py
    └── intent_parser.py    # Natural language intent resolution
```