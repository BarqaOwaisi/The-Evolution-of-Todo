"""
Task models for the Todo CLI application.

Defines:
- Task data structure
- Task attributes and methods
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a task in the Todo CLI application.

    Attributes:
        id: Unique identifier for the task
        title: Title of the task (required)
        description: Description of the task (optional)
        completed: Completion status of the task (default: False)
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __str__(self) -> str:
        """Return a string representation of the task."""
        status = "✔ [Done]" if self.completed else "✖ [Pending]"
        return f"[{self.id}] {self.title} - {status}"