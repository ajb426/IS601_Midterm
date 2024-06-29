# tests/test_plugin_manager.py

import os
import sys
import pytest
from unittest.mock import patch
from calculator.plugin_manager import PluginManager
from calculator.calculator import Calculator

# Ensure the tests/plugins directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'plugins')))

# Mocking os.listdir to simulate plugins directory
@patch('os.listdir', return_value=['dummy_plugin.py'])
def test_load_plugins(mock_listdir):
    command_dict = {}
    calculator = Calculator()
    plugin_manager = PluginManager(command_dict, calculator)
    plugin_manager.load_plugins('tests/plugins')

    # Verify that plugins are loaded correctly
    assert 'dummyadd' in command_dict
    assert 'dummysubtract' in command_dict
    assert isinstance(command_dict['dummyadd'], Command)
    assert isinstance(command_dict['dummysubtract'], Command)

    # Further verify the commands work as expected
    assert command_dict['dummyadd'].execute(3, 2) == 5
    assert command_dict['dummysubtract'].execute(5, 3) == 2
