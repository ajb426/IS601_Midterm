# calculator/plugin_manager.py
import importlib
import os
from calculator.command import Command

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
                        self.command_dict[name.lower()] = obj()
