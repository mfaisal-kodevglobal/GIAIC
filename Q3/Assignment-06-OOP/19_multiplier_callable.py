class Multiplier:
    def __init__(self, factor):
        """Initialize with multiplication factor"""
        self.factor = factor
    
    def __call__(self, x):
        """Make instances callable like functions"""
        return x * self.factor

# Create a multiplier object
double = Multiplier(2)
triple = Multiplier(3)

# Test if objects are callable
print("Is double callable?", callable(double))  # True
print("Is triple callable?", callable(triple))  # True

# Call objects like functions
print("Double of 5:", double(5))    # 10 (2 * 5)
print("Triple of 5:", triple(5))    # 15 (3 * 5)

# Can still access the factor
print("Multiplication factor:", triple.factor)  # 3