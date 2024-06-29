import os
import sys
import importlib
import pytest
from unittest.mock import patch, MagicMock
from calculator.plugin_manager import PluginManager
from calculator.calculator import Calculator

# Ensure the tests/plugins directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'plugins')))

def test_load_plugins():
    command_dict = {}
    calculator = Calculator()
    plugin_manager = PluginManager(command_dict, calculator)

    # Load plugins from tests/plugins directory
    plugin_manager.load_plugins('tests/plugins')

    # Verify that plugins are loaded correctly
    assert 'dummyadd' in command_dict
    assert 'dummysubtract' in command_dict
    assert isinstance(command_dict['dummyadd'], Command)
    assert isinstance(command_dict['dummysubtract'], Command)

# Run the test function
if __name__ == "__main__":
    test_load_plugins()