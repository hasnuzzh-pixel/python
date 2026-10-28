#multilevel inheritance
class Grandparent:
    def sing(self):
        print("Grandparent is singing.")

class parent(Grandparent):
    def dance(self):
        print("parent is dancing.")

class child(parent):
    def play(self):
        parent("child is playing.")


child = child()
child.sing()
child.dance()
child.play()