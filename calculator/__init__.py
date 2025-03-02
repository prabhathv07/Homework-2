"""This module provides a simple interface for performing calculations."""
from .calculator import Calculator
from .operations import add, subtract, multiply, divide
from .calculation import Calculation
from .calculations import Calculations

__all__ = ['Calculator', 'add', 'subtract', 'multiply', 'divide', 'Calculation', 'Calculations']
