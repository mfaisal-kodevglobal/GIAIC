def log_function_call(func):
    """Decorator that logs when a function is called"""
    def wrapper(*args, **kwargs):
        print(f"'{func.__name__}' is being called")  # Log message
        return func(*args, **kwargs)  # Call the original function
    return wrapper

# Applying the decorator
@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Testing the decorated function
say_hello("Alice")