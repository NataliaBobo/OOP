# Defining a class
class Car:
    color = "red"  # Attribute
    model = "sedan"
    
    # Method/behavior of the car
    def drive(self): #self accesses the attributes and methods of the class.
        print("The car is driving")

# Creating an object
my_car = Car() #Car variable is assigned to the car class
my_car.drive()  #Call the method. The car drives
print(my_car.model)