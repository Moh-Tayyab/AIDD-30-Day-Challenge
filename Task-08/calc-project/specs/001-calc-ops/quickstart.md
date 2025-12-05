# Quickstart: Basic Calculator Operations Library

This guide provides a quick overview of how to install and use the Basic Calculator Operations library.

## Installation

To install the library, use `uv` (or `pip`):

```bash
uv add calculator-library # (replace with actual package name)
```

## Usage

Here are some basic examples of how to use the calculator functions:

```python
from calculator import operations # (replace with actual module structure)

# Addition
result_add = operations.add(10, 5)
print(f"10 + 5 = {result_add}") # Expected: 15

result_decimal_add = operations.add(2.5, 1.3)
print(f"2.5 + 1.3 = {result_decimal_add}") # Expected: 3.8

# Subtraction
result_sub = operations.subtract(10, 5)
print(f"10 - 5 = {result_sub}") # Expected: 5

# Multiplication
result_mul = operations.multiply(4, 3)
print(f"4 * 3 = {result_mul}") # Expected: 12

# Division
result_div = operations.divide(10, 2)
print(f"10 / 2 = {result_div}") # Expected: 5.0

# Division by Zero
error_div_zero = operations.divide(10, 0)
print(f"10 / 0 = {error_div_zero}") # Expected: Error: Division by zero

# Exponentiation
result_pow = operations.power(2, 3)
print(f"2 ** 3 = {result_pow}") # Expected: 8

# Square Root
result_sqrt = operations.sqrt(25)
print(f"sqrt(25) = {result_sqrt}") # Expected: 5.0

# Natural Logarithm
result_ln = operations.ln(2.71828)
print(f"ln(2.71828) = {result_ln}") # Expected: ~1.0

# Sine
result_sin = operations.sin(0)
print(f"sin(0) = {result_sin}") # Expected: 0.0
```
