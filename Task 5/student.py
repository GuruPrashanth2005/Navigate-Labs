class Student:
    def __init__(self, name):
        self.name = name
        self.courses = set()

    def register(self, course):
        if course in self.courses:
            print("Already Registered")
        else:
            self.courses.add(course)

s = Student("Anu")
s.register("Math")
