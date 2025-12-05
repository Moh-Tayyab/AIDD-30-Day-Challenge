# API Contracts for Basic Calculator Operations

The calculator library exposes its functionality through a set of standalone Python functions.

## Function Signatures

### `add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
-   **Description**: Adds two numbers.
-   **Parameters**:
    -   `a`: The first number (integer or float).
    -   `b`: The second number (integer or float).
-   **Returns**: The sum of `a` and `b` (integer or float).
-   **Raises**: `TypeError` if `a` or `b` are not numeric.

### `subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
-   **Description**: Subtracts the second number from the first.
-   **Parameters**:
    -   `a`: The first number (integer or float).
    -   `b`: The second number (integer or float).
-   **Returns**: The difference of `a` and `b` (integer or float).
-   **Raises**: `TypeError` if `a` or `b` are not numeric.

### `multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
-   **Description**: Multiplies two numbers.
-   **Parameters**:
    -   `a`: The first number (integer or float).
    -   `b`: The second number (integer or float).
-   **Returns**: The product of `a` and `b` (integer or float).
-   **Raises**: `TypeError` if `a` or `b` are not numeric.

### `divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float, str]`
-   **Description**: Divides the first number by the second.
-   **Parameters**:
    -   `a`: The numerator (integer or float).
    -   `b`: The denominator (integer or float).
-   **Returns**: The quotient of `a` and `b` (integer or float), or the string "Error: Division by zero" if `b` is zero.
-   **Raises**: `TypeError` if `a` or `b` are not numeric.

### `power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]`
-   **Description**: Raises the base to the power of the exponent.
-   **Parameters**:
    -   `base`: The base number (integer or float).
    -   `exponent`: The exponent (integer or float).
-   **Returns**: The result of `base` raised to the power of `exponent` (integer or float).
-   **Raises**: `TypeError` if `base` or `exponent` are not numeric.

### `modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
-   **Description**: Returns the remainder of the division of `a` by `b`.
-   **Parameters**:
    -   `a`: The dividend (integer or float).
    -   `b`: The divisor (integer or float).
-   **Returns**: The remainder of `a` divided by `b` (integer or float).
-   **Raises**: `TypeError` if `a` or `b` are not numeric. `ValueError` if `b` is zero.

### `sqrt(x: Union[int, float]) -> float`
-   **Description**: Calculates the square root of a number.
-   **Parameters**:
    -   `x`: The number (integer or float).
-   **Returns**: The square root of `x` (float).
-   **Raises**: `TypeError` if `x` is not numeric. `ValueError` if `x` is negative.

### `log(x: Union[int, float], base: Union[int, float] = 10) -> float`
-   **Description**: Calculates the logarithm of a number to a given base.
-   **Parameters**:
    -   `x`: The number (integer or float).
    -   `base`: The logarithm base (integer or float, defaults to 10).
-   **Returns**: The logarithm of `x` to the given `base` (float).
-   **Raises**: `TypeError` if `x` or `base` are not numeric. `ValueError` if `x` is non-positive or `base` is non-positive or equal to 1.

### `ln(x: Union[int, float]) -> float`
-   **Description**: Calculates the natural logarithm (base e) of a number.
-   **Parameters**:
    -   `x`: The number (integer or float).
-   **Returns**: The natural logarithm of `x` (float).
-   **Raises**: `TypeError` if `x` is not numeric. `ValueError` if `x` is non-positive.

### `sin(x: Union[int, float]) -> float`
-   **Description**: Calculates the sine of an angle (in radians).
-   **Parameters**:
    -   `x`: The angle in radians (integer or float).
-   **Returns**: The sine of `x` (float).
-   **Raises**: `TypeError` if `x` is not numeric.

### `cos(x: Union[int, float]) -> float`
-   **Description**: Calculates the cosine of an angle (in radians).
-   **Parameters**:
    -   `x`: The angle in radians (integer or float).
-   **Returns**: The cosine of `x` (float).
-   **Raises**: `TypeError` if `x` is not numeric.

### `tan(x: Union[int, float]) -> float`
-   **Description**: Calculates the tangent of an angle (in radians).
-   **Parameters**:
    -   `x`: The angle in radians (integer or float).
-   **Returns**: The tangent of `x` (float).
-   **Raises**: `TypeError` if `x` is not numeric. `ValueError` if `x` is an odd multiple of pi/2.

### `factorial(n: int) -> int`
-   **Description**: Calculates the factorial of a non-negative integer.
-   **Parameters**:
    -   `n`: The non-negative integer.
-   **Returns**: The factorial of `n` (integer).
-   **Raises**: `TypeError` if `n` is not an integer. `ValueError` if `n` is negative.
