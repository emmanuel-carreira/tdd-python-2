from src.main.employee import Employee
from src.main.performance import Performance


class ReadjustmentService:
    def readjust_salary(self, employee: Employee, performance: Performance) -> None:
        readjustment = 1
        performance_strategy = {
            Performance.BELOW_EXPECTATIONS: 0.03,
            Performance.GOOD: 0.15,
            Performance.GREAT: 0.2
        }
        readjustment += performance_strategy.get(performance, 0)

        employee.readjust_salary(readjustment)
