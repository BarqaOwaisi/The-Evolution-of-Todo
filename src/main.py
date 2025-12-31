# """
# Main entry point for the Todo CLI application.

# This module orchestrates the application flow:
# - Initializes the application state
# - Handles authentication
# - Starts the main event loop
# """
# import sys
# import os
# # Add the project root to the Python path
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from src.auth.authenticator import Authenticator
# from src.tasks.repository import TaskRepository
# from src.tasks.service import TaskService
# from src.cli.greetings import display_welcome, display_goodbye
# from src.cli.prompt import (
#     get_username_input, get_password_input, display_error
# )
# from src.utils.intent_parser import parse_intent, is_exit_intent
# from src.cli.menu import display_menu as show_menu


# def authenticate_user() -> str:
#     """
#     Handle the authentication flow with user creation support.

#     Returns:
#         The authenticated username
#     """
#     authenticator = Authenticator()

#     username = get_username_input()

#     # Check if user exists
#     if authenticator.user_exists(username):
#         # User exists, authenticate with password
#         while True:
#             password = get_password_input()
#             if authenticator.authenticate(username, password):
#                 return username
#             else:
#                 display_error("Invalid password. Please try again.")
#     else:
#         # User doesn't exist, create new user
#         display_info(f"New user '{username}' detected. Please set a password.")
#         password = get_password_input()
#         authenticator.add_user(username, password)
#         display_success(f"User '{username}' created successfully!")
#         return username


# def main_event_loop(username: str) -> None:
#     """
#     Run the main event loop of the application.

#     Args:
#         username: The authenticated username
#     """
#     # Initialize services
#     task_repository = TaskRepository()
#     task_service = TaskService(task_repository)

#     # Display welcome message
#     display_welcome(username)

#     while True:
#         # Show the menu
#         show_menu()

#         # Get user input
#         user_input = input("\nEnter your choice: ").strip()

#         # Check for exit intent
#         if is_exit_intent(user_input):
#             break

#         # Parse the intent
#         intent = parse_intent(user_input)

#         if intent is None:
#             display_error("Invalid choice. Please try again.")
#             continue

#         # Dispatch to appropriate service based on intent
#         if intent == 'add_task':
#             task_service.add_task_flow()
#         elif intent == 'list_tasks':
#             task_service.list_tasks_flow()
#         elif intent == 'update_task':
#             task_service.update_task_flow()
#         elif intent == 'delete_task':
#             task_service.delete_task_flow()
#         elif intent == 'toggle_task':
#             task_service.toggle_task_flow()
#         elif intent == 'exit':
#             break
#         else:
#             display_error("Invalid choice. Please try again.")

#         # Wait for user to press enter before showing menu again
#         input("\nPress Enter to continue...")


# def main():
#     """
#     Main entry point of the application.
#     """
#     print("Welcome to the Todo CLI Application!")
#     print("Please authenticate to continue...")

#     # Authenticate user
#     username = authenticate_user()

#     # Run main event loop
#     main_event_loop(username)

#     # Display goodbye message
#     display_goodbye(username)


# if __name__ == "__main__":
#     main()






"""
Main entry point for the Todo CLI application.

Handles:
- Authentication (new and existing users)
- Main event loop
- CLI menu dispatch
"""
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.auth.authenticator import Authenticator
from src.tasks.repository import TaskRepository
from src.tasks.service import TaskService
from src.cli.greetings import display_welcome, display_goodbye
from src.cli.prompt import (
    get_username_input, get_password_input,
    display_error, display_info, display_success
)
from src.utils.intent_parser import parse_intent, is_exit_intent
from src.cli.menu import display_menu as show_menu


def authenticate_user() -> str:
    authenticator = Authenticator()

    while True:
        username = get_username_input()

        if authenticator.user_exists(username):
            while True:
                password = get_password_input()
                if authenticator.authenticate(username, password):
                    return username
                else:
                    display_error("Invalid password. Please try again.")
        else:
            display_info(f"New user '{username}' detected. Please set a password.")
            password = get_password_input()
            authenticator.add_user(username, password)
            display_success(f"User '{username}' created successfully!")
            return username


def main_event_loop(username: str) -> None:
    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    display_welcome(username)

    while True:
        show_menu()
        user_input = input("\nEnter your choice: ").strip()

        if is_exit_intent(user_input):
            break

        intent = parse_intent(user_input)
        if intent is None:
            display_error("Invalid choice. Please try again.")
            continue

        if intent == 'add_task':
            task_service.add_task_flow()
        elif intent == 'list_tasks':
            task_service.list_tasks_flow()
        elif intent == 'update_task':
            task_service.update_task_flow()
        elif intent == 'delete_task':
            task_service.delete_task_flow()
        elif intent == 'toggle_task':
            task_service.toggle_task_flow()
        elif intent == 'exit':
            break
        else:
            display_error("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")


def main():
    print("Welcome to the Todo CLI Application!")
    print("Please authenticate to continue...")

    username = authenticate_user()
    main_event_loop(username)
    display_goodbye(username)


if __name__ == "__main__":
    main()
