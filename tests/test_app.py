import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import math
import pytest
from app import add, sub, multiply, division, log, square, squareroot, sin, cos, percentage

def test_add():
    assert add(5, 6) == 11
    assert add(-3, 3) == 0

def test_sub():
    assert sub(10,5) == 5
    assert sub(-5,-6) == -11
    assert sub(0,0) == 0
def test_multiply():
    assert multiply(6,7) == 42
    assert multiply(0,420) == 0
    assert multiply(-3,-5) == 15

def test_division():
    assert division(9,3) == 3
    assert division (0,10) == 0
    with pytest.raises(ValueError):
        division(5,0) #dividing by zero
