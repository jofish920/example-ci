ABSOLUTE_0_IN_FAHRENHEIT = -459.67


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def convert_fahrenheit_to_celsius(fahrenheit):
    assert fahrenheit >= ABSOLUTE_0_IN_FAHRENHEIT
    return multiply(subtract(fahrenheit, 32), 5 / 9)
