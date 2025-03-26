# sample_test.py

def add_numbers(a, b):
    return a + b


# Type mismatch
result: int = add_numbers("5", 10)

# Undefined variable
print(unknown_variable)   #

# Incorrect return type
def get_message() -> int:
    return "Hello, world!"   #

# Unused variable
unused_var = 42

# Unreachable code
return_value = 1 / 0
print("This will never run")

# Attribute error
class Sample:
    def __init__(self):
        self.name = "Sample"

obj = Sample()
print(obj.age)  # age is not defined   #
