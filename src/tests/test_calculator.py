import unittest

from src import calculator


class CalculatorTest(unittest.TestCase):
    def test_sum_two_numbers_when_both_are_positive_numbers(self):
        result = calculator.sum_two_numbers(2, 8)
        self.assertEqual(result, 10)

    def test_sum_two_numbers_when_one_of_them_is_a_zero(self):
        result = calculator.sum_two_numbers(2, 0)
        self.assertEqual(result, 2)

    def test_sum_two_numbers_when_both_are_zero(self):
        result = calculator.sum_two_numbers(0, 0)
        self.assertEqual(result, 0)

    def test_sum_two_numbers_when_one_of_them_is_negative(self):
        result = calculator.sum_two_numbers(4, -2)
        self.assertEqual(result, 2)
