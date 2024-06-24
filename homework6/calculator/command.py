"""
Command module for the calculator application. Defines commands for various arithmetic operations.
"""

from calculator.calculator import Calculator

class Command:
    """
    Base Command class that all other commands inherit from.
    """
    def execute(self, *args):
        """
        Execute the command with the provided arguments.

        Args:
            *args: Variable length argument list.
        """


class AddCommand(Command):
    """
    Command to add two numbers.
    """
    def execute(self, operand1, operand2):
        """
        Execute the add command.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of adding operand1 and operand2.
        """
        return Calculator.add(operand1, operand2)

class SubtractCommand(Command):
    """
    Command to subtract one number from another.
    """
    def execute(self, operand1, operand2):
        """
        Execute the subtract command.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of subtracting operand2 from operand1.
        """
        return Calculator.subtract(operand1, operand2)

class MultiplyCommand(Command):
    """
    Command to multiply two numbers.
    """
    def execute(self, operand1, operand2):
        """
        Execute the multiply command.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of multiplying operand1 by operand2.
        """
        return Calculator.multiply(operand1, operand2)

class DivideCommand(Command):
    """
    Command to divide one number by another.
    """
    def execute(self, operand1, operand2):
        """
        Execute the divide command.

        Args:
            operand1 (float): The first number.
            operand2 (float): The second number.

        Returns:
            float: The result of dividing operand1 by operand2.

        Raises:
            ValueError: If operand2 is zero.
        """
        return Calculator.divide(operand1, operand2)

class GetHistoryCommand(Command):
    """
    Command to get the history of calculations.
    """
    def execute(self):
        """
        Execute the get history command.

        Returns:
            list: The history of calculations.
        """
        return Calculator.get_history()

class ClearHistoryCommand(Command):
    """
    Command to clear the history of calculations.
    """
    def execute(self):
        """
        Execute the clear history command.
        """
        return Calculator.clear_history()

class GetLastCalculationCommand(Command):
    """
    Command to get last calculation.
    """
    def execute(self):
        """
        Execte the get last calculation command.
        """
        return Calculator.get_last_calculation()
