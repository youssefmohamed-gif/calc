import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(calculate(-5, -3, "+"), -8)

    def test_addition_positive_and_negative(self):
        self.assertEqual(calculate(-5, 3, "+"), -2)


if __name__ == "__main__":
    unittest.main()
