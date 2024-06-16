import pytest
from calculator.command import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, ClearHistoryCommand, GetLastCalculationCommand
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def setup():
    Calculator.clear_history()  # Ensure history is clear before each test

def test_command_base_class():
    command = Command()
    result = command.execute(1, 2)  # Call execute on base class
    assert result is None  # Expecting None since it's not implemented

def test_add_command():
    command = AddCommand()
    result = command.execute(3, 2)
    assert result == 5

def test_subtract_command():
    command = SubtractCommand()
    result = command.execute(5, 3)
    assert result == 2

def test_multiply_command():
    command = MultiplyCommand()
    result = command.execute(4, 3)
    assert result == 12

def test_divide_command():
    command = DivideCommand()
    result = command.execute(8, 2)
    assert result == 4

def test_divide_command_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(8, 0)

def test_get_history_command():
    Calculator.add(1, 2)
    command = GetHistoryCommand()
    history = command.execute()
    assert len(history) == 1
    assert history[0].result == 3

def test_clear_history_command():
    Calculator.add(1, 2)
    command = ClearHistoryCommand()
    command.execute()
    history = Calculator.get_history()
    assert len(history) == 0

def test_get_last_calculation_command():
    Calculator.add(1, 2)
    command = GetLastCalculationCommand()
    last_calc = command.execute()
    assert last_calc.result == 3
