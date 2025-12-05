"""
Utility functions for the calculator.
"""

import math





def is_close(




    a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 0.0
) -> bool:
    """
    Determine whether two float values are close to each other.

    This function is a wrapper around math.isclose, providing a convenient
    way to compare floats with a configurable relative and absolute tolerance.

    Args:
        a: The first float value.
        b: The second float value.
        rel_tol: The relative tolerance. It is the maximum allowed difference
                                                   between a and b, relative to the larger absolute value of
                                                   a or b.                 For example, to check for 1% tolerance, use rel_tol=0.01.
        abs_tol: The absolute tolerance. It is the maximum allowed difference
                 between a and b, regardless of their magnitude. Useful for
                 comparisons near zero.

    Returns:
        True if a and b are considered close, False otherwise.
    """
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
