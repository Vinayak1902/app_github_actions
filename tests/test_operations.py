from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,2) == 1

def test_sub():
    assert sub(5,2) == 3
    assert sub(3,-9) == 12
    assert sub(2,7) == -5
    
