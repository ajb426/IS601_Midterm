# calculator/command.py
from . import Calculator

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
