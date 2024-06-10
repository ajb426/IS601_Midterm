@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 15),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert Calculator.add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 5),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract(x, y, expected):
    assert Calculator.subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 50),
    (-1, -1, 1),
    (0, 5, 0),
])
def test_multiply(x, y, expected):
    assert Calculator.multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 2.0),
    (-10, -5, 2.0),
    (0, 5, 0.0),
])
def test_divide(x, y, expected):
    assert Calculator.divide(x, y) == expected

def test_divide_by_zero():
    assert Calculator.divide(10, 0) == "Error: Division by zero is not allowed."

def test_history():
    Calculator.clear_history()
    Calculator.add(1, 1)
    Calculator.subtract(2, 1)
    assert len(Calculator.get_history()) == 2
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0

def test_last_calculation():
    Calculator.clear_history()
    Calculator.add(3, 3)
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.result == 6