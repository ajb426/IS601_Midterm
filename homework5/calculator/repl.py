from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, ClearHistoryCommand, GetLastCalculationCommand

class CalculatorREPL:
    def __init__(self):
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
            'history': GetHistoryCommand(),
            'clear_history': ClearHistoryCommand(),
            'last': GetLastCalculationCommand(),
        }

    def start(self):
        print("Calculator REPL. Type 'exit' to quit.")
        while True:
            user_input = input("Enter command: ").split()
            if not user_input:
                continue

            command_name = user_input[0].lower()
            if command_name == 'exit':
                break

            args = list(map(float, user_input[1:]))

            if command_name in self.commands:
                command = self.commands[command_name]
                try:
                    result = command.execute(*args)
                    if result is not None:
                        if isinstance(result, list):
                            for item in result:
                                print(item)
                        else:
                            print(f"Result: {result}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Unknown command")

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()
