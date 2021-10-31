from datetime import datetime


class Employee:
    def __init__(self, name: str, salary: float, admission_date: datetime) -> None:
        self._name = name
        self._salary = salary
        self._admission_date = admission_date

    @property
    def admission_date(self):
        return self._admission_date

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary
