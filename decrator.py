#decrator
#class method 
class company:
    company_name = "Tech innovators"

    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name = new_name

#changing class variable through a class method
company.change_company_name("Future solutions")
print(company.company_name)

#static method
class mathoperations:
    @staticmethod
    def add(a,b):
        return a+b


print(mathoperations.add(10,20))