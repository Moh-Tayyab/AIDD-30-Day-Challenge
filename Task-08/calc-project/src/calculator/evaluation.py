import enum
from dataclasses import dataclass


class TokenType(enum.Enum):
    """Enum for different types of tokens."""

    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    EOF = "EOF"  # End Of File/Expression


@dataclass
class Token:
    """Represents a lexical token with its type and optional value."""

    type: TokenType
    value: any = None

    def __repr__(self):
        return f"Token({self.type.name}{f': {self.value}' if self.value is not None else ''})"


class Lexer:
    """
    Breaks an input string into a stream of tokens.
    """

    def __init__(self, text: str):
        """
        Initializes the Lexer with the input text.

        Args:
            text: The input string to tokenize.
        """
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if len(self.text) > 0 else None

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self) -> Token:
        """Return a (multi-digit) integer or float consumed from the input."""
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == ".":
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()

        # Ensure that the number is not followed by an invalid character (e.g., "123a")
        if self.current_char is not None and self.current_char.isalpha():
            raise ValueError("Invalid character in number literal.")

        return Token(TokenType.NUMBER, float(result))

    def get_next_token(self) -> Token:
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence apart into tokens.
        One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS)
            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS)
            if self.current_char == "*":
                self.advance()
                return Token(TokenType.MULTIPLY)
            if self.current_char == "/":
                self.advance()
                return Token(TokenType.DIVIDE)
            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN)
            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN)

            # Handle invalid characters
            raise ValueError(f"Invalid character: '{self.current_char}'")

        return Token(TokenType.EOF)


# AST Node Classes
class AST:
    """Base class for all Abstract Syntax Tree nodes."""

    pass


@dataclass
class Number(AST):
    """Represents a number literal in the AST."""

    token: Token
    value: float


@dataclass
class BinOp(AST):
    """Represents a binary operation in the AST (e.g., 1 + 2)."""

    left: AST
    op: Token
    right: AST


@dataclass
class UnaryOp(AST):
    """Represents a unary operation in the AST (e.g., -1)."""

    op: Token
    right: AST


class Parser:
    """
    Parses a stream of tokens to build an Abstract Syntax Tree (AST).
    Implements a recursive descent parser for arithmetic expressions.
    """

    def __init__(self, lexer: Lexer):
        """
        Initializes the Parser with a lexer instance.

        Args:
            lexer: The lexer to provide tokens.
        """
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message="Invalid syntax"):
        """Raises a ValueError for syntax errors."""
        raise ValueError(message)

    def eat(self, token_type: TokenType):
        """Consumes a token if its type matches the expected type."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(
                f"Expected {token_type.name}, got {self.current_token.type.name} instead."
            )

    def factor(self) -> AST:
        """
        Parses a factor in the expression: NUMBER or (EXPR).

        Returns:
            An AST node representing the factor.
        """
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(token, token.value)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        else:
            self.error(
                f"Expected NUMBER or LPAREN, got {self.current_token.type.name} instead."
            )

    def term(self) -> AST:
        """
        Parses a term in the expression: factor ((MUL | DIV) factor)*.

        Returns:
            An AST node representing the term.
        """
        node = self.factor()

        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            elif token.type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)

            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self) -> AST:
        """
        Parses an expression: term ((PLUS | MINUS) term)*.

        Returns:
            An AST node representing the expression.
        """
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinOp(left=node, op=token, right=self.term())
        return node

    def parse(self) -> AST:
        """
        Parses the entire expression and builds the AST.

        Returns:
            The root AST node.
        """
        node = self.expr()
        if self.current_token.type != TokenType.EOF:
            self.error("Unexpected token at end of expression.")
        return node


class Interpreter:
    """
    Traverses the Abstract Syntax Tree (AST) to evaluate the expression.
    """

    def visit(self, node: AST):
        """Dispatches to the appropriate visit method based on the node type."""
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Fallback for unknown AST node types."""
        raise Exception(f"No visit_{type(node).__name__} method")

    def visit_Number(self, node: Number):
        """Visits a Number node and returns its value."""
        return node.value

    def visit_BinOp(self, node: BinOp):
        """Visits a BinOp node, evaluates its children, and applies the operation."""
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == TokenType.MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == TokenType.DIVIDE:
            # Handle division by zero
            right_val = self.visit(node.right)
            if right_val == 0:
                raise ZeroDivisionError("Division by zero error.")
            return self.visit(node.left) / right_val

    def interpret(self, node: AST):
        """
        Starts the interpretation process from the given AST node.

        Args:
            node: The root AST node to interpret.

        Returns:
            The numerical result of the expression.
        """
        return self.visit(node)


def evaluate_expression(expression: str) -> float:
    """
    Evaluates a mathematical expression string.

    Args:
        expression: The string containing the mathematical expression.

    Returns:
        The numerical result of the expression.

    Raises:
        ValueError: If the expression has a syntax error or invalid characters.
        ZeroDivisionError: If the expression involves division by zero.
    """
    lexer = Lexer(expression)
    parser = Parser(lexer)
    interpreter = Interpreter()
    tree = parser.parse()
    result = interpreter.interpret(tree)
    return result
