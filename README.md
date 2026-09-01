# Arithmetic Calculator

A small Python/Tkinter learning project for desktop arithmetic. The interface is
kept separate from the calculation engine so the arithmetic can be tested without
opening a window.

## Features

- Addition, subtraction, multiplication and division with normal precedence.
- Parentheses and signed numbers entered from the keyboard.
- Enter to calculate; Escape or Clear to reset.
- Specific messages for invalid input, division by zero and numeric limits.
- An allowlisted expression parser instead of Python's `eval()`.
- Automated tests using the Python standard library.

## Run

Use Python 3.10 or newer with Tkinter installed. No pip packages are required.
From this repository's directory:

```sh
python -m tkinter
python kola.py
```

The first command checks Tkinter and opens a small test window. If Tkinter is
missing, install the Tk support package for your Python distribution.

## Test

```sh
python -m unittest discover -s tests -v
```

Tests cover arithmetic, precedence, signs, invalid syntax, unsupported Python
constructs, division by zero, length/depth/range limits and GUI-safe imports.

## Structure

```text
calculator.py              Arithmetic parsing and validation
kola.py                    Desktop interface and entry point
tests/test_calculator.py   Automated tests
```

## Examples

| Input | Result |
| --- | --- |
| `2 + 3 * 4` | `14` |
| `(2 + 3) * 4` | `20` |
| `9 / 2` | `4.5` |
| `10 / 0` | Division-by-zero message |

## Design and limitations

The engine parses an expression with `ast` and only evaluates numeric constants,
unary signs and the four arithmetic operators. Names, function calls, attributes,
containers, powers and other Python constructs are rejected. Input length is
limited to 128 characters, evaluation depth to 16, and each numeric value/result
to an absolute value of 10^12.

This is an educational calculator, not a general-purpose code sandbox or a
financial calculator. Decimal results use Python floating-point arithmetic;
rounding artifacts can occur. The GUI still needs manual checks on each target
desktop platform.

## Development note

The original version used `eval()` inside the Tkinter callback. This revision
separates the engine from the interface and adds validation and regression tests.
The revision was prepared with AI assistance and should be reviewed and understood
before using it as a portfolio example.
