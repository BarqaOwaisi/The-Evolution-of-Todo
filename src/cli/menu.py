"""
Menu module for the Todo CLI application.

Handles:
- Displaying the main menu
- Rendering menu options
- Managing user interface flow
"""
from src.cli.prompt import display_menu as show_menu


def display_menu() -> None:
    """
    Display the main menu to the user.
    """
    show_menu()