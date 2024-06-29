# tests/plugins/dummy_plugin.py

from calculator.command import Command

class DummyAddCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return x + y

class DummySubtractCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return x - y
