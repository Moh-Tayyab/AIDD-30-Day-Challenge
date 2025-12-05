import pytest
from src.calculator.evaluation import Lexer, TokenType, Token, evaluate_expression


class TestLexer:
    def test_lexer_basic_arithmetic_tokens(self):
        lexer = Lexer("12 + 34 - 5")
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        expected_tokens = [
            Token(TokenType.NUMBER, 12.0),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 34.0),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 5.0),
            Token(TokenType.EOF),
        ]
        assert tokens == expected_tokens

    def test_lexer_handles_whitespace(self):
        lexer = Lexer("  10   +   20  ")
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        expected_tokens = [
            Token(TokenType.NUMBER, 10.0),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 20.0),
            Token(TokenType.EOF),
        ]
        assert tokens == expected_tokens

    def test_lexer_floating_point_numbers(self):
        lexer = Lexer("12.5 + 0.5")
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        expected_tokens = [
            Token(TokenType.NUMBER, 12.5),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 0.5),
            Token(TokenType.EOF),
        ]
        assert tokens == expected_tokens

    def test_lexer_multiplication_division(self):
        lexer = Lexer("10 * 2 / 5")
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        expected_tokens = [
            Token(TokenType.NUMBER, 10.0),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2.0),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 5.0),
            Token(TokenType.EOF),
        ]
        assert tokens == expected_tokens

    def test_lexer_parentheses(self):
        lexer = Lexer("(1 + 2) * 3")
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        expected_tokens = [
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 1.0),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 2.0),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 3.0),
            Token(TokenType.EOF),
        ]
        assert tokens == expected_tokens

    def test_lexer_invalid_character(self):
        with pytest.raises(ValueError, match=r"Invalid character: '#'"):
            lexer = Lexer("1 + #")
            while True:
                token = lexer.get_next_token()
                if token.type == TokenType.EOF:
                    break

    def test_lexer_invalid_character_in_number(self):
        with pytest.raises(
            ValueError, match="Invalid character in number literal."
        ):
            lexer = Lexer("123a + 45")
            while True:
                token = lexer.get_next_token()
                if token.type == TokenType.EOF:
                    break


class TestEvaluator:
    @pytest.mark.parametrize(
        "expression, expected_result",
        [
            ("10 * 2", 20.0),
            ("10 / 2", 5.0),
            ("2 * 3 * 4", 24.0),
            ("20 / 4 / 2", 2.5),
            ("10 * 2 / 4", 5.0),
            ("5 / 2 * 4", 10.0),  # Left-to-right associativity
        ],
    )
    def test_multiplication_division(self, expression, expected_result):
        assert evaluate_expression(expression) == expected_result

    @pytest.mark.parametrize(
        "expression, expected_result",
        [
            ("10 + 5", 15.0),
            ("10 - 5", 5.0),
            ("1 + 2 + 3", 6.0),
            ("10 - 2 - 3", 5.0),
            ("10 + 5 - 2", 13.0),
            ("5 - 10 + 2", -3.0),  # Left-to-right associativity
        ],
    )
    def test_addition_subtraction(self, expression, expected_result):
        assert evaluate_expression(expression) == expected_result

    @pytest.mark.parametrize(
        "expression, expected_result",
        [
            ("10 + 2 * 3", 16.0),  # Multiplication before addition
            ("10 - 6 / 2", 7.0),  # Division before subtraction
            ("2 * 3 + 4 * 5", 26.0),  # Multiple operations
            ("20 / 4 + 1", 6.0),
            ("1 + 2 * 3 - 4 / 2", 5.0),  # Mixed operations with precedence
        ],
    )
    def test_order_of_operations(self, expression, expected_result):
        assert evaluate_expression(expression) == expected_result

    @pytest.mark.parametrize(
        "expression, error_message",
        [
            (
                "1 + (",
                "Expected NUMBER or LPAREN, got EOF instead.",
            ),  # Mismatched parentheses
            (
                "1 + / 2",
                "Expected NUMBER or LPAREN, got DIVIDE instead.",
            ),  # Operator at wrong position
            (
                "1 +",
                "Expected NUMBER or LPAREN, got EOF instead.",
            ),  # Incomplete expression
            ("", "Expected NUMBER or LPAREN, got EOF instead."),  # Empty string
            (
                "(1 + 2",
                "Expected RPAREN, got EOF instead.",
            ),  # Missing RPAREN (this one should still match)
            (
                "1 2 + 3",
                "Unexpected token at end of expression.",
            ),  # Missing operator - the parser successfully parses '1', then in 'parse', it finds that '2 + 3' remains, leading to this error.
        ],
    )
    def test_invalid_syntax_errors(self, expression, error_message):
        with pytest.raises(ValueError, match=error_message):
            evaluate_expression(expression)

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Division by zero error."):
            evaluate_expression("10 / 0")
        with pytest.raises(ZeroDivisionError, match="Division by zero error."):
            evaluate_expression("10 / (5 - 5)")
