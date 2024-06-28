from calculator.command import Command
from calculator.factory import CommandFactory

class AddCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.add(x, y)

class AddCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return AddCommand(calculator)

class SubtractCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.subtract(x, y)

class SubtractCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return SubtractCommand(calculator)

class MultiplyCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.multiply(x, y)

class MultiplyCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return MultiplyCommand(calculator)

class DivideCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, x, y):
        return self.calculator.divide(x, y)

class DivideCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return DivideCommand(calculator)

class GetHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        return self.calculator.get_history()

class GetHistoryCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return GetHistoryCommand(calculator)

class ClearHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        self.calculator.clear_history()

class ClearHistoryCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return ClearHistoryCommand(calculator)

class GetLastCalculationCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        return self.calculator.get_last_calculation()

class GetLastCalculationCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return GetLastCalculationCommand(calculator)

class SaveHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, file_path):
        self.calculator.save_history_to_csv(file_path)

class SaveHistoryCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return SaveHistoryCommand(calculator)

class LoadHistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, file_path):
        self.calculator.load_history_from_csv(file_path)

class LoadHistoryCommandFactory(CommandFactory):
    def create_command(self, calculator):
        return LoadHistoryCommand(calculator)
