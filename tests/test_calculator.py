"""This module contains tests for the Calculator class."""
from decimal import Decimal
import pytest  # Add this import
from calculator.calculator import Calculator

def test_add():
    """Test addition."""
    assert Calculator.add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract():
    """Test subtraction."""
    assert Calculator.subtract(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply():
    """Test multiplication."""
    assert Calculator.multiply(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide():
    """Test division."""
    assert Calculator.divide(Decimal('6'), Decimal('2')) == Decimal('3')

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal('10'), Decimal('0'))
