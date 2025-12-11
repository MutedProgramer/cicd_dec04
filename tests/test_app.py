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
    assert sub(-5,6) == -11
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

#testing for advanced
def test_log():
    assert math.isclose(log(10),1, rel_tol=1e-9)
    assert math.isclose(log(math.e, math.e), 1, rel_tol=1e-9)
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-6)

def test_square():
    assert square(5) == 25
    assert square(-4) == 16
    assert square(0) == 0

def test_squareroot():
    assert squareroot(16) == 4
    assert squareroot(0) == 0
    assert squareroot(36) != 7
    with pytest.raises(ValueError):
        squareroot(-4)

def test_sin():
    assert sin(math.pi/2) == 1
    assert sin(0) == 0
    assert sin(math.pi) == 0
    assert sin(3*math.pi/2) == -1


def test_cos():
    assert cos(0) == 1
    assert cos(math.pi/2) == 0
    assert cos(math.pi) == -1
    assert cos(2*math.pi) == 1

def test_percentage():
    assert percentage(50) == 0.5
    assert percentage(-78) == -0.78
    assert percentage(0) == 0