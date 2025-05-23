# 1. Define the custom exception
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# 2. Function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print(f"Age {age} is valid - access granted")

# 3. Test with try-except
ages_to_test = [15, 20, 17, 25]

for age in ages_to_test:
    try:
        check_age(age)
    except InvalidAgeError as e:
        print(f"Invalid age: {e.age} - {e}")