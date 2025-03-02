"""This module contains tests for the Calculation class."""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(num1, num2, operation, expected):
    """Test calculation operations."""
    calc = Calculation(num1, num2, operation)
    assert calc.perform() == expected, (
        f"Failed {operation.__name__} operation with {num1} and {num2}"
    )

def test_calculation_repr():
    """Test the string representation of a calculation."""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, (
        "The __repr__ method output does not match the expected string."
    )

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc = Calculation(Decimal('10'), Decimal('0'), divide)
        calc.perform()
