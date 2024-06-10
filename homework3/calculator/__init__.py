class Calculation:
    def __init__(self, operation, x, y, result):
        self.operation = operation
        self.x = x
        self.y = y
        self.result = result

    def __repr__(self):
        return f"{self.x} {self.operation} {self.y} = {self.result}"


class Calculator:
    history = []

    def __init__(self):
        self.result = 0

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
        try:
            result = x / y
            Calculator._store_calculation("/", x, y, result)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

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