class Counter:
    # Class variable to keep track of count
    count = 0
    
    def __init__(self):
        # Increment the count when a new instance is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        # Using cls to access the class variable
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()  # Output: Total objects created: 3

obj4 = Counter()
Counter.display_count()  # Output: Total objects created: 4