import os
import importlib
import inspect
from calculator.command import Command
import logging

class PluginManager:
    def __init__(self, command_dict, calculator):
        self.command_dict = command_dict
        self.calculator = calculator

    def load_plugins(self, plugin_folder='calculator/plugins'):
        loaded_commands = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{plugin_folder.replace('/', '.')}.{module_name}")
                for name, obj in module.__dict__.items():
                    if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                        command_name = name.lower().replace('command', '')
                        self.command_dict[command_name] = obj(self.command_dict) if command_name == 'menu' else obj(self.calculator)
                        loaded_commands.append(command_name)
        if loaded_commands:
            logging.info(f"Loaded plugin commands: {loaded_commands}")
        else:
            logging.info("No plugin commands loaded.")