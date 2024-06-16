import pytest
from unittest.mock import patch, MagicMock
from calculator.repl import CalculatorREPL
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def setup():
    Calculator.clear_history()  # Ensure history is clear before each test

def mock_input(inputs):
    """
    Creates a generator function to mock the input() function.
    """
    def inner(prompt=""):
        print(f"Prompt: {prompt}")  # Debug print for prompt
        return next(inputs)
    return inner

def test_repl_add_command():
    user_inputs = iter(['add 3 4', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        print("Starting REPL...")  # Debug print for REPL start
        repl.start()
        print("REPL exited.")  # Debug print for REPL exit
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Available commands:")
        mock_print.assert_any_call(" - add")
        mock_print.assert_any_call(" - subtract")
        mock_print.assert_any_call(" - multiply")
        mock_print.assert_any_call(" - divide")
        mock_print.assert_any_call(" - history")
        mock_print.assert_any_call(" - clear_history")
        mock_print.assert_any_call(" - last")
        mock_print.assert_any_call(" - menu")
        mock_print.assert_any_call("Calculator REPL. Type 'exit' to quit.")
        mock_print.assert_any_call("Result: 7.0")

def test_repl_subtract_command():
    user_inputs = iter(['subtract 10 4', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Result: 6.0")

def test_repl_multiply_command():
    user_inputs = iter(['multiply 3 4', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Result: 12.0")

def test_repl_divide_command():
    user_inputs = iter(['divide 12 4', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Result: 3.0")

def test_repl_divide_by_zero():
    user_inputs = iter(['divide 12 0', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Error: Cannot divide by zero")

def test_repl_history_command():
    user_inputs = iter(['add 1 2', 'history', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Result: 3.0")
        mock_print.assert_any_call("1 + 2 = 3.0")

def test_repl_clear_history_command():
    user_inputs = iter(['add 1 2', 'clear_history', 'history', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Result: 3.0")
        mock_print.assert_any_call("History cleared.")
        mock_print.assert_any_call([])

def test_repl_last_command():
    user_inputs = iter(['add 1 2', 'last', 'exit'])
    with patch('builtins.input', new=mock_input(user_inputs)), patch('builtins.print') as mock_print:
        repl = CalculatorREPL()
        repl.start()
        
        # Print all calls to print for debugging
        for call in mock_print.mock_calls:
            print(call)
        
        # Check the calls to print
        mock_print.assert_any_call("Result: 3.0")
        mock_print.assert_any_call("1 + 2 = 3.0")
