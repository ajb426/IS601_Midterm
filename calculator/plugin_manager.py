"""
Plugin Manager Module

This module contains the PluginManager class, which is responsible for
loading and integrating command plugins into the calculator application.
"""

import os
import logging
import importlib
from calculator.command import Command

class PluginManager:
    """
    Manages the loading and integration of command plugins into the calculator application.
    """

    def __init__(self, command_dict, calculator):
        """
        Initialize the PluginManager.

        Args:
            command_dict (dict): A dictionary to store command instances.
            calculator (Calculator): An instance of the Calculator class.
        """
        self.command_dict = command_dict
        self.calculator = calculator

    def load_plugins(self, plugin_folder='calculator/plugins'):
        """
        Load command plugins from the specified plugin folder.

        Args:
            plugin_folder (str): The folder to search for plugin modules.
            Defaults to 'calculator/plugins'.
        """
        loaded_commands = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{plugin_folder.replace('/', '.')}.{module_name}")
                for name, obj in module.__dict__.items():
                    if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                        command_name = name.lower().replace('command', '')
                        if command_name == 'menu':
                            self.command_dict[command_name] = obj(self.command_dict)
                        else:
                            self.command_dict[command_name] = obj(self.calculator)
                        loaded_commands.append(command_name)
        if loaded_commands:
            logging.info("Loaded plugin commands: %s", loaded_commands)
        else:
            logging.info("No plugin commands loaded.")
