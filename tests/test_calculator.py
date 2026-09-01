import importlib
import unittest

from calculator import CalculationError, calculate_expression


class CalculatorTests(unittest.TestCase):
    def test_arithmetic(self):
        for expression, expected in [("2+3", 5), ("8-12", -4), ("6*7", 42), ("9/2", 4.5), ("0*12", 0)]:
            with self.subTest(expression=expression):
                self.assertEqual(calculate_expression(expression), expected)

    def test_precedence_and_parentheses(self):
        self.assertEqual(calculate_expression("2+3*4"), 14)
        self.assertEqual(calculate_expression("(2+3)*4"), 20)
        self.assertEqual(calculate_expression("8/2/2"), 2)

    def test_signs_whitespace_and_decimals(self):
        self.assertEqual(calculate_expression("  -3 + +5  "), 2)
        self.assertEqual(calculate_expression("-(2+3)"), -5)
        self.assertAlmostEqual(calculate_expression("0.1+0.2"), 0.3)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(CalculationError, "zero"):
            calculate_expression("10/(2-2)")

    def test_invalid_expressions(self):
        for expression in ["", "   ", "2+", "(", "2 3", "2;3"]:
            with self.subTest(expression=expression), self.assertRaises(CalculationError):
                calculate_expression(expression)

    def test_non_arithmetic_is_rejected(self):
        for expression in ["True", "None", "'hello'", "[1]", "{1:2}", "(1,2)", "x", "abs(-1)", "(1).__class__", "1<2", "1 and 2", "2**8", "4//2", "4%2", "2<<2"]:
            with self.subTest(expression=expression), self.assertRaises(CalculationError):
                calculate_expression(expression)

    def test_length_depth_and_numeric_limits(self):
        for expression in ["1+" * 100 + "1", "-" * 20 + "1", "1e999", "1000000000001", "1000000000000*2"]:
            with self.subTest(expression=expression), self.assertRaises(CalculationError):
                calculate_expression(expression)
        self.assertEqual(calculate_expression("1000000000000"), 1_000_000_000_000)

    def test_import_does_not_start_gui(self):
        self.assertTrue(callable(importlib.import_module("kola").main))


if __name__ == "__main__":
    unittest.main()
