# calculator/repl.py
from .command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from .plugin_manager import PluginManager

class CalculatorREPL:
    def __init__(self):
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
        }
        self.plugin_manager = PluginManager(self.commands)
        self.plugin_manager.load_plugins()

    def start(self):
        while True:
            user_input = input("Enter command: ").split()
            if not user_input:
                continue

            command_name = user_input[0]
            args = map(float, user_input[1:])

            if command_name in self.commands:
                command = self.commands[command_name]
                result = command.execute(*args)
                print(f"Result: {result}")
            else:
                print("Unknown command")

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()
