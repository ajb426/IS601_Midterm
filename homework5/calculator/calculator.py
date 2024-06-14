# calculator/calculator.py

from calculator.calculation import Calculation

class Calculator:
    """
    A calculator class to perform arithmetic operations and manage calculation history.
    """
    history = []

    @staticmethod
    def add(x, y):
        result = x + y
        Calculator._store_calculation("+", x, y, result)
        return result

    @staticmethod
    def subtract(x, y):
        result = x - y
        Calculator._store_calculation("-", x, y, result)
        return result

    @staticmethod
    def multiply(x, y):
        result = x * y
        Calculator._store_calculation("*", x, y, result)
        return result

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        result = x / y
        Calculator._store_calculation("/", x, y, result)
        return result

    @classmethod
    def _store_calculation(cls, operation, x, y, result):
        calculation = Calculation(operation, x, y, result)
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history = []

    @classmethod
    def get_last_calculation(cls):
        if cls.history:
            return cls.history[-1]
        return None
