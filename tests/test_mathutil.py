from pcd_rehearsal.mathutil import add

def test_placeholder_import():
    assert callable(add)

def test_add_two_positives():
    assert add(2, 2) == 4

def test_add_zero_left():
    assert add(0, 5) == 5

def test_add_zero_right():
    assert add(7, 0) == 7

def test_add_negative_and_positive():
    assert add(-3, 5) == 2

def test_add_two_negatives():
    assert add(-4, -6) == -10

def test_add_returns_sum():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
