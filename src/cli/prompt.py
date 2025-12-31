# """
# Prompt module for the Todo CLI application.

# Handles:
# - User input prompts
# - Output formatting
# - Error message display
# """
# from typing import Optional
# from src.config import STATUS_COMPLETED, STATUS_INCOMPLETE
# # Note: Task import removed as it's not used in this module


# def display_error(message: str) -> None:
#     """
#     Display an error message to the user.

#     Args:
#         message: The error message to display
#     """
#     print(f"\n❌ Error: {message}")


# def display_success(message: str) -> None:
#     """
#     Display a success message to the user.

#     Args:
#         message: The success message to display
#     """
#     print(f"\n✅ {message}")


# def display_info(message: str) -> None:
#     """
#     Display an informational message to the user.

#     Args:
#         message: The informational message to display
#     """
#     print(f"\n[INFO] {message}")


# def get_username_input() -> str:
#     """
#     Prompt the user for their username.

#     Returns:
#         The username entered by the user
#     """
#     return input("Enter username: ").strip()


# def get_password_input() -> str:
#     """
#     Prompt the user for their password.

#     Returns:
#         The password entered by the user
#     """
#     import getpass
#     return getpass.getpass("Enter password: ")


# def get_menu_choice() -> str:
#     """
#     Prompt the user for their menu choice.

#     Returns:
#         The user's menu choice
#     """
#     return input("\nEnter your choice: ").strip()


# def get_task_title() -> str:
#     """
#     Prompt the user for a task title.

#     Returns:
#         The task title entered by the user
#     """
#     return input("Enter task title: ").strip()


# def get_task_description() -> Optional[str]:
#     """
#     Prompt the user for a task description.

#     Returns:
#         The task description entered by the user, or None if empty
#     """
#     description = input("Enter task description (optional): ").strip()
#     return description if description else None


# def get_task_id() -> Optional[int]:
#     """
#     Prompt the user for a task ID.

#     Returns:
#         The task ID entered by the user, or None if invalid
#     """
#     while True:
#         try:
#             user_input = input("Enter task ID: ").strip()
#             if not user_input:
#                 display_error("Task ID cannot be empty.")
#                 return None
#             task_id = int(user_input)
#             if task_id <= 0:
#                 display_error("Task ID must be a positive number.")
#                 return None
#             return task_id
#         except ValueError:
#             display_error("Invalid input. Please enter a valid number for task ID.")
#             return None


# def confirm_action(prompt: str) -> bool:
#     """
#     Ask the user to confirm an action.

#     Args:
#         prompt: The confirmation prompt to display

#     Returns:
#         True if the user confirms, False otherwise
#     """
#     response = input(f"{prompt} (yes/no): ").strip().lower()
#     return response in ['yes', 'y', '1', 'true']


# def display_tasks(tasks: list) -> None:
#     """
#     Display a list of tasks to the user.

#     Args:
#         tasks: List of Task objects to display
#     """
#     if not tasks:
#         print("\n📋 No tasks found.")
#         return

#     print("\n📋 Your Tasks:")
#     print("-" * 50)
#     for task in tasks:
#         status = STATUS_COMPLETED if task.completed else STATUS_INCOMPLETE
#         print(f"[{task.id}] {task.title}")
#         if task.description:
#             print(f"    Description: {task.description}")
#         print(f"    Status: {status}")
#         print()
#     print("-" * 50)


# def display_menu() -> None:
#     """
#     Display the main menu to the user.
#     """
#     print("\n" + "="*40)
#     print("           TODO CLI APPLICATION")
#     print("="*40)
#     print("1. Add a task")
#     print("2. List all tasks")
#     print("3. Update a task")
#     print("4. Delete a task")
#     print("5. Mark task complete / incomplete")
#     print("6. Exit")
#     print("="*40)
#     print("You can also use natural language commands like:")
#     print("'add task', 'list tasks', 'exit', etc.")
#     print("="*40)






"""
Prompt module for the Todo CLI application.

Handles:
- User input prompts
- Output formatting
- Error / info / success messages
"""
from typing import Optional
from src.config import STATUS_COMPLETED, STATUS_INCOMPLETE


def display_error(message: str) -> None:
    print(f"\n❌ Error: {message}")


def display_success(message: str) -> None:
    print(f"\n✅ {message}")


def display_info(message: str) -> None:
    print(f"\n[INFO] {message}")


def get_username_input() -> str:
    return input("Enter username: ").strip()


def get_password_input() -> str:
    import getpass
    return getpass.getpass("Enter password: ")


def get_menu_choice() -> str:
    return input("\nEnter your choice: ").strip()


def get_task_title() -> str:
    return input("Enter task title: ").strip()


def get_task_description() -> Optional[str]:
    description = input("Enter task description (optional): ").strip()
    return description if description else None


def get_task_id() -> Optional[int]:
    while True:
        try:
            user_input = input("Enter task ID: ").strip()
            if not user_input:
                display_error("Task ID cannot be empty.")
                return None
            task_id = int(user_input)
            if task_id <= 0:
                display_error("Task ID must be a positive number.")
                return None
            return task_id
        except ValueError:
            display_error("Invalid input. Please enter a valid number for task ID.")
            return None


def confirm_action(prompt: str) -> bool:
    response = input(f"{prompt} (yes/no): ").strip().lower()
    return response in ['yes', 'y', '1', 'true']


def display_tasks(tasks: list) -> None:
    if not tasks:
        print("\n📋 No tasks found.")
        return

    print("\n📋 Your Tasks:")
    print("-" * 50)
    for task in tasks:
        status = STATUS_COMPLETED if task.completed else STATUS_INCOMPLETE
        print(f"[{task.id}] {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print(f"    Status: {status}")
        print()
    print("-" * 50)


def display_menu() -> None:
    print("\n" + "="*40)
    print("           TODO CLI APPLICATION")
    print("="*40)
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark task complete / incomplete")
    print("6. Exit")
    print("="*40)
    print("You can also use natural language commands like:")
    print("'add task', 'list tasks', 'exit', etc.")
    print("="*40)
