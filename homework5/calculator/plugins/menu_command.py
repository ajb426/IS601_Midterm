from calculator.command import Command

class MenuCommand(Command):
    def __init__(self, command_dict):
        self.command_dict = command_dict

    def execute(self):
        print("Available commands:")
        for command in self.command_dict:
            print(f" - {command}")
        return None
