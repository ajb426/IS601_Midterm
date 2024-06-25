"""
Plugin Manager module for loading calculator command plugins dynamically.
"""

import os
import importlib
import inspect
from calculator.command import Command
import logging

class PluginManager:
    """
    Manages loading of command plugins for the calculator.
    """
    def __init__(self, command_dict, calculator):
        """
        Initializes the PluginManager with a dictionary of commands and a calculator instance.

        Args:
            command_dict (dict): Dictionary to store the loaded commands.
            calculator (Calculator): Instance of the Calculator class.
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
                    if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                        # Simplify command name
                        command_name = name.lower().replace('command', '')
                        init_params = inspect.signature(obj.__init__).parameters
                        if 'calculator' in init_params:
                            self.command_dict[command_name] = obj(self.calculator)
                        elif 'command_dict' in init_params:
                            self.command_dict[command_name] = obj(self.command_dict)
                        else:
                            self.command_dict[command_name] = obj()
                        loaded_commands.append(command_name)
        if loaded_commands:
            logging.info(f"Loaded plugin commands: {loaded_commands}")
        else:
            logging.info("No plugin commands loaded.")
