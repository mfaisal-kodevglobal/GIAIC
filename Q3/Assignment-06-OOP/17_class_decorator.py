def add_greeting(cls):
    """Class decorator that adds a greet() method"""
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add the new method to the class
    return cls  # Return the modified class

# Apply the decorator to a class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorated class
p = Person("Alice")
print(p.greet())  
print(p.name)    