class Student:
    def __init__(self, name, dept, cgpa, year):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        self.year = year

    def is_eligible(self):
        return self.cgpa >= 7.0 and self.year >= 3

name = input("Name: ")
dept = input("Department: ")
cgpa = float(input("CGPA: "))
year = int(input("Year: "))

s = Student(name, dept, cgpa, year)
print("Eligible for Placement" if s.is_eligible() else "Not Eligible")
