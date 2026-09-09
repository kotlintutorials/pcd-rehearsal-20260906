from pcd_rehearsal.mathutil import add

def test_placeholder_import():
    assert callable(add)


def test_add_returns_sum():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
