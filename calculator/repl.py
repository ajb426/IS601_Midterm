"""
REPL (Read-Eval-Print Loop) for the Calculator application.
"""

from calculator.command import (AddCommand, SubtractCommand, MultiplyCommand, DivideCommand,
                                GetHistoryCommand, ClearHistoryCommand, GetLastCalculationCommand)
from calculator.plugin_manager import PluginManager

class CalculatorREPL:
    """
    A REPL class to interact with the Calculator through commands.
    """
    def __init__(self):
        """
        Initialize the REPL with available commands.
        """
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
            'history': GetHistoryCommand(),
            'clear_history': ClearHistoryCommand(),
            'last': GetLastCalculationCommand()        
        }
        self.plugin_manager = PluginManager(self.commands)
        self.plugin_manager.load_plugins()

    def start(self):
        """
        Start the REPL loop, taking user input and executing commands.
        """
        if 'menu' in self.commands:
            self.commands['menu'].execute()
        print("Calculator REPL. Type 'exit' to quit.")
        while True:
            user_input = input("Enter command: ").split()
            if not user_input:
                continue
            command_name, *args = user_input
            if command_name.lower() == 'exit':
                print("Exiting REPL...")
                break
            command = self.commands.get(command_name)
            if command:
                try:
                    result = command.execute(*map(float, args))
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
                except TypeError as e:
                    print(f"Error: {e}")
            else:
                print("Unknown command")


if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()
