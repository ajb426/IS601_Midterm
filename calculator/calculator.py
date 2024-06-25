"""
Calculator module for performing basic arithmetic operations and managing calculation history.
"""

from calculator.calculation import Calculation
import pandas as pd

class Calculator:
    """
    A calculator class to perform arithmetic operations and manage calculation history.
    """

    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
    

    @staticmethod
    @staticmethod
    def add(operand1, operand2):
        """
        Add two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of adding operand1 and operand2.
        """
        result = operand1 + operand2
        Calculator._store_calculation("+", operand1, operand2, result)
        return result

    @staticmethod
    def subtract(operand1, operand2):
        """
        Subtract two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of subtracting operand2 from operand1.
        """
        result = operand1 - operand2
        Calculator._store_calculation("-", operand1, operand2, result)
        return result

    @staticmethod
    def multiply(operand1, operand2):
        """
        Multiply two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of multiplying operand1 by operand2.
        """
        result = operand1 * operand2
        Calculator._store_calculation("*", operand1, operand2, result)
        return result

    @staticmethod
    def divide(operand1, operand2):
        """
        Divide two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of dividing operand1 by operand2.

        Raises:
            ValueError: If operand2 is zero.
        """
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        result = operand1 / operand2
        Calculator._store_calculation("/", operand1, operand2, result)
        return result

    @classmethod
    def _store_calculation(self, operation, operand1, operand2, result):
        """
        Store a calculation in the history.

        Args:
            operation (str): The arithmetic operation performed.
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the operation.
        """
        new_record = pd.DataFrame([[operation, operand1, operand2, result]], columns=['operation', 'operand1', 'operand2', 'result'])
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    @classmethod
    def get_history(self):
        """
        Get the history of calculations.

        Returns:
            list: A list of all Calculation instances.
        """
        return self.history

    @classmethod
    def clear_history(self):
        """
        Clear the history of calculations.
        """
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
    @classmethod
    def get_last_calculation(self):
        """
        Get the last calculation from the history.

        Returns:
            Calculation: The last Calculation instance, or None if the history is empty.
        """
        if not self.history.empty:
            return self.history.iloc[-1]
        return None

    def save_history_to_csv(self, file_path):
        self.history.to_csv(file_path, index=False)

    def load_history_from_csv(self, file_path):
        self.history = pd.read_csv(file_path)
