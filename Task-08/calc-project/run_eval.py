from src.calculator.evaluation import evaluate_expression

if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter an expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break
            if not expression:
                continue

            result = evaluate_expression(expression)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
