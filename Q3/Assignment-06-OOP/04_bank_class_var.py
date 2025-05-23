class Bank:
    # Class variable shared by all instances
    bank_name = "Global Bank"
    
    def __init__(self, branch):
       self.branch = branch  # Instance variable
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    def display_info(self):
        print(f"Bank: {self.bank_name}, Branch: {self.branch}")

# Create instances
branch1 = Bank("Korangi")
branch2 = Bank("Malir")

# Show initial state
print("Initial state:")
branch1.display_info() 
branch2.display_info()  

# Change bank name using class method
Bank.change_bank_name("International Bank")

# Show all instances reflect the change
print("\nAfter name change:")
branch1.display_info()  
branch2.display_info()  
