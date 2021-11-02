from datetime import datetime
import unittest

from src.main import readjustment_service
from src.main.employee import Employee
from src.main.performance import Performance


class ReadjustmentServiceTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Test', 10000, datetime.utcnow())

    def test_salary_readjuste_should_be_three_percent_for_employee_below_expectations(self):
        readjustment_service.readjust_salary(self.employee, Performance.BELOW_EXPECTATIONS)
        self.assertEqual(self.employee.salary, 10300)

    def test_salary_readjuste_should_be_fifteen_percent_for_employee_with_good_performance(self):
        readjustment_service.readjust_salary(self.employee, Performance.GOOD)
        self.assertEqual(self.employee.salary, 11500)

    def test_salary_readjuste_should_be_twenty_percent_for_employee_with_great_performance(self):
        readjustment_service.readjust_salary(self.employee, Performance.GREAT)
        self.assertEqual(self.employee.salary, 12000)

    def test_salary_is_not_readjusted_when_performance_is_not_valid(self):
        readjustment_service.readjust_salary(self.employee, 0)
        self.assertEqual(self.employee.salary, 10000)
