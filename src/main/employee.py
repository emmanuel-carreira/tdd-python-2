from dataclasses import dataclass
from datetime import datetime


@dataclass
class Employee:
    name: str
    salary: float
    admission_date: datetime

    def readjust_salary(self, readjustment: float) -> None:
        self.salary *= readjustment
