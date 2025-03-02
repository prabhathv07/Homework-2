"""This module defines the MenuCommand class for displaying available commands."""
from app.commands.command import Command

class MenuCommand(Command):
    """Command class for displaying available commands."""
    def execute(self, a=None, b=None) -> str:
        """Display available commands."""
        return "Available commands: add, subtract, multiply, divide"
