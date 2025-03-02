"""
Main module for the Calculator application.
This module handles the initialization, command loading, and REPL interface.
"""

import importlib
import logging
import logging.config
import os
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv

from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand

# Load environment variables from .env file
load_dotenv()

# Load logging configuration
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

# Access environment variables
api_key = os.getenv("API_KEY")
environment = os.getenv("ENVIRONMENT")

# Command registry
commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
    'menu': MenuCommand()
}

def load_plugins():
    """Dynamically load commands from the plugins folder."""
    plugins_dir = "plugins"
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugins_dir}.{module_name}")
            for attr in dir(module):
                if attr.endswith("Command"):
                    command_class = getattr(module, attr)
                    commands[module_name] = command_class()

def calculate_and_print(first_number: str, second_number: str, operation_name: str):
    """Perform a calculation and print the result."""
    try:
        a_decimal = Decimal(first_number)
        b_decimal = Decimal(second_number)
        operation = commands.get(operation_name)
        if operation:
            result = operation.execute(a_decimal, b_decimal)
            logger.info(
    f"Performed {operation_name} operation: {first_number} {operation_name} {second_number} = {result}"
)


            print(f"The result of {first_number} {operation_name} {second_number} is equal to {result}")
        else:
            logger.warning("Unknown operation: %s", operation_name)
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        logger.error(
            "Invalid number input: %s or %s is not a valid number.",
            first_number, second_number
        )
        print(f"Invalid number input: {first_number} or {second_number} is not a valid number.")
    except ZeroDivisionError:
        logger.error("Attempted division by zero.")
        print("An error occurred: Cannot divide by zero.")
    except ValueError as error:
        logger.error("An error occurred: %s", error)
        print(f"An error occurred: {error}")

def repl():
    """Read-Evaluate-Print-Loop for the calculator."""
    print("Welcome to the Calculator REPL. Type 'menu' for available commands.")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "exit":
            break
        if user_input == "menu":
            print("Available commands:")
            for cmd in commands:
                print(f"- {cmd}")
        elif user_input in commands:
            try:
                first_number = Decimal(input("Enter first number: "))
                second_number = Decimal(input("Enter second number: "))
                result = commands[user_input].execute(first_number, second_number)
                print(f"Result: {result}")
            except InvalidOperation:
                print("Invalid input. Please enter valid numbers.")
            except ValueError as error:
                print(f"Error: {error}")
        else:
            print("Unknown command. Type 'menu' for available commands.")

def main():
    """Entry point for the program."""
    load_plugins()
    repl()

if __name__ == '__main__':
    main()
