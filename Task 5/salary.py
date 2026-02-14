class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def final_salary(self):
        if self.designation == "Manager":
            return self.salary + 5000
        elif self.designation == "Developer":
            return self.salary + 3000
        return self.salary

e = Employee("Ram", "Manager", 50000)
print("Final Salary:", e.final_salary())
