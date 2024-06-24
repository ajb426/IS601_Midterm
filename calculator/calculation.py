"""
Calculation module for representing individual arithmetic calculations.
"""

class Calculation:
    """
    A class to represent a single calculation.
    """
    def __init__(self, operation, operand1, operand2, result):
        """
        Initialize a Calculation instance.

        Args:
            operation (str): The arithmetic operation performed.
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the calculation.
        """
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result

    def __repr__(self):
        """
        Return a string representation of the calculation.

        Returns:
            str: A string showing the calculation details.
        """
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"

    def get_details(self):
        """
        Get the details of the calculation.

        Returns:
            tuple: A tuple containing the operation, operands, and result.
        """
        return (self.operation, self.operand1, self.operand2, self.result)
