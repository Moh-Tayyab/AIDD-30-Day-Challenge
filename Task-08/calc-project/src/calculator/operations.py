"""
This module provides basic arithmetic operations for the calculator.
"""

import math
from typing import Union

e = math.e
pi = math.pi


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float).
    """

    if (
        not isinstance(a, (int, float)) or
        not isinstance(b, (int, float))
    ):
        raise TypeError("Both arguments must be numeric (int or float).")
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts the second number from the first.

    Args:
        a: The number to be subtracted from (integer or float).
        b: The number to subtract (integer or float).
    """
    if (
        not isinstance(a, (int, float)) or
        not isinstance(b, (int, float))
    ):
        raise TypeError("Both arguments must be numeric (int or float).")
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float).

    Returns:
        The product of a and b (integer or float).

    Raises:
        TypeError: If a or b are not numeric.
    """
    if (
        not isinstance(a, (int, float)) or
        not isinstance(b, (int, float))
    ):
        raise TypeError("Both arguments must be numeric (int or float).")
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float, str]:
    """
    Divides the first number by the second.

    Args:
        a: The numerator (integer or float).
        b: The denominator (integer or float).

    Returns:
        The quotient of a and b (integer or float), or the string "Error: Division by zero" if b is zero.

    Raises:
        TypeError: If a or b are not numeric.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float).")
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Raises a number to the power of an exponent.

    Args:
        base: The base number (integer or float).
        exponent: The exponent (integer or float).

    Returns:
        The result of base raised to the power of exponent (integer or float).

    Raises:
        TypeError: If base or exponent are not numeric.
    """
    if (not isinstance(base, (int, float)) or
            not isinstance(exponent, (int, float))):
        raise TypeError("Both arguments must be numeric (int or float).")
    return base ** exponent


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculates the remainder of the division of a by b.

    Args:
        a: The dividend (integer or float).
        b: The divisor (integer or float).

    Returns:
        The remainder of the division (integer or float).

    Raises:
        TypeError: If a or b are not numeric.
        ValueError: If the divisor b is zero.
    """
    if (not isinstance(a, (int, float)) or
            not isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numeric (int or float).")
    if b == 0:
        raise ValueError("Cannot perform modulo operation with zero divisor.")
    return a % b


def sqrt(x: Union[int, float]) -> float:
    """
    Calculates the square root of a number.

    Args:
        x: The number (integer or float).

    Returns:
        The square root of x (float).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is negative.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument must be numeric (int or float).")
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(x)


def log(x: Union[int, float], base: Union[int, float] = 10) -> float:
    """
    Calculates the logarithm of a number to a given base.

    Args:
        x: The number (integer or float).
        base: The logarithm base (integer or float, defaults to 10).

    Returns:
        The logarithm of x to the given base (float).

    Raises:
        TypeError: If x or base are not numeric.
        ValueError: If x is non-positive or base is non-positive or equal to 1.
    """
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float).")
    if x <= 0:
        raise ValueError("Logarithm of non-positive number is undefined.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(x, base)


def ln(x: Union[int, float]) -> float:
    """
    Calculates the natural logarithm (base e) of a number.

    Args:
        x: The number (integer or float).

    Returns:
        The natural logarithm of x (float).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is non-positive.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument must be numeric (int or float).")
    if x <= 0:
        raise ValueError("Natural logarithm of non-positive number is undefined.")
    return math.log(x)


def sin(x: Union[int, float]) -> float:
    """
    Calculates the sine of an angle (in radians).

    Args:
        x: The angle in radians (integer or float).

    Returns:
        The sine of x (float).

    Raises:
        TypeError: If x is not numeric.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument must be numeric (int or float).")
    return math.sin(x)


def cos(x: Union[int, float]) -> float:
    """
    Calculates the cosine of an angle (in radians).

    Args:
        x: The angle in radians (integer or float).

    Returns:
        The cosine of x (float).

    Raises:
        TypeError: If x is not numeric.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument must be numeric (int or float).")
    return math.cos(x)


def tan(x: Union[int, float]) -> float:
    """
    Calculates the tangent of an angle (in radians).

    Args:
        x: The angle in radians (integer or float).

    Returns:
        The tangent of x (float).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is an odd multiple of pi/2.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument must be numeric (int or float).")
    # Check for odd multiples of pi/2 where tan is undefined
    # Using a small epsilon for float comparison
    if (abs(x - pi / 2) < 1e-9 or abs(x + pi / 2) < 1e-9 or
            abs(x - 3 * pi / 2) < 1e-9 or abs(x + 3 * pi / 2) < 1e-9):
        raise ValueError("Tangent is undefined for odd multiples of pi/2.")
    return math.tan(x)


def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n (integer).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)