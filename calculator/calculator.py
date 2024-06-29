import pandas as pd
from calculator.singleton import SingletonMeta

class Calculator(metaclass=SingletonMeta):
    """
    A calculator class to perform arithmetic operations and manage calculation history.
    """

    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def add(self, operand1, operand2):
        result = operand1 + operand2
        self._store_calculation("+", operand1, operand2, result)
        return result

    def subtract(self, operand1, operand2):
        result = operand1 - operand2
        self._store_calculation("-", operand1, operand2, result)
        return result

    def multiply(self, operand1, operand2):
        result = operand1 * operand2
        self._store_calculation("*", operand1, operand2, result)
        return result

    def divide(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        result = operand1 / operand2
        self._store_calculation("/", operand1, operand2, result)
        return result

    def _store_calculation(self, operation, operand1, operand2, result):
        new_record = pd.DataFrame([[operation, operand1, operand2, result]], columns=['operation', 'operand1', 'operand2', 'result'])
        if self.history.empty:
            self.history = new_record
        else:
            self.history = pd.concat([self.history, new_record], ignore_index=True)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def get_last_calculation(self):
        if not self.history.empty:
            return self.history.iloc[-1]
        return None

    def save_history_to_csv(self, file_path):
        self.history.to_csv(file_path, index=False)

    def load_history_from_csv(self, file_path):
        self.history = pd.read_csv(file_path)
