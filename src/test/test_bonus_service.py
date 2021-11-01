from datetime import datetime
import unittest

from src.main import bonus_service
from src.main.employee import Employee


class BonusServiceTest(unittest.TestCase):
    def test_throws_exception_when_employee_salary_is_greater_than_10000(self):
        employee = Employee('Test', 11000, datetime.utcnow())
        with self.assertRaises(Exception):
            bonus_service.calculate_bonus(employee)

    def test_bonus_is_one_tenth_of_the_salary_when_employee_salary_is_less_than_10000(self):
        employee = Employee('Test', 1000, datetime.utcnow())
        bonus = bonus_service.calculate_bonus(employee)
        self.assertEqual(bonus, 100)

    def test_bonus_is_one_tenth_of_the_salary_when_employee_salary_is_exactly_10000(self):
        employee = Employee('Test', 10000, datetime.utcnow())
        bonus = bonus_service.calculate_bonus(employee)
        self.assertEqual(bonus, 1000)
