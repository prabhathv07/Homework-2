# Calculator Project

This is a simple calculator project that performs basic arithmetic operations (addition, subtraction, multiplication, division) using Decimal numbers for precision.

## Features

- Perform arithmetic operations with high precision.
- Maintain a history of calculations.
- Generate test data using Faker.
- Handle user input with exception handling.

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`.

## Usage

- Run the calculator: `python main.py <number1> <number2> <operation>`.
- Run tests: `pytest`.

## Testing

- Generate test data: `pytest --num_records=100`.
- Run all tests: `pytest`.
