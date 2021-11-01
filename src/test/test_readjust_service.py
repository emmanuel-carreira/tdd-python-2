from datetime import datetime
import unittest

from src.main import readjustment_service
from src.main.employee import Employee
from src.main.performance import Performance


class ReadjustmentServiceTest(unittest.TestCase):
    def test_salary_readjuste_should_be_three_percent_for_employee_below_expectations(self):
        employee = Employee('Test', 10000, datetime.utcnow())
        readjustment_service.readjust_salary(employee, Performance.BELOW_EXPECTATIONS)
        self.assertEqual(employee.salary, 10300)

    def test_salary_readjuste_should_be_fifteen_percent_for_employee_with_good_performance(self):
        employee = Employee('Test', 10000, datetime.utcnow())
        readjustment_service.readjust_salary(employee, Performance.GOOD)
        self.assertEqual(employee.salary, 11500)

    def test_salary_readjuste_should_be_twenty_percent_for_employee_with_great_performance(self):
        employee = Employee('Test', 10000, datetime.utcnow())
        readjustment_service.readjust_salary(employee, Performance.GREAT)
        self.assertEqual(employee.salary, 12000)

    def test_salary_is_not_readjusted_when_performance_is_not_valid(self):
        employee = Employee('Test', 10000, datetime.utcnow())
        readjustment_service.readjust_salary(employee, 0)
        self.assertEqual(employee.salary, 10000)
