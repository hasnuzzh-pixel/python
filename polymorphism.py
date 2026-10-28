#polymorphism
class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):
    def speak(self):
        return "woof"

class cat(Animal):
    def speak(self):
        return "meow!"

def animal_sound(animal:Animal):
    return animal.speak()

#example usage:
dog = Dog()
cat  = cat()
print(animal_sound(dog))
print(animal_sound(cat))