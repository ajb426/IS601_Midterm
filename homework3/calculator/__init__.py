"""
Calculator module to perform basic arithmetic operations and maintain calculation history.
"""

class Calculation:
    """
    A class to represent a single calculation.
    """

    def __init__(self, operation, x, y, result):
        """
        Initialize a Calculation instance.

        Args:
            operation (str): The arithmetic operation performed.
            x (float): The first operand.
            y (float): The second operand.
            result (float): The result of the operation.
        """
        self.operation = operation
        self.x = x
        self.y = y
        self.result = result

    def __repr__(self):
        """
        Return a string representation of the calculation.

        Returns:
            str: A string showing the calculation details.
        """
        return f"{self.x} {self.operation} {self.y} = {self.result}"

    def get_details(self):
        """
        Get the details of the calculation.

        Returns:
            tuple: A tuple containing the operation, operands, and result.
        """
        return (self.operation, self.x, self.y, self.result)


class Calculator:
    """
    A calculator class to perform arithmetic operations and manage calculation history.
    """
    history = []

    def __init__(self):
        """
        Initialize a Calculator instance.
        """
        self.result = 0

    @staticmethod
    def add(x, y):
        """
        Add two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of adding x and y.
        """
        result = x + y
        Calculator._store_calculation("+", x, y, result)
        return result

    @staticmethod
    def subtract(x, y):
        """
        Subtract two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of subtracting y from x.
        """
        result = x - y
        Calculator._store_calculation("-", x, y, result)
        return result

    @staticmethod
    def multiply(x, y):
        """
        Multiply two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of multiplying x by y.
        """
        result = x * y
        Calculator._store_calculation("*", x, y, result)
        return result

    @staticmethod
    def divide(x, y):
        """
        Divide two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of dividing x by y, or an error message if division by zero occurs.
        """
        try:
            result = x / y
            Calculator._store_calculation("/", x, y, result)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    @classmethod
    def _store_calculation(cls, operation, x, y, result):
        """
        Store a calculation in the history.

        Args:
            operation (str): The arithmetic operation performed.
            x (float): The first operand.
            y (float): The second operand.
            result (float): The result of the operation.
        """
        calculation = Calculation(operation, x, y, result)
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        """
        Get the history of calculations.

        Returns:
            list: A list of all Calculation instances.
        """
        return cls.history

    @classmethod
    def clear_history(cls):
        """
        Clear the history of calculations.
        """
        cls.history = []

    @classmethod
    def get_last_calculation(cls):
        """
        Get the last calculation from the history.

        Returns:
            Calculation: The last Calculation instance, or None if the history is empty.
        """
        if cls.history:
            return cls.history[-1]
        return None
    