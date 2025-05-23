class Countdown:
    def __init__(self, start):
        self.start = start + 1  # Initialize counter
    
    def __iter__(self):
        return self  # Returns the iterator object
    
    def __next__(self):
        self.start -= 1
        if self.start < 0:
            raise StopIteration  # Signals end of iteration
        return self.start

# Using the iterable in a for loop
print("Countdown from 5:")
for num in Countdown(5):
    print(num, end=" ") 

# Manual iteration demonstration
print("\n\nCountdown from 3:")
counter = Countdown(3)
iterator = iter(counter)
print(next(iterator))  # 3
print(next(iterator))  # 2
print(next(iterator))  # 1
print(next(iterator))  # 0
try:
    print(next(iterator))  # Raises StopIteration
except StopIteration:
    print("Countdown finished!")