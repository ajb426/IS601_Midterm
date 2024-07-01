import pytest
from calculator.calculator import Calculator
import importlib.util

# Check if the SquareCommand module is available
square_command_available = importlib.util.find_spec("calculator.plugins.square_command") is not None

if square_command_available:
    from calculator.plugins.square_command import SquareCommand, SquareCommandFactory

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.skipif(not square_command_available, reason="SquareCommand not available")
def test_square_command_execution(calculator):
    square_command = SquareCommand(calculator)
    result = square_command.execute(3)
    assert result == 9
    assert len(calculator.get_history()) == 1
    last_calculation = calculator.get_last_calculation()
    assert last_calculation['operation'] == 'square'
    assert last_calculation['operand1'] == 3
    assert last_calculation['operand2'] is None
    assert last_calculation['result'] == 9

@pytest.mark.skipif(not square_command_available, reason="SquareCommand not available")
def test_square_command_factory(calculator):
    factory = SquareCommandFactory()
    square_command = factory.create_command(calculator)
    assert isinstance(square_command, SquareCommand)

# Run the tests
if __name__ == "__main__":
    pytest.main()
