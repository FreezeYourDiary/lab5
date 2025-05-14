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
    m = 5
    n = 5
    """convert float x, with base m .
    """
    if not (0 <= x <= 100):
        raise ValueError("out of range range.")
    x_scaled = round(x * 2 ** n)
    return '{:0{}b}'.format(x_scaled, m + n)
if __name__ == '__main__':
    print(float_to_binary(5))