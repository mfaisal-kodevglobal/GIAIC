class Logger:
    def __init__(self, name):
        """Constructor: Called when object is created"""
        self.name = name
        print(f"Logger '{self.name}' created!")

    def __del__(self):
        """Destructor: Called when object is destroyed"""
        print(f"Logger '{self.name}' destroyed!")

print("Creating loggers...")
log1 = Logger("SystemLog")
log2 = Logger("ErrorLog")

print("\nDeleting loggers...")
del log1  # Explicitly deleting log1
# log2 will be automatically deleted when the program ends