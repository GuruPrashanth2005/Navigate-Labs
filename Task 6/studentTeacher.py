class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "studying")

class Teacher(Person):
    def teach(self):
        print(self.name, "teaching")

Student("Arun").study()
Teacher("Meena").teach()
