#ducktype
class Dog:
    def speak(self):
        print("woof!")

class cat:
    def speak(self):
        print("Meow!")

class Human:
    def speak(self):
        print("hello!")

def make_it_speak(obj):
    obj.speak()
    