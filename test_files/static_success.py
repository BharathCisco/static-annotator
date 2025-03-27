def my_function(x, y):
    """Takes an integer and a string, returns an integer."""
    z = x + len(y)
    return z

def another_function(a, b):
    """Takes a list of integers and a dictionary, returns a tuple."""
    result_list = [i * 2 for i in a]
    result_keys = list(b.keys())
    return result_list, result_keys


class SampleClass:
    """A sample class to demonstrate type annotation."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Greet with the person's name."""
        return f"Hello, {self.name}! You are {self.age} years old."
