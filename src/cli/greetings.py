"""
Greetings module for the Todo CLI application.

Handles:
- Randomized session greetings
- Personalized welcome messages
- Goodbye messages
"""
import random
from src.config import GREETING_MESSAGES, GOODBYE_MESSAGES


def get_random_greeting(username: str) -> str:
    """
    Get a random greeting message for the user.

    Args:
        username: The name of the user

    Returns:
        A personalized greeting message
    """
    greeting = random.choice(GREETING_MESSAGES)
    return greeting.format(name=username)


def get_random_goodbye(username: str) -> str:
    """
    Get a random goodbye message for the user.

    Args:
        username: The name of the user

    Returns:
        A personalized goodbye message
    """
    goodbye = random.choice(GOODBYE_MESSAGES)
    return goodbye.format(name=username)


def display_welcome(username: str) -> None:
    """
    Display a welcome message to the user.

    Args:
        username: The name of the user
    """
    greeting = get_random_greeting(username)
    print(f"\n{greeting}\n")


def display_goodbye(username: str) -> None:
    """
    Display a goodbye message to the user.

    Args:
        username: The name of the user
    """
    goodbye = get_random_goodbye(username)
    print(f"\n{goodbye}\n")