class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, amount):
        if amount > 0:
            self.__salary += amount

    def get_salary(self):
        return self.__salary

emp = Employee(50000)
emp.update_salary(5000)
print(emp.get_salary())
