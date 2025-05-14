"""module docstring"""


def add(a: int, b: int) -> int:
    """Return sum of a b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return diff of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return multiply of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return diff? of a divided by b."""
    return a / b


def float_to_binary(x):
    """convert to float x with base m"""
    m = 5
    n = 5
    if not 0 <= x <= 100:
        raise ValueError("out of range range.")
    x_scaled = round(x * 2**n)
    return f"{x_scaled:0{m + n}b}"
