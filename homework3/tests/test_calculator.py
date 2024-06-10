
'''My Calculator Test'''
from calculator import add, subtract, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_divide_normal_case():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == "Error: Division by zero is not allowed."