"""Small arithmetic engine: parse an allowlisted expression without eval()."""

import ast
import math
import operator

MAX_LENGTH = 128
MAX_DEPTH = 16
MAX_MAGNITUDE = 1_000_000_000_000
OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


class CalculationError(ValueError):
    """An expression is invalid, unsupported, or outside calculator limits."""


def _checked(value):
    if type(value) not in (int, float):
        raise CalculationError("Use numbers only.")
    if not math.isfinite(value) or abs(value) > MAX_MAGNITUDE:
        raise CalculationError("Number is outside the supported range.")
    return value


def _evaluate(node, depth=0):
    if depth > MAX_DEPTH:
        raise CalculationError("Expression is too deeply nested.")
    if isinstance(node, ast.Constant):
        return _checked(node.value)
    if isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub):
        operand = _evaluate(node.operand, depth + 1)
        return _checked(operand if isinstance(node.op, ast.UAdd) else -operand)
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATIONS:
        left = _evaluate(node.left, depth + 1)
        right = _evaluate(node.right, depth + 1)
        try:
            return _checked(OPERATIONS[type(node.op)](left, right))
        except ZeroDivisionError as error:
            raise CalculationError("Cannot divide by zero.") from error
    raise CalculationError("Only numbers, parentheses and + - * / are supported.")


def calculate_expression(expression):
    """Return a finite numeric result or raise CalculationError.

    This is a deliberately limited calculator, not a general Python sandbox.
    Function calls, names, attributes, and arbitrary Python execution are rejected.
    """
    expression = expression.strip()
    if not expression:
        raise CalculationError("Enter an expression.")
    if len(expression) > MAX_LENGTH:
        raise CalculationError("Expression is too long.")
    try:
        tree = ast.parse(expression, mode="eval")
    except (SyntaxError, ValueError, RecursionError) as error:
        raise CalculationError("Invalid expression.") from error
    return _evaluate(tree.body)
