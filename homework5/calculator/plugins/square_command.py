from calculator.command import Command

class SquareCommand(Command):
    def execute(self, x):
        return x * x
