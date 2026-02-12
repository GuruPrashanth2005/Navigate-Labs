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
    def calculate_bonus(self):
        return self.__salary * 0.5
emp=Employee("Madhubalakumar",50000)
emp.set_name("Yaswanth")
emp.set_salary(60000)
print(emp.get_name(),emp.get_salary(),"Bonus:",emp.calculate_bonus())
