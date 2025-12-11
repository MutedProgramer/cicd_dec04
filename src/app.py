import math
def add (a, b):
    return a+b

def sub (a, b):
    return a-b
def multiply (a,b):
    return a*b
def division (a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
#advance operations

def log (a, b=10):
    if a <= 0:
        raise ValueError("A must be greater than 0")
    return math.log(a, b)

def square(a):
    return a**2

def squareroot(a):
    if a < 0:
        raise ValueError("A must be greater than 0")
    return math.sqrt(a)

def sin(a):
    return round(math.sin(a), 10)

def cos(a):
    return round(math.cos(a), 10)

def percentage(a):
    return a / 100