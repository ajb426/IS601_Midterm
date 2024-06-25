from calculator.command import Command

class SquareCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, operand):
        result = operand * operand
        self.calculator._store_calculation("square", operand, operand, result)
        return result
