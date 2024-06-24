import pytest
from calculator.repl import CalculatorREPL
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def setup():
    Calculator.clear_history()  # Ensure history is clear before each test

def test_repl_start(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the initial greeting is printed
    assert "Calculator REPL. Type 'exit' to quit." in out

def test_repl_add_command(capfd, monkeypatch):
    """Test the REPL add command."""
    inputs = iter(['add 3 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the add command works and the REPL exits gracefully
    assert "Result: 7.0" in out

def test_repl_subtract_command(capfd, monkeypatch):
    """Test the REPL subtract command."""
    inputs = iter(['subtract 10 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the subtract command works and the REPL exits gracefully
    assert "Result: 6.0" in out

def test_repl_multiply_command(capfd, monkeypatch):
    """Test the REPL multiply command."""
    inputs = iter(['multiply 3 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the multiply command works and the REPL exits gracefully
    assert "Result: 12.0" in out

def test_repl_divide_command(capfd, monkeypatch):
    """Test the REPL divide command."""
    inputs = iter(['divide 12 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the divide command works and the REPL exits gracefully
    assert "Result: 3.0" in out

def test_repl_divide_by_zero(capfd, monkeypatch):
    """Test division by zero in the REPL."""
    inputs = iter(['divide 12 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the REPL handles division by zero
    assert "Error: Cannot divide by zero" in out

def test_repl_history_command(capfd, monkeypatch):
    """Test the REPL history command."""
    inputs = iter(['add 1 2', 'history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()

    # Check that the history command works
    assert "Result: 3.0" in out
    assert "1.0 + 2.0 = 3.0" in out

def test_repl_clear_history_command(capfd, monkeypatch):
    """Test the REPL clear_history command."""
    inputs = iter(['add 1 2', 'clear_history', 'history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the clear_history command works
    assert "Result: 3.0" in out
    assert "" in out

def test_repl_last_command(capfd, monkeypatch):
    """Test the REPL last command."""
    inputs = iter(['add 1 2', 'last', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    
    # Check that the last command works
    assert "Result: 3.0" in out
    assert "Result: 1.0 + 2.0 = 3.0" in out

def test_unknown_command(capfd, monkeypatch):
    """Test unknown command scenario."""
    inputs = iter(['addition 1 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()

    assert "Unknown command" in out

def test_repl_empty_input(capfd, monkeypatch):
    """Test the REPL handling of empty input."""
    inputs = iter(["", 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    print(out)
    # Check that the REPL handles empty input by continuing the loop
    assert "Calculator REPL. Type 'exit' to quit." in out

def test_repl_type_error(capfd, monkeypatch):
    """Test the REPL handling of TypeError."""
    inputs = iter(['add 3 four', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    repl = CalculatorREPL()
    repl.start()
    out, err = capfd.readouterr()
    assert "Error: could not convert string to float: 'four'" in out
