"""
Task repository for the Todo CLI application.

Handles:
- In-memory task storage
- Task CRUD operations
"""
from typing import List, Optional
from .models import Task


class TaskRepository:
    """
    In-memory repository for managing tasks.

    Provides methods for:
    - Adding tasks
    - Retrieving all tasks
    - Getting a task by ID
    - Updating tasks
    - Deleting tasks
    - Toggling task completion status
    """

    def __init__(self):
        """Initialize the repository with an empty list of tasks."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the repository.

        Args:
            title: Title of the task (required)
            description: Description of the task (optional)

        Returns:
            The newly created Task object
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the repository.

        Returns:
            List of all Task objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None) -> bool:
        """
        Update an existing task.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if task was updated, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: ID of the task to toggle

        Returns:
            True if task status was toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = not task.completed
        return True