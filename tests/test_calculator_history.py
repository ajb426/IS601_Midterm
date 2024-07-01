import pytest
import pandas as pd
import os
from calculator.calculation import Calculation
from calculator.calculator_history import CalculatorHistory

@pytest.fixture
def history():
    return CalculatorHistory(file_path='test_history.csv')

def test_load_from_csv_empty_file(history):
    if os.path.exists(history.file_path):
        os.remove(history.file_path)
    history.load_from_csv()
    assert history.df.empty

def test_load_from_csv_with_data(history):
    data = pd.DataFrame({
        'operation': ['+', '-', '*', '/'],
        'operand1': [1, 2, 3, 4],
        'operand2': [5, 6, 7, 8],
        'result': [6, -4, 21, 0.5]
    })
    data.to_csv(history.file_path, index=False)
    history.load_from_csv()
    pd.testing.assert_frame_equal(history.df, data)

def test_save_to_csv(history):
    data = pd.DataFrame({
        'operation': ['+', '-'],
        'operand1': [1, 2],
        'operand2': [3, 4],
        'result': [4, -2]
    })
    history.df = data
    history.save_to_csv()
    loaded_data = pd.read_csv(history.file_path)
    pd.testing.assert_frame_equal(loaded_data, data)

def test_add_record(history):
    calculation = Calculation('+', 1, 2, 3)
    history.add_record(calculation)
    assert len(history.df) == 1
    assert history.df.iloc[0]['operation'] == '+'
    assert history.df.iloc[0]['operand1'] == 1
    assert history.df.iloc[0]['operand2'] == 2
    assert history.df.iloc[0]['result'] == 3

def test_clear_history(history):
    calculation = Calculation('*', 3, 3, 9)
    history.add_record(calculation)
    assert not history.df.empty
    history.clear_history()
    assert history.df.empty

def test_get_last_record(history):
    calculation1 = Calculation('-', 5, 2, 3)
    calculation2 = Calculation('/', 9, 3, 3)
    history.add_record(calculation1)
    history.add_record(calculation2)
    last_record = history.get_last_record()
    assert last_record.operation == '/'
    assert last_record.operand1 == 9
    assert last_record.operand2 == 3
    assert last_record.result == 3

def test_get_last_record_empty(history):
    last_record = history.get_last_record()
    assert last_record is None

def test_get_all_records(history):
    calculation1 = Calculation('+', 1, 2, 3)
    calculation2 = Calculation('*', 2, 2, 4)
    history.add_record(calculation1)
    history.add_record(calculation2)
    all_records = history.get_all_records()
    assert len(all_records) == 2

def test_set_file_path(history):
    new_path = 'new_history.csv'
    history.set_file_path(new_path)
    assert history.file_path == new_path

@pytest.fixture(autouse=True)
def cleanup():
    yield
    if os.path.exists('test_history.csv'):
        os.remove('test_history.csv')
    if os.path.exists('new_history.csv'):
        os.remove('new_history.csv')

# Run the tests
if __name__ == "__main__":
    pytest.main()
