from calculator.command import Command
from calculator.factory import CommandFactory

class SquareCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, operand):
        result = operand * operand
        self.calculator._store_calculation("square", operand, None, result)
        return result

class SquareCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return SquareCommand(calculator)
