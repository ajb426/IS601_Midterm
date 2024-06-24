import logging


class CalculatorREPL:
    def __init__(self, commands):
        self.commands = commands

    def start(self):
        if 'menu' in self.commands:
            self.commands['menu'].execute()
        logging.info("Calculator REPL started")
        print("Calculator REPL. Type 'exit' to quit.")
        while True:
            user_input = input("Enter command: ").split()
            if not user_input:
                continue

            command_name = user_input[0].lower()
            if command_name == 'exit':
                logging.info("Exiting REPL")
                print("Exiting REPL...")
                break

            try:
                args = list(map(float, user_input[1:]))
            except ValueError as e:
                logging.error("Invalid input: %s", e)
                print(f"Error: {e}")
                continue

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
                    logging.info("Executed command '%s' with args %s: Result %s", command_name, args, result)
                except Exception as e:
                    logging.error("Error executing command '%s': %s", command_name, e)
                    print(f"Error: {e}")
            else:
                logging.warning("Unknown command: %s", command_name)
                print("Unknown command")

if __name__ == "__main__":
    from calculator import CalculatorApp
    app = CalculatorApp()
    app.start()
