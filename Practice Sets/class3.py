#encapsulation
class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("Invalid salary")
    def set_name(self,name):
        if name:
            self.__name=name
        else:
            print("Invalid name")
emp=Employee("Madhubalakumar",50000)
emp.set_name("Yaswanth")
emp.set_salary(60000)
print(emp.get_name())
print(emp.get_salary())
