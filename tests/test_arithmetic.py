import pytest
from hatchproject.arithmetic import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 5) == -4
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)