from calculator.command import Command, CommandFactory


class MenuCommand(Command):
    def __init__(self, command_dict):
        self.command_dict = command_dict

    def execute(self):
        print("Available commands:")
        for command_name in self.command_dict:
            print(f" - {command_name}")

class MenuCommandFactory(CommandFactory):
    def create_command(self, command_dict):
        return MenuCommand(command_dict)
