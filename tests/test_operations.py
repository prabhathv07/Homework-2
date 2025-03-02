"""This module contains tests for the arithmetic operations."""
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

def test_add():
    """Test addition."""
    assert add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract():
    """Test subtraction."""
    assert subtract(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply():
    """Test multiplication."""
    assert multiply(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide():
    """Test division."""
    assert divide(Decimal('6'), Decimal('2')) == Decimal('3')

def test_divide_by_zero():
    """Test division by zero."""
    try:
        divide(Decimal('10'), Decimal('0'))
    except ValueError as error:  # Renamed from 'e' to 'error'
        assert str(error) == "Cannot divide by zero"
