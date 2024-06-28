import os
import importlib
import inspect
from calculator.command import Command
import logging
from calculator.factory import CommandFactory

class PluginManager:
    """
    Manages loading of command plugins for the calculator.
    """
    def __init__(self, command_dict, calculator):
        """
        Initializes the PluginManager with a dictionary of commands and a calculator instance.

        Args:
            command_dict (dict): Dictionary to store the loaded commands.
            calculator (Calculator): The calculator instance to pass to command factories.
        """
        self.command_dict = command_dict
        self.calculator = calculator

    def load_plugins(self, plugin_folder='calculator/plugins'):
        """
        Loads plugins from the plugins directory and updates the command dictionary.
        """
        loaded_commands = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"calculator.plugins.{module_name}")
                for name, obj in module.__dict__.items():
                    print(name)
                    if isinstance(obj, type) and issubclass(obj, CommandFactory) and obj != CommandFactory:
                        factory = obj()
                        if 'command_dict' in inspect.signature(factory.create_command).parameters:
                            command = factory.create_command(self.command_dict)
                        else:
                            command = factory.create_command(self.calculator)
                        command_name = name.lower().replace('factory', '').replace('command', '')
                        self.command_dict[command_name] = command
                        loaded_commands.append(command_name)
        if loaded_commands:
            logging.info(f"Loaded plugin commands: {loaded_commands}")
        else:
            logging.info("No plugin commands loaded.")
