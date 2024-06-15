import importlib
import os
from calculator.command import Command
import inspect

class PluginManager:
    def __init__(self, command_dict):
        self.command_dict = command_dict

    def load_plugins(self, plugin_folder='calculator/plugins'):
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"calculator.plugins.{module_name}")
                for name, obj in module.__dict__.items():
                    if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                        # Simplify command name
                        command_name = name.lower().replace('command', '')
                        init_params = inspect.signature(obj.__init__).parameters
                        if 'command_dict' in init_params:
                            self.command_dict[command_name] = obj(self.command_dict)
                        else:
                            self.command_dict[command_name] = obj()
                        print(f"Loaded plugin command: {command_name}")  # Debugging line
