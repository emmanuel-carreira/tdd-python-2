from src.main.employee import Employee


def calculate_bonus(employee: Employee) -> float:
    if employee.salary > 10000:
        raise Exception("Employee with salary greater than 10000 can't have bonus!")
    return employee.salary * 0.1
