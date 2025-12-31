"""
Task service for the Todo CLI application.

Handles:
- Task business logic
- Task operations coordination
"""
from typing import Optional
from src.tasks.repository import TaskRepository
from src.tasks.models import Task
from src.cli.prompt import (
    get_task_title, get_task_description, display_error,
    display_success, display_info
)


class TaskService:
    """
    Service layer for handling task business logic.

    Provides methods for:
    - Adding tasks
    - Listing tasks
    - Updating tasks
    - Deleting tasks
    - Toggling task completion status
    """

    def __init__(self, repository: TaskRepository):
        """Initialize the service with a task repository."""
        self.repository = repository

    def add_task_flow(self) -> bool:
        """
        Handle the add task flow.

        Returns:
            True if task was added successfully, False otherwise
        """
        title = get_task_title()

        if not title:
            display_error("Task title cannot be empty.")
            return False

        description = get_task_description()
        task = self.repository.add_task(title, description)
        display_success(f"Task '{task.title}' added successfully with ID {task.id}.")
        return True

    def list_tasks_flow(self) -> None:
        """
        Handle the list tasks flow.
        """
        tasks = self.repository.get_all_tasks()
        from src.cli.prompt import display_tasks
        display_tasks(tasks)

    def update_task_flow(self) -> bool:
        """
        Handle the update task flow.

        Returns:
            True if task was updated successfully, False otherwise
        """
        from src.cli.prompt import get_task_id

        task_id = get_task_id()
        if task_id is None:
            display_error("Invalid task ID.")
            return False

        task = self.repository.get_task_by_id(task_id)
        if task is None:
            display_error(f"Task with ID {task_id} not found.")
            return False

        # Get new values (or keep existing ones if not provided)
        display_info(f"Current task: {task.title}")
        if task.description:
            display_info(f"Current description: {task.description}")

        new_title = get_task_title()
        if not new_title:
            new_title = task.title  # Keep existing title if no new title provided

        new_description = get_task_description()
        if new_description is None:
            new_description = task.description  # Keep existing description if no new one provided

        success = self.repository.update_task(task_id, new_title, new_description)
        if success:
            display_success(f"Task with ID {task_id} updated successfully.")
            return True
        else:
            display_error(f"Failed to update task with ID {task_id}.")
            return False

    def delete_task_flow(self) -> bool:
        """
        Handle the delete task flow.

        Returns:
            True if task was deleted successfully, False otherwise
        """
        from src.cli.prompt import get_task_id, confirm_action

        task_id = get_task_id()
        if task_id is None:
            display_error("Invalid task ID.")
            return False

        task = self.repository.get_task_by_id(task_id)
        if task is None:
            display_error(f"Task with ID {task_id} not found.")
            return False

        if confirm_action(f"Are you sure you want to delete task '{task.title}'?"):
            success = self.repository.delete_task(task_id)
            if success:
                display_success(f"Task '{task.title}' deleted successfully.")
                return True
            else:
                display_error(f"Failed to delete task with ID {task_id}.")
                return False
        else:
            display_info("Task deletion cancelled.")
            return False

    def toggle_task_flow(self) -> bool:
        """
        Handle the toggle task completion flow.

        Returns:
            True if task status was toggled successfully, False otherwise
        """
        from src.cli.prompt import get_task_id

        task_id = get_task_id()
        if task_id is None:
            display_error("Invalid task ID.")
            return False

        task = self.repository.get_task_by_id(task_id)
        if task is None:
            display_error(f"Task with ID {task_id} not found.")
            return False

        success = self.repository.toggle_task_status(task_id)
        if success:
            new_status = "completed" if task.completed else "incomplete"
            display_success(f"Task '{task.title}' marked as {new_status}.")
            return True
        else:
            display_error(f"Failed to toggle task with ID {task_id}.")
            return False