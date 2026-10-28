#multiple inheritance
class Engine:
    def start_engine(self):
        print("Engine started.")

class Wheels:
    def rotate(self):
        print("wheels are rotating.")

class car:
    def drive(self):
        print("car is driving.")


car = car()
car.start_engine()
car.rotate()
car.drive()