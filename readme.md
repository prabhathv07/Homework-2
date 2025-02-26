# Command Pattern and Plugins Homework 5

This project is an interactive command-line calculator application that demonstrates the use of the **command pattern**, **REPL (Read-Evaluate-Print-Loop)**, and a **plugin architecture**. It allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) interactively and supports dynamic loading of new commands via plugins.

---

## Features

1. **Command Pattern**:

   - Each arithmetic operation (`add`, `subtract`, `multiply`, `divide`) is implemented as a command class.
   - Commands are registered in a central command registry and executed dynamically.

2. **REPL (Read-Evaluate-Print-Loop)**:

   - The application runs interactively, allowing users to input commands repeatedly.
   - Handles invalid inputs gracefully (e.g., division by zero, non-numeric inputs).

3. **Plugin Architecture**:

   - New commands can be added dynamically by placing them in the `plugins/` folder.
   - The application automatically loads plugins at startup.

4. **Bonus Features**:
   - **Menu Command**: Displays a list of available commands.
   - **Multiprocessing (Optional)**: Supports parallel execution of commands using Python's `multiprocessing` module.

---

## Project Structure
