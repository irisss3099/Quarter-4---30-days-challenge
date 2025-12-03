import math

def sine(angle_degrees):
    return math.sin(math.radians(angle_degrees))

def cosine(angle_degrees):
    return math.cos(math.radians(angle_degrees))

def tangent(angle_degrees):
    # Handle tangent for angles where cosine is zero (e.g., 90, 270 degrees)
    if abs(math.cos(math.radians(angle_degrees))) < 1e-9:
        raise ValueError("Tangent undefined for this angle")
    return math.tan(math.radians(angle_degrees))

def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)

def logarithm(number, base=10):
    if number <= 0:
        raise ValueError("Logarithm is defined only for positive numbers")
    return math.log(number, base)

def power(base, exponent):
    return math.pow(base, exponent)
