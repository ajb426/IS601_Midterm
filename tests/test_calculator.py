import pytest
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
    assert len(calculator.get_history()) == 1

def test_subtract_method(calculator):
    assert calculator.subtract(5, 3) == 2
    assert len(calculator.get_history()) == 1

def test_multiply_method(calculator):
    assert calculator.multiply(4, 3) == 12
    assert len(calculator.get_history()) == 1

def test_divide_method(calculator):
    assert calculator.divide(8, 2) == 4
    assert len(calculator.get_history()) == 1

def test_divide_by_zero_method(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(8, 0)
    assert len(calculator.get_history()) == 0

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
