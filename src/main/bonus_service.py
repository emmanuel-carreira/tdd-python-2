from src.main.employee import Employee


def calculate_bonus(employee: Employee) -> float:
    value = employee.salary * 0.1
    return value if value <= 1000 else 0
