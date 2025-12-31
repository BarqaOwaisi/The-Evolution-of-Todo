"""
Intent parser for the Todo CLI application.

Handles:
- Natural language intent recognition
- Input normalization
- Command mapping
"""
from typing import Dict, Optional
from src.config import MENU_OPTIONS, NATURAL_LANGUAGE_MAP


def normalize_input(user_input: str) -> str:
    """
    Normalize user input by stripping whitespace and converting to lowercase.

    Args:
        user_input: The raw user input

    Returns:
        The normalized input
    """
    return user_input.strip().lower()


def parse_intent(user_input: str) -> Optional[str]:
    """
    Parse the user's intent from their input.

    Args:
        user_input: The user's input (could be numeric or text)

    Returns:
        The corresponding action, or None if no match found
    """
    normalized_input = normalize_input(user_input)

    # Check if input is a numeric menu option
    if normalized_input in MENU_OPTIONS:
        return MENU_OPTIONS[normalized_input]

    # Split the input into words and check for natural language commands
    words = normalized_input.split()
    for word in words:
        if word in NATURAL_LANGUAGE_MAP:
            return NATURAL_LANGUAGE_MAP[word]

    # If no match found, return None
    return None


def is_exit_intent(user_input: str) -> bool:
    """
    Check if the user's input indicates an exit intent.

    Args:
        user_input: The user's input

    Returns:
        True if the input indicates an exit intent, False otherwise
    """
    normalized_input = normalize_input(user_input)

    # Check if input is a numeric exit option (6)
    if normalized_input == '6':
        return True

    # Check if input matches any exit keywords
    words = normalized_input.split()
    for word in words:
        if word in ['exit', 'quit']:
            return True

    return False