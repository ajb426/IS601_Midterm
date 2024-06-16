from calculator.command import Command

class MockAddCommand(Command):
    def execute(self, x, y):
        return x + y

class MockSubtractCommand(Command):
    def execute(self, x, y):
        return x - y
