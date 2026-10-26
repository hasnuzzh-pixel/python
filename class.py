#defaining a class
class car:
    def __init__(self,make,model,year,):
     self.make = make
     self.model = model
     self.year = year
     


    def display_info(self):
       print(f"car:{self.year} {self.make} {self.model}")

#creating an object(instance) of the car class
my_car = car("Toyota", "corolla", 2021)


#Accessing object methods
my_car.display_info()


#object in python
car1 = car("Honda", "civic",2022)
car2 = car("ford", "mustang", 2023)

car1.display_info()
car2.display_info()

#the self keyword

class person:
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def greet(self):
     print(f"Hello,my name is{self.name}and i am {self.age} years old.")

person1 = person("Alice",30)
person1.greet()

#Accessing class attributes and methods
class Dog:
   def __init__(self,breed,name):
      self.breed = breed
      self.name = name

   def bark(self):
         print(f"{self.name} says woof!")

#creating an object
dog1 = Dog("Labrador","Buddy")

#Accessing attributes
print(dog1.breed)

#Accessing methods
dog1.bark()

#modifying object
dog1.name = "Max"
dog1.bark()

#The str() method
class Book:
   def __init__(self,title,author):
      self.title = title
      self.author = author

   def __str__(self):
       return f"{self.title}'by {self.author}"

book = Book("1984", "george orwell")
print(book)