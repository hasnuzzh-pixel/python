class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def display_employee(self):
        print(f"name: {self.name}, salary:{self.__salary}")


    def update_salary(self, new_salary):
        self.__salary = new_salary

emp = Employee("john",50000)
emp.display_employee()

#correct way to  update and access private attribute
emp.update_salary(60000)
emp.display_employee()