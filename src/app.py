import math
def add (a, b):
    return a+b

def sub (a, b):
    return a-b
def multiply (a,b):
    return a*b
def division (a,b):
    if b == 0:
        return ValueError("Cannot divide by zero")
    return a/b
#advance operations

def log (a, b):
    if a <= 0:
        return ValueError("A must be greater than 0")
    return math.log(a, base)

def square(a):
    return a**2

def squareroot(a):
    if a < 0:
        raise ValueError("A must be greater than 0")
    return math.sqrt(a)

def sin(a):
    math.sin(a)

def cos(a):
    return math.cos(a)

def perecentage(a):
    return a / 100