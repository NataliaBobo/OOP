class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming.")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"The {self.model} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"The {self.model} is driving.")

class Plane(Vehicle):
    def move(self):
        print(f"The {self.model} is flying.")

# Create instances of the classes
my_dog = Dog("Charlie")
my_fish = Fish("Goshie")
my_car = Car("BMW")
my_plane = Plane("Boeing 747")

# Call the move() method on each object
my_dog.move()
my_fish.move()
my_car.move()
my_plane.move()