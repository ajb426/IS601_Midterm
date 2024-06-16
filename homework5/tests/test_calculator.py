"""
Test suite for the Calculator and Calculation classes.

This module contains tests for the following functionalities:
- Basic arithmetic operations (add, subtract, multiply, divide) in the Calculator class
- Exception handling for division by zero in the Calculator class
- History management in the Calculator class
- String representation and detail retrieval in the Calculation class
- Initialization of Calculator instances
"""

from faker import Faker
from calculator.calculator import Calculator
from calculator.calculation import Calculation
import pytest

fake = Faker()

@pytest.mark.parametrize("operation, function", [
    ("add", Calculator.add),
    ("subtract", Calculator.subtract),
    ("multiply", Calculator.multiply),
    ("divide", Calculator.divide)
])
def test_operations(operation, function):
    """
    Parametrized test for basic arithmetic operations.
    """
    x = fake.random_number(digits=2)
    y = fake.random_number(digits=2) if operation != "divide" else fake.random_number(digits=2, fix_len=True) + 1  # avoid division by zero

    if operation == "divide" and y == 0:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            function(x, y)
    else:
        expected = {
            "add": x + y,
            "subtract": x - y,
            "multiply": x * y,
            "divide": x / y
        }[operation]
        assert function(x, y) == expected

def test_divide_by_zero():
    """
    Test division by zero in the Calculator class.
    """
    x = fake.random_number(digits=5)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(x, 0)

def test_history():
    """
    Test the history management methods of the Calculator class.
    """
    Calculator.clear_history()
    Calculator.add(fake.random_number(digits=5), fake.random_number(digits=5))
    Calculator.subtract(fake.random_number(digits=5), fake.random_number(digits=5))
    assert len(Calculator.get_history()) == 2
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0

def test_last_calculation():
    """
    Test the get_last_calculation method of the Calculator class.
    """
    Calculator.clear_history()
    x = fake.random_number(digits=5)
    y = fake.random_number(digits=5)
    Calculator.add(x, y)
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.result == x + y

def test_calculation_get_details():
    """
    Test the get_details method of the Calculation class.
    """
    x = fake.random_number(digits=5)
    y = fake.random_number(digits=5)
    calc = Calculation("+", x, y, x + y)
    details = calc.get_details()
    assert details == ("+", x, y, x + y)

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.
    """
    x = fake.random_number(digits=5)
    y = fake.random_number(digits=5)
    calc = Calculation("+", x, y, x + y)
    expected_repr = f"{x} + {y} = {x + y}"
    assert repr(calc) == expected_repr

def test_calculator_initialization():
    """
    Test the initialization of the Calculator class.
    """
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0
