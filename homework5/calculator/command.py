# calculator/command.py

from calculator.calculator import Calculator

class Command:
    def execute(self, *args):
        pass

class AddCommand(Command):
    def execute(self, x, y):
        return Calculator.add(x, y)

class SubtractCommand(Command):
    def execute(self, x, y):
        return Calculator.subtract(x, y)

class MultiplyCommand(Command):
    def execute(self, x, y):
        return Calculator.multiply(x, y)

class DivideCommand(Command):
    def execute(self, x, y):
        return Calculator.divide(x, y)

class GetHistoryCommand(Command):
    def execute(self):
        return Calculator.get_history()

class ClearHistoryCommand(Command):
    def execute(self):
        return Calculator.clear_history()

class GetLastCalculationCommand(Command):
    def execute(self):
        return Calculator.get_last_calculation()
