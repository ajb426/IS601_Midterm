import pytest
import os
from calculator.calculator import Calculator
from calculator.plugins.default_commands import (
    AddCommand, AddCommandFactory,
    SubtractCommand, SubtractCommandFactory,
    MultiplyCommand, MultiplyCommandFactory,
    DivideCommand, DivideCommandFactory,
    HistoryCommand, HistoryCommandFactory,
    ClearHistoryCommand, ClearHistoryCommandFactory,
    GetLastCalculationCommand, GetLastCalculationCommandFactory,
    SaveHistoryCommand, SaveHistoryCommandFactory,
    LoadHistoryCommand, LoadHistoryCommandFactory
)

@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture(autouse=True)
def setup(calculator):
    calculator.clear_history()

def test_add_command(calculator):
    command = AddCommand(calculator)
    result = command.execute(3, 2)
    assert result == 5

def test_add_command_factory(calculator):
    factory = AddCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, AddCommand)

def test_subtract_command(calculator):
    command = SubtractCommand(calculator)
    result = command.execute(5, 3)
    assert result == 2

def test_subtract_command_factory(calculator):
    factory = SubtractCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, SubtractCommand)

def test_multiply_command(calculator):
    command = MultiplyCommand(calculator)
    result = command.execute(4, 3)
    assert result == 12

def test_multiply_command_factory(calculator):
    factory = MultiplyCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, MultiplyCommand)

def test_divide_command(calculator):
    command = DivideCommand(calculator)
    result = command.execute(8, 2)
    assert result == 4

def test_divide_command_by_zero(calculator):
    command = DivideCommand(calculator)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(8, 0)

def test_divide_command_factory(calculator):
    factory = DivideCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, DivideCommand)

def test_history_command(calculator):
    calculator.add(1, 2)
    command = HistoryCommand(calculator)
    history = command.execute()
    assert len(history) == 1
    assert history.iloc[0]['result'] == 3

def test_history_command_factory(calculator):
    factory = HistoryCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, HistoryCommand)

def test_clear_history_command(calculator):
    calculator.add(1, 2)
    command = ClearHistoryCommand(calculator)
    command.execute()
    history = calculator.get_history()
    assert len(history) == 0

def test_clear_history_command_factory(calculator):
    factory = ClearHistoryCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, ClearHistoryCommand)

def test_get_last_calculation_command(calculator):
    calculator.add(1, 2)
    command = GetLastCalculationCommand(calculator)
    last_calc = command.execute()
    assert last_calc['result'] == 3

def test_get_last_calculation_command_factory(calculator):
    factory = GetLastCalculationCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, GetLastCalculationCommand)

def test_save_history_command(calculator, tmpdir):
    calculator.add(1, 1)
    file_path = tmpdir.join("history.csv")
    command = SaveHistoryCommand(calculator)
    command.execute(file_path)
    assert os.path.exists(file_path)

def test_save_history_command_factory(calculator):
    factory = SaveHistoryCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, SaveHistoryCommand)

def test_load_history_command(calculator, tmpdir):
    calculator.add(1, 1)
    file_path = tmpdir.join("history.csv")
    calculator.save_history_to_csv(file_path)
    calculator.clear_history()
    command = LoadHistoryCommand(calculator)
    command.execute(file_path)
    assert len(calculator.get_history()) == 1
    assert calculator.get_last_calculation()['result'] == 2

def test_load_history_command_factory(calculator):
    factory = LoadHistoryCommandFactory()
    command = factory.create_command(calculator)
    assert isinstance(command, LoadHistoryCommand)

# Run the tests
if __name__ == "__main__":
    pytest.main()
