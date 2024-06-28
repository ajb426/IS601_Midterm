from abc import ABC, abstractmethod
from calculator.calculator import Calculator

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class AddCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.add(x, y)

class SubtractCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.subtract(x, y)

class MultiplyCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.multiply(x, y)

class DivideCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.divide(x, y)

class GetHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        return self.calculator.get_history()

class ClearHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        self.calculator.clear_history()

class GetLastCalculationCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        return self.calculator.get_last_calculation()

class SaveHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, file_path):
        self.calculator.save_history_to_csv(file_path)

class LoadHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, file_path):
        self.calculator.load_history_from_csv(file_path)
