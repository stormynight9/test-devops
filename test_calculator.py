import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(5, 5) == 0
    assert calculator.subtract(10, -3) == 13

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5, 0) == 0
    assert calculator.multiply(-4, 3) == -12

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 1) == 5
    assert calculator.divide(8, 4) == 2

def test_divide_by_zero():
    try:
        calculator.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
