import os
import sys
import importlib
import pytest
from unittest.mock import patch, MagicMock
from calculator.plugin_manager import PluginManager
from calculator.command import Command

# Ensure the plugins directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../calculator/plugins')))

# Mocking os.listdir to simulate plugins directory
@patch('os.listdir', return_value=['mock_plugins.py'])
@patch('importlib.import_module')
def test_load_plugins(mock_import_module, mock_listdir):
    # Mock the import_module to load our mock plugins
    mock_import_module.return_value = MagicMock(
        MockAddCommand=MockAddCommand,
        MockSubtractCommand=MockSubtractCommand
    )

    command_dict = {}
    plugin_manager = PluginManager(command_dict)
    plugin_manager.load_plugins()

    # Verify that plugins are loaded correctly
    assert 'mockadd' in command_dict
    assert 'mocksubtract' in command_dict
    assert isinstance(command_dict['mockadd'], MockAddCommand)
    assert isinstance(command_dict['mocksubtract'], MockSubtractCommand)

class MockAddCommand(Command):
    def execute(self, x, y):
        return x + y

class MockSubtractCommand(Command):
    def execute(self, x, y):
        return x - y

@patch('os.listdir', return_value=['mock_plugins.py'])
@patch('importlib.import_module', side_effect=lambda name: sys.modules[__name__])
def test_load_plugins(mock_import_module, mock_listdir):
    command_dict = {}
    plugin_manager = PluginManager(command_dict)
    plugin_manager.load_plugins()

    assert 'mockadd' in command_dict
    assert 'mocksubtract' in command_dict
    assert isinstance(command_dict['mockadd'], MockAddCommand)
    assert isinstance(command_dict['mocksubtract'], MockSubtractCommand)
