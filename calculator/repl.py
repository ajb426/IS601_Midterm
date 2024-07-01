"""
This module contains the CalculatorREPL class for running a read-eval-print loop (REPL)
to interact with a calculator via command-line input.
"""

import logging
import pandas as pd

class CalculatorREPL:
    """REPL for interacting with the calculator."""

    def __init__(self, commands):
        """Initialize the REPL with a dictionary of commands."""
        self.commands = commands

    def start(self):
        """Start the REPL loop."""
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

            args = self._parse_args(user_input[1:])

            if command_name in self.commands:
                command = self.commands[command_name]
                try:
                    result = command.execute(*args)
                    self._print_result(result)
                    logging.info("Executed command '%s' with args %s: Result %s",
                                 command_name, args, result)
                except Exception as e:  # pylint: disable=broad-exception-caught
                    logging.error("Error executing command '%s': %s", command_name, e)
                    print(f"Error: {e}")
            else:
                logging.warning("Unknown command: %s", command_name)
                print("Unknown command")

    def _parse_args(self, args):
        """Parse command arguments."""
        parsed_args = []
        for arg in args:
            try:
                parsed_args.append(float(arg) if arg.replace('.', '', 1).isdigit() else arg)
            except ValueError:
                parsed_args.append(arg)
        return parsed_args

    def _print_result(self, result):
        """Print the command result."""
        if result is not None:
            if isinstance(result, pd.DataFrame):
                print(result.to_string(index=False))
            elif isinstance(result, pd.Series):
                print(result.to_string())
            else:
                print(f"Result: {result}")
