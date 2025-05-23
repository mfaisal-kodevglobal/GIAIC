class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (convention)
        self.__ssn = ssn       # Private variable (name mangling)

# Create an Employee object
emp = Employee("Ahmed", 75000, "123-45-6789")

# Accessing variables:
print("Public (name):", emp.name)         # ✅ Works
print("Protected (_salary):", emp._salary)  # ⚠️ Works (but discouraged)
try:
    print("Private (__ssn):", emp.__ssn)   # ❌ Fails (AttributeError)
except AttributeError as e:
    print("Private access failed:", e)

# Accessing private variable using name mangling (not recommended)
print("Private (name-mangled):", emp._Employee__ssn)  # 🚨 Works (but hacky)