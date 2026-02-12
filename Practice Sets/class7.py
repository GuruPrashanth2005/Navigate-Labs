class Person:
    def __init__(self):
        self.__name = input("Name: ")
        self.__age = int(input("Age: "))

    def get_details(self):
        return self.__name, self.__age
    
class Salary(Person):
    def get_salary(self):
        self.__salary = int(input("Salary: "))
        return self.__salary

    def display(self):
        name, age = self.get_details()
        salary = self.__salary
        print("Name:", name)
        print("Age:", age)
        print("Salary:", salary)

details = Salary()
details.get_salary()
details.display()
