"""
Configuration constants for the Todo CLI application.

Defines:
- Menu option mappings
- Exit keywords
- Status indicators
- Authentication retry limits
"""
# Menu option mappings
MENU_OPTIONS = {
    '1': 'add_task',
    '2': 'list_tasks',
    '3': 'update_task',
    '4': 'delete_task',
    '5': 'toggle_task',
    '6': 'exit'
}

# Natural language mappings
NATURAL_LANGUAGE_MAP = {
    'add': 'add_task',
    'create': 'add_task',
    'new': 'add_task',
    'view': 'list_tasks',
    'list': 'list_tasks',
    'show': 'list_tasks',
    'update': 'update_task',
    'edit': 'update_task',
    'change': 'update_task',
    'delete': 'delete_task',
    'remove': 'delete_task',
    'complete': 'toggle_task',
    'mark': 'toggle_task',
    'done': 'toggle_task',
    'exit': 'exit',
    'quit': 'exit'
}

# Exit keywords
EXIT_KEYWORDS = ['exit', 'quit', '6']

# Status indicators
STATUS_COMPLETED = '✔ [Done]'
STATUS_INCOMPLETE = '✖ [Pending]'

# Authentication settings
MAX_LOGIN_ATTEMPTS = 3

# Greeting messages
GREETING_MESSAGES = [
    "Hello {name}! Welcome to your Todo app!",
    "Hi {name}! Ready to be productive today?",
    "Greetings {name}! Let's get things done!",
    "Welcome back {name}! Time to manage your tasks!",
    "Hey {name}! What would you like to accomplish today?"
]

# Goodbye messages
GOODBYE_MESSAGES = [
    "Goodbye {name}! See you next time!",
    "Thanks for using the Todo app, {name}!",
    "Have a great day, {name}!",
    "Until next time, {name}!",
    "Take care, {name}!"
]