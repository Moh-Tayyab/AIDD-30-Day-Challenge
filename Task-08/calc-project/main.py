from src.calculator.operations import add, subtract, multiply, divide

def main():
    print("Hello from calc-project!")
    
    # Demonstrate calculator operations
    result_add = add(10, 5)
    print(f"10 + 5 = {result_add}")
    
    result_subtract = subtract(10, 5)
    print(f"10 - 5 = {result_subtract}")
    
    result_multiply = multiply(10, 5)
    print(f"10 * 5 = {result_multiply}")
    
    result_divide = divide(10, 5)
    print(f"10 / 5 = {result_divide}")
    
    result_divide_by_zero = divide(10, 0)
    print(f"10 / 0 = {result_divide_by_zero}")


if __name__ == "__main__":
    main()
