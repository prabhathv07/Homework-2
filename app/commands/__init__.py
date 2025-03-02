"""This module defines the command interface and registers all available commands."""
from .add import AddCommand
from .subtract import SubtractCommand
from .multiply import MultiplyCommand
from .divide import DivideCommand
from .menu import MenuCommand

__all__ = ['AddCommand', 'SubtractCommand', 'MultiplyCommand', 'DivideCommand', 'MenuCommand']
