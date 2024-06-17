from calculator.command import Command
from calculator.calculator import Calculator

class SquareCommand(Command):
    def execute(self, operand):
        result = operand * operand
        Calculator._store_calculation("square", operand, operand, result)
        return result
