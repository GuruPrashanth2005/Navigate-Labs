class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours


employees = [
    FullTimeEmployee("Arun", 50000),
    ContractEmployee("Meena", 500, 80)
]

for emp in employees:
    print(emp.name, "Salary:", emp.calculate_salary())
