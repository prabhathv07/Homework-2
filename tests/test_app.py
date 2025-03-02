"""This module contains tests for the app package."""
from decimal import Decimal
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command():
    """Test the AddCommand class."""
    command = AddCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract_command():
    """Test the SubtractCommand class."""
    command = SubtractCommand()
    assert command.execute(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply_command():
    """Test the MultiplyCommand class."""
    command = MultiplyCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide_command():
    """Test the DivideCommand class."""
    command = DivideCommand()
    assert command.execute(Decimal('6'), Decimal('2')) == Decimal('3')

# pylint: disable=duplicate-code
