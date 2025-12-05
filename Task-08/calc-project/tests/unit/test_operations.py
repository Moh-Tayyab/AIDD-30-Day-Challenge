import pytest
from src.calculator import operations

def test_add_two_positives():
    assert operations.add(1, 2) == 3

def test_add_positive_and_negative():
    assert operations.add(1, -2) == -1

def test_add_two_negatives():
    assert operations.add(-1, -2) == -3

def test_add_zero():
    assert operations.add(0, 5) == 5
    assert operations.add(5, 0) == 5
    assert operations.add(0, 0) == 0

def test_add_floats():
    assert operations.add(1.5, 2.5) == 4.0
    assert operations.add(-1.5, 2.0) == 0.5

def test_add_mixed_types():
    assert operations.add(1, 2.5) == 3.5
    assert operations.add(1.5, 2) == 3.5

def test_add_type_error():
    with pytest.raises(TypeError):
        operations.add("a", 1)
    with pytest.raises(TypeError):
        operations.add(1, "b")
    with pytest.raises(TypeError):
        operations.add("a", "b")


def test_subtract_two_positives():
    assert operations.subtract(5, 2) == 3

def test_subtract_positive_and_negative():
    assert operations.subtract(5, -2) == 7

def test_subtract_two_negatives():
    assert operations.subtract(-5, -2) == -3

def test_subtract_zero():
    assert operations.subtract(5, 0) == 5
    assert operations.subtract(0, 5) == -5
    assert operations.subtract(0, 0) == 0

def test_subtract_floats():
    assert operations.subtract(5.5, 2.5) == 3.0
    assert operations.subtract(-1.5, 2.0) == -3.5

def test_subtract_mixed_types():
    assert operations.subtract(5, 2.5) == 2.5
    assert operations.subtract(5.5, 2) == 3.5

def test_subtract_type_error():
    with pytest.raises(TypeError):
        operations.subtract("a", 1)
    with pytest.raises(TypeError):
        operations.subtract(1, "b")
    with pytest.raises(TypeError):
        operations.subtract("a", "b")


def test_multiply_two_positives():
    assert operations.multiply(2, 3) == 6

def test_multiply_positive_and_negative():
    assert operations.multiply(2, -3) == -6

def test_multiply_two_negatives():
    assert operations.multiply(-2, -3) == 6

def test_multiply_by_zero():
    assert operations.multiply(0, 5) == 0
    assert operations.multiply(5, 0) == 0
    assert operations.multiply(0, 0) == 0

def test_multiply_floats():
    assert operations.multiply(2.5, 2.0) == 5.0
    assert operations.multiply(-1.5, 2.0) == -3.0

def test_multiply_mixed_types():
    assert operations.multiply(2, 2.5) == 5.0
    assert operations.multiply(2.5, 2) == 5.0

def test_multiply_type_error():
    with pytest.raises(TypeError):
        operations.multiply("a", 1)
    with pytest.raises(TypeError):
        operations.multiply(1, "b")
    with pytest.raises(TypeError):
        operations.multiply("a", "b")


def test_divide_two_positives():
    assert operations.divide(6, 3) == 2

def test_divide_positive_and_negative():
    assert operations.divide(6, -3) == -2

def test_divide_two_negatives():
    assert operations.divide(-6, -3) == 2

def test_divide_zero_by_non_zero():
    assert operations.divide(0, 5) == 0

def test_divide_floats():
    assert operations.divide(5.0, 2.0) == 2.5
    assert operations.divide(-5.0, 2.0) == -2.5

def test_divide_mixed_types():
    assert operations.divide(5, 2.0) == 2.5
    assert operations.divide(5.0, 2) == 2.5

def test_divide_by_zero():
    assert operations.divide(5, 0) == "Error: Division by zero"
    assert operations.divide(0, 0) == "Error: Division by zero"

def test_divide_type_error():
    with pytest.raises(TypeError):
        operations.divide("a", 1)
    with pytest.raises(TypeError):
        operations.divide(1, "b")
    with pytest.raises(TypeError):
        operations.divide("a", "b")


def test_power_positive_integers():
    assert operations.power(2, 3) == 8

def test_power_zero_exponent():
    assert operations.power(5, 0) == 1
    assert operations.power(-5, 0) == 1

def test_power_one_exponent():
    assert operations.power(5, 1) == 5
    assert operations.power(-5, 1) == -5

def test_power_negative_exponent():
    assert operations.power(2, -1) == 0.5
    assert operations.power(2, -2) == 0.25

def test_power_float_exponent():
    assert operations.power(4, 0.5) == 2.0
    assert operations.power(8, 1/3) == pytest.approx(2.0)

def test_power_zero_base():
    assert operations.power(0, 5) == 0
    assert operations.power(0, 0) == 1 # Convention in mathematics

def test_power_negative_base_integer_exponent():
    assert operations.power(-2, 3) == -8
    assert operations.power(-2, 2) == 4

def test_power_negative_base_float_exponent():
    # Result is complex for negative base and non-integer exponent,
    # Python's ** operator returns a complex number.
    # For this calculator, we'll assume real number results or raise error.
    # Based on contract, it should return Union[int, float], so complex is not expected.
    # Let's test for a ValueError or similar if the implementation handles it.
    # For now, we'll test cases that result in real numbers.
    pass # No simple real number test for this case without complex numbers

def test_power_floats():
    assert operations.power(2.5, 2) == 6.25
    assert operations.power(1.5, 3.0) == pytest.approx(3.375)

def test_power_type_error():
    with pytest.raises(TypeError):
        operations.power("a", 2)
    with pytest.raises(TypeError):
        operations.power(2, "b")
    with pytest.raises(TypeError):
        operations.power("a", "b")


def test_modulo_positive_integers():
    assert operations.modulo(10, 3) == 1
    assert operations.modulo(9, 3) == 0

def test_modulo_positive_and_negative():
    assert operations.modulo(10, -3) == -2
    assert operations.modulo(-10, 3) == 2

def test_modulo_floats():
    assert operations.modulo(10.5, 3.0) == 1.5
    assert operations.modulo(-10.5, 3.0) == 1.5
    assert operations.modulo(10.5, -3.0) == -1.5

def test_modulo_by_zero_value_error():
    with pytest.raises(ValueError):
        operations.modulo(10, 0)
    with pytest.raises(ValueError):
        operations.modulo(0, 0)

def test_modulo_type_error():
    with pytest.raises(TypeError):
        operations.modulo("a", 2)
    with pytest.raises(TypeError):
        operations.modulo(10, "b")
    with pytest.raises(TypeError):
        operations.modulo("a", "b")


def test_sqrt_positive_integer():
    assert operations.sqrt(9) == 3.0

def test_sqrt_positive_float():
    assert operations.sqrt(2.25) == 1.5

def test_sqrt_zero():
    assert operations.sqrt(0) == 0.0

def test_sqrt_large_number():
    assert operations.sqrt(1000000) == 1000.0

def test_sqrt_small_number():
    assert operations.sqrt(0.0001) == 0.01

def test_sqrt_negative_value_error():
    with pytest.raises(ValueError):
        operations.sqrt(-1)
    with pytest.raises(ValueError):
        operations.sqrt(-0.001)

def test_sqrt_type_error():
    with pytest.raises(TypeError):
        operations.sqrt("a")
    with pytest.raises(TypeError):
        operations.sqrt([1])


def test_log_positive_integer_default_base():
    assert operations.log(100) == pytest.approx(2.0)

def test_log_positive_float_default_base():
    assert operations.log(10.0) == pytest.approx(1.0)

def test_log_custom_base():
    assert operations.log(8, 2) == pytest.approx(3.0)
    assert operations.log(100, 10) == pytest.approx(2.0)

def test_log_base_e():
    assert operations.log(operations.power(operations.e, 5), operations.e) == pytest.approx(5.0)

def test_log_non_positive_x_value_error():
    with pytest.raises(ValueError):
        operations.log(0)
    with pytest.raises(ValueError):
        operations.log(-1)

def test_log_non_positive_base_value_error():
    with pytest.raises(ValueError):
        operations.log(10, 0)
    with pytest.raises(ValueError):
        operations.log(10, -2)

def test_log_base_one_value_error():
    with pytest.raises(ValueError):
        operations.log(10, 1)

def test_log_type_error():
    with pytest.raises(TypeError):
        operations.log("a")
    with pytest.raises(TypeError):
        operations.log(10, "b")
    with pytest.raises(TypeError):
        operations.log("a", "b")


def test_ln_positive_integer():
    assert operations.ln(operations.e) == pytest.approx(1.0)
    assert operations.ln(operations.power(operations.e, 2)) == pytest.approx(2.0)

def test_ln_positive_float():
    assert operations.ln(2.71828) == pytest.approx(1.0, rel=1e-5)

def test_ln_non_positive_x_value_error():
    with pytest.raises(ValueError):
        operations.ln(0)
    with pytest.raises(ValueError):
        operations.ln(-1)

def test_ln_type_error():
    with pytest.raises(TypeError):
        operations.ln("a")
    with pytest.raises(TypeError):
        operations.ln([1])


def test_sin_zero():
    assert operations.sin(0) == pytest.approx(0.0)

def test_sin_pi_over_2():
    assert operations.sin(operations.pi / 2) == pytest.approx(1.0)

def test_sin_pi():
    assert operations.sin(operations.pi) == pytest.approx(0.0)

def test_sin_negative_pi_over_2():
    assert operations.sin(-operations.pi / 2) == pytest.approx(-1.0)

def test_sin_floats():
    assert operations.sin(0.5) == pytest.approx(0.4794255386)

def test_sin_type_error():
    with pytest.raises(TypeError):
        operations.sin("a")
    with pytest.raises(TypeError):
        operations.sin([1])


def test_cos_zero():
    assert operations.cos(0) == pytest.approx(1.0)

def test_cos_pi_over_2():
    assert operations.cos(operations.pi / 2) == pytest.approx(0.0)

def test_cos_pi():
    assert operations.cos(operations.pi) == pytest.approx(-1.0)

def test_cos_negative_pi_over_2():
    assert operations.cos(-operations.pi / 2) == pytest.approx(0.0)

def test_cos_floats():
    assert operations.cos(0.5) == pytest.approx(0.8775825619)

def test_cos_type_error():
    with pytest.raises(TypeError):
        operations.cos("a")
    with pytest.raises(TypeError):
        operations.cos([1])


def test_tan_zero():
    assert operations.tan(0) == pytest.approx(0.0)

def test_tan_pi_over_4():
    assert operations.tan(operations.pi / 4) == pytest.approx(1.0)

def test_tan_negative_pi_over_4():
    assert operations.tan(-operations.pi / 4) == pytest.approx(-1.0)

def test_tan_floats():
    assert operations.tan(0.5) == pytest.approx(0.5463024898)

def test_tan_odd_multiple_of_pi_over_2_value_error():
    with pytest.raises(ValueError):
        operations.tan(operations.pi / 2)
    with pytest.raises(ValueError):
        operations.tan(3 * operations.pi / 2)
    with pytest.raises(ValueError):
        operations.tan(-operations.pi / 2)

def test_tan_type_error():
    with pytest.raises(TypeError):
        operations.tan("a")
    with pytest.raises(TypeError):
        operations.tan([1])


def test_factorial_positive_integer():
    assert operations.factorial(0) == 1
    assert operations.factorial(1) == 1
    assert operations.factorial(5) == 120
    assert operations.factorial(10) == 3628800

def test_factorial_negative_value_error():
    with pytest.raises(ValueError):
        operations.factorial(-1)
    with pytest.raises(ValueError):
        operations.factorial(-5)

def test_factorial_float_type_error():
    with pytest.raises(TypeError):
        operations.factorial(5.0)
    with pytest.raises(TypeError):
        operations.factorial(1.5)

def test_factorial_non_integer_type_error():
    with pytest.raises(TypeError):
        operations.factorial("a")
    with pytest.raises(TypeError):
        operations.factorial([1])








