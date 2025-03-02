"""This module defines fixtures and test data for pytest."""
import sys
import os
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for calculations."""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        num1 = Decimal(fake.random_number(digits=2))
        num2 = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Handle division by zero
        if operation_name == 'divide':
            num2 = Decimal('1') if num2 == Decimal('0') else num2

        try:
            expected = operation_func(num1, num2)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield num1, num2, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Add command-line option for number of test records."""
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    """Generate tests dynamically based on command-line options."""
    if {"num1", "num2", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (num1, num2, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for num1, num2, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("num1,num2,operation,expected", modified_parameters)
