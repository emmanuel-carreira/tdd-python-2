from src.main.employee import Employee
from src.main.performance import Performance


def readjust_salary(employee: Employee, performance: Performance) -> None:
    readjustment = 1 + Performance.get_readjustment_percentage(performance)
    employee.readjust_salary(readjustment)
