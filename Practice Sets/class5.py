class Employee:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Employee Name: {self.name}"
emp = Employee("Yaswanth")
print(emp)
