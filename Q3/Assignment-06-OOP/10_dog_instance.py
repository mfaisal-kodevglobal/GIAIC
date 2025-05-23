class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed
    
    # Instance method
    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof!")

# Create Dog instances
dog1 = Dog("Tommy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Call instance methods
dog1.bark() 
dog2.bark() 