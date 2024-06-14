"""
Test suite for the Calculator and Calculation classes.

This module contains tests for the following functionalities:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Exception handling for division by zero
- History management
- String representation and detail retrieval
- Initialization of Calculator instances
"""

import pytest
from calculator.calculator import Calculator
from calculator.calculation import Calculation

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 15),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(x, y, expected):
    """
    Test the add method of the Calculator class.
    """
    assert Calculator.add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 5),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract(x, y, expected):
    """
    Test the subtract method of the Calculator class.
    """
    assert Calculator.subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 50),
    (-1, -1, 1),
    (0, 5, 0),
])
def test_multiply(x, y, expected):
    """
    Test the multiply method of the Calculator class.
    """
    assert Calculator.multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 2.0),
    (-10, -5, 2.0),
    (0, 5, 0.0),
])
def test_divide(x, y, expected):
    """
    Test the divide method of the Calculator class.
    """
    assert Calculator.divide(x, y) == expected

def test_divide_by_zero():
    """
    Test division by zero in the Calculator class.
    """
    assert Calculator.divide(10, 0) == "Error: Division by zero is not allowed."

def test_history():
    """
    Test the history management methods of the Calculator class.
    """
    Calculator.clear_history()
    Calculator.add(1, 1)
    Calculator.subtract(2, 1)
    assert len(Calculator.get_history()) == 2
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0

def test_last_calculation():
    """
    Test the get_last_calculation method of the Calculator class.
    """
    Calculator.clear_history()
    Calculator.add(3, 3)
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.result == 6

def test_calculation_get_details():
    """
    Test the get_details method of the Calculation class.
    """
    calculation = Calculation("+", 10, 5, 15)
    details = calculation.get_details()
    assert details == ("+", 10, 5, 15)

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.
    """
    calculation = Calculation("+", 10, 5, 15)
    expected_repr = "10 + 5 = 15"
    assert repr(calculation) == expected_repr

def test_calculator_initialization():
    """
    Test the initialization of the Calculator class.
    """
    calculator = Calculator()
    assert calculator.result == 0

def test_get_last_calculation():
    """
    Test the get_last_calculation method of the Calculator class.
    """
    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None  # History is empty, should return None

    Calculator.add(2, 3)
    Calculator.add(4, 5)
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.operation == "+"
    assert last_calc.x == 4
    assert last_calc.y == 5
    assert last_calc.result == 9

    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None
    
