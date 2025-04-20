class Hair:
    #Attribute
    color = "Brown"
    length = "long"
    style = "Kinky"

#Constructor
def __init__(self, color, length, style):
    self.color = color
    self.length = length
    self.style = style

    #Method
    def straightener(self):
        print(f"This {self.style} hair is straightened")
    def dye(self):
        print(f"This hair is dyed {self.color}")  
    def get_info(self):
        #Returns a string with the hair's information.
        return f"Color: {self.color}, Length: {self.length}, Style: {self.style}"

 #Objects with unique values
hairtype1 = Hair("Kinky", "Short","Ginger")
hairtype2 = Hair("Curly", "Long","Brown")
hairtype3 = Hair("Straight", "Medium", "Black")


# Demonstrating the methods and attributes
print(hairtype1.get_info())
hairtype1.straightener()
hairtype1.dye("Red Wine")
print(hairtype1.get_info())
  # Show updated color

print(hairtype2.get_info())
hairtype2.dye("Blue")
print(hairtype2.get_info())


print(hairtype3.get_info())
hairtype3.straightener()
print(hairtype3.get_info()) # Show updated style
   
#Inheritance
class WavyHair(Hair):
    #Represents wavy hair, inheriting from the Hair class.
    def __init__(self, color="Brown", length="Medium"):
        #Constructor for WavyHair.  
        
        # Calls the parent class's constructor and sets the style to "Wavy" by default.
        
        super().__init__(color, length, "Wavy") # Call to parent constructor

    def add_volume(self):
        print(f"The wavy hair has added volume.")
 

# Create a WavyHair object
wavy_hair1 = WavyHair("Blonde", "Long")
print(wavy_hair1.get_info())  # It inherits color and length, and has style Wavy
wavy_hair1.straighten() #It can use methods from the parent class
wavy_hair1.add_volume()
