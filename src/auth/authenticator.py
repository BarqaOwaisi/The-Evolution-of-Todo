"""
Authentication module for the Todo CLI application.

Handles:
- User authentication
- Credential validation
- Session management
- User creation for new users
"""
from dataclasses import dataclass


@dataclass
class User:
    """
    Represents a user in the Todo CLI application.

    Attributes:
        username: The user's username
        password: The user's password
    """
    username: str
    password: str


class Authenticator:
    """
    Handles user authentication using an in-memory user store.

    Provides methods for:
    - Validating user credentials
    - Checking user existence
    - Creating new users
    """

    def __init__(self):
        """Initialize the authenticator with default users."""
        self._users = [
            User(username="admin", password="password"),
            User(username="user", password="123456")
        ]

    def authenticate(self, username: str, password: str) -> bool:
        """Return True if username and password match a user in memory."""
        return any(user.username == username and user.password == password for user in self._users)

    def user_exists(self, username: str) -> bool:
        """Return True if a user with the given username exists."""
        return any(user.username == username for user in self._users)

    def add_user(self, username: str, password: str) -> bool:
        """
        Add a new user in memory.
        Returns False if username already exists.
        """
        if self.user_exists(username):
            return False
        self._users.append(User(username=username, password=password))
        return True
