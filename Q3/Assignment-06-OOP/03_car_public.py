class Car:
    # Constructor with public variable initialization
    def __init__(self, brand="Unknown"):
        self.brand = brand  # Public instance variable
    
    # Public method
    def start(self):
        print(f"The {self.brand} car has started!")

# Creating instances with constructor
car1 = Car("Toyota")  # Initialize brand through constructor
car2 = Car("Honda")

# Accessing public variable
print(f"Car1 brand: {car1.brand}") 
print(f"Car2 brand: {car2.brand}")  

# Modifying public variable after creation
car1.brand = "Lexus"
print(f"Updated car1 brand: {car1.brand}")  

# Calling public method
car1.start()  
car2.start()  
