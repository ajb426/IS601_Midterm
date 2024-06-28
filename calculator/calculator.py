from calculator.calculation import Calculation
from calculator.calculator_history import CalculatorHistory

class Calculator:
    """
    A calculator class to perform arithmetic operations and manage calculation history.
    """

    def __init__(self):
        self.history = CalculatorHistory()

    def add(self, operand1, operand2):
        result = operand1 + operand2
        self.history.add_record(Calculation("+", operand1, operand2, result))
        return result

    def subtract(self, operand1, operand2):
        result = operand1 - operand2
        self.history.add_record(Calculation("-", operand1, operand2, result))
        return result

    def multiply(self, operand1, operand2):
        result = operand1 * operand2
        self.history.add_record(Calculation("*", operand1, operand2, result))
        return result

    def divide(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        result = operand1 / operand2
        self.history.add_record(Calculation("/", operand1, operand2, result))
        return result

    def get_history(self):
        return self.history.get_all_records()

    def clear_history(self):
        self.history.clear_history()

    def get_last_calculation(self):
        return self.history.get_last_record()

    def save_history_to_csv(self, file_path=None):
        if file_path:
            self.history.set_file_path(file_path)
        self.history.save_to_csv()

    def load_history_from_csv(self, file_path=None):
        if file_path:
            self.history.set_file_path(file_path)
        self.history.load_from_csv()
