import pytest
from calculator.plugins.menu_command import MenuCommand
from calculator.plugins.square_command import SquareCommand

def test_menu_command(capfd):
    """Test the MenuCommand plugin."""
    # Create a mock command dictionary
    mock_command_dict = {
        'add': 'AddCommand',
        'subtract': 'SubtractCommand',
        'multiply': 'MultiplyCommand',
        'divide': 'DivideCommand',
        'history': 'GetHistoryCommand',
        'clear_history': 'ClearHistoryCommand',
        'last': 'GetLastCalculationCommand',
        'menu': 'MenuCommand'
    }

    # Instantiate the MenuCommand with the mock command dictionary
    menu_command = MenuCommand(mock_command_dict)
    
    # Execute the menu command
    menu_command.execute()
    
    # Capture the output
    out, err = capfd.readouterr()
    
    # Check that the output matches the expected list of commands
    assert "Available commands:" in out
    for command in mock_command_dict:
        assert f" - {command}" in out

def test_square_command():
    command = SquareCommand()
    result = command.execute(3)
    assert result == 9.0
