#single inheritance
class Animal:
    def __init__(self,name):
        self.name = name


    def speak(self):
        print(f"{self.name} make a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} syas woof!")

dog = Dog("Buddy")
dog.speak()