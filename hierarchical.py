#hierarchical inheritence
class animal:
    def speak(self):
        print("animal speaks.")

class dog(animal):
    def speak(self):
        print("dog barks.")

class cat(animal):
    def speak(self):
        print("cat meows.")


Dog = dog()
Cat = cat()

dog.speak()
cat.speak()