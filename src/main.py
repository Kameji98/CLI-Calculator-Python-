#!/usr/bin/env python3
"""
CLI Calculator (Python)

A simple, robust command-line calculator to practice:
- input validation
- control flow
- clean function design
- error handling
"""

from __future__ import annotations


def read_number(prompt: str) -> float:
    """Read a float from user input with validation."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value (e.g., 12, 3.5).")


def read_operator() -> str:
    """Read an operator from user input with validation."""
    allowed = {"+", "-", "*", "/", "**"}
    while True:
        op = input("Choose an operator (+, -, *, /, **): ").strip()
        if op in allowed:
            return op
        print("Invalid operator. Allowed: +  -  *  /  **")


def calculate(a: float, op: str, b: float) -> float:
    """Perform the calculation and return the result."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    if op == "**":
        return a ** b
    raise ValueError(f"Unsupported operator: {op}")


def ask_continue() -> bool:
    """Ask user whether they want to continue."""
    while True:
        choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Please answer with 'y' or 'n'.")


def format_result(value: float) -> str:
    """
    Format result nicely:
    - Show as int when it's effectively an integer
    - Otherwise show up to 10 significant digits (clean output)
    """
    if abs(value - int(value)) < 1e-12:
        return str(int(value))
    return f"{value:.10g}"


def main() -> None:
    print("=== CLI Calculator ===")
    print("Tip: '**' is power (e.g., 2 ** 3 = 8).")
    print()

    while True:
        a = read_number("Enter the first number: ")
        op = read_operator()
        b = read_number("Enter the second number: ")

        try:
            result = calculate(a, op, b)
            print(f"Result: {format_result(result)}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print()
        if not ask_continue():
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()
