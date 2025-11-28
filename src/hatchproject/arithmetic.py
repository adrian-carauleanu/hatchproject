from typing import TypeVar, Union

T = TypeVar("T", int, float, complex)

def add(a: T, b: T) -> T:
    """Returns the sum of a and b."""
    return a + b

def subtract(a: T, b: T) -> T:
    """Returns the difference of a and b."""
    return a - b

def multiply(a: T, b: T) -> T:
    """Returns the product of a and b."""
    return a * b

def divide(a: T, b: T) -> Union[float, complex]:
    """
    Returns the quotient of a and b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b