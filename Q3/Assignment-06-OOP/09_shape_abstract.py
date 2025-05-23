from abc import ABC, abstractmethod

class Shape(ABC):  # Inherit from ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by subclasses"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Concrete implementation of area() for Rectangle"""
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")  
