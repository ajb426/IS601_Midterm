import pytest
from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, ClearHistoryCommand, GetLastCalculationCommand
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture(autouse=True)
def setup(calculator):
    calculator.clear_history()  # Ensure history is clear before each test

# Test Calculator methods directly
def test_add_method(calculator):
    assert calculator.add(3, 2) == 5

def test_subtract_method(calculator):
    assert calculator.subtract(5, 3) == 2

def test_multiply_method(calculator):
    assert calculator.multiply(4, 3) == 12

def test_divide_method(calculator):
    assert calculator.divide(8, 2) == 4

def test_divide_by_zero_method(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(8, 0)

def test_history_method(calculator):
    calculator.add(1, 2)
    assert len(calculator.get_history()) == 1
    calculator.clear_history()
    assert len(calculator.get_history()) == 0

def test_last_calculation_method(calculator):
    calculator.add(3, 3)
    last_calc = calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc['result'] == 6

def test_save_and_load_history_method(calculator, tmpdir):
    calculator.add(1, 1)
    calculator.add(2, 2)
    file_path = tmpdir.join("history.csv")
    calculator.save_history_to_csv(file_path)
    calculator.clear_history()
    assert len(calculator.get_history()) == 0
    calculator.load_history_from_csv(file_path)
    assert len(calculator.get_history()) == 2
    last_calc = calculator.get_last_calculation()
    assert last_calc['result'] == 4

# Test command classes
def test_add_command(calculator):
    command = AddCommand(calculator)
    result = command.execute(3, 2)
    assert result == 5

def test_subtract_command(calculator):
    command = SubtractCommand(calculator)
    result = command.execute(5, 3)
    assert result == 2

def test_multiply_command(calculator):
    command = MultiplyCommand(calculator)
    result = command.execute(4, 3)
    assert result == 12

def test_divide_command(calculator):
    command = DivideCommand(calculator)
    result = command.execute(8, 2)
    assert result == 4

def test_divide_command_by_zero(calculator):
    command = DivideCommand(calculator)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(8, 0)

def test_get_history_command(calculator):
    calculator.add(1, 2)
    command = GetHistoryCommand(calculator)
    history = command.execute()
    assert len(history) == 1
    assert history.iloc[0]['result'] == 3

def test_clear_history_command(calculator):
    calculator.add(1, 2)
    command = ClearHistoryCommand(calculator)
    command.execute()
    history = calculator.get_history()
    assert len(history) == 0

def test_get_last_calculation_command(calculator):
    calculator.add(1, 2)
    command = GetLastCalculationCommand(calculator)
    last_calc = command.execute()
    assert last_calc['result'] == 3
