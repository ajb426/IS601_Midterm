"""
Calculator module for performing basic arithmetic operations and managing calculation history.
"""

import pandas as pd

class Calculator:
    """
    A calculator class to perform arithmetic operations and manage calculation history.
    """

    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def add(self, operand1, operand2):
        """
        Add two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of adding operand1 and operand2.
        """
        result = operand1 + operand2
        self._store_calculation("+", operand1, operand2, result)
        return result

    def subtract(self, operand1, operand2):
        """
        Subtract two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of subtracting operand2 from operand1.
        """
        result = operand1 - operand2
        self._store_calculation("-", operand1, operand2, result)
        return result

    def multiply(self, operand1, operand2):
        """
        Multiply two numbers.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of multiplying operand1 by operand2.
        """
        result = operand1 * operand2
        self._store_calculation("*", operand1, operand2, result)
        return result

    def divide(self, operand1, operand2):
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
        self._store_calculation("/", operand1, operand2, result)
        return result

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
        if self.history.empty:
            self.history = new_record
        else:
            self.history = pd.concat([self.history, new_record], ignore_index=True)

    def get_history(self):
        """
        Get the history of calculations.

        Returns:
            pd.DataFrame: A DataFrame of all calculations.
        """
        return self.history

    def clear_history(self):
        """
        Clear the history of calculations.
        """
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def get_last_calculation(self):
        """
        Get the last calculation from the history.

        Returns:
            pd.Series: The last calculation, or None if the history is empty.
        """
        if not self.history.empty:
            return self.history.iloc[-1]
        return None

    def save_history_to_csv(self, file_path):
        """
        Save the calculation history to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """
        self.history.to_csv(file_path, index=False)

    def load_history_from_csv(self, file_path):
        """
        Load the calculation history from a CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """
        self.history = pd.read_csv(file_path)
