"""
FUNCTIONS
"""

"""
FUNCTION DEFINITIONS AND EXECUTIONS
Functions are defined using the 'def' keyword followed by the function name and parentheses.
"""


def greet():
    print("Hello, World!")


# Function execution
greet()  # prints: Hello, World!

"""
FUNCTIONS WITH ONE ARGUMENT
Functions can take arguments, which are values passed into the function to be used within.
"""


def greet(name):
    print("Hello, " + name + "!")


# Function execution with one argument
greet("Alice")  # prints: Hello, Alice!

"""
FUNCTIONS WITH TWO ARGUMENTS
Functions can also take more than one argument.
"""


def greet(first_name, last_name):
    print("Hello, " + first_name + " " + last_name + "!")


# Function execution with two arguments
greet("Alice", "Johnson")  # prints: Hello, Alice Johnson!

"""
RETURN VALUES
Functions can return values using the 'return' keyword.
"""


def add(a, b):
    return a + b


# Capturing return value
result = add(3, 4)
print(result)  # prints: 7

"""
TYPE HINTS
Type hints can be used to indicate the expected data types of arguments and the return type.
"""


def add(a: int, b: int) -> int:
    return a + b


# Function with type hints
result = add(5, 6)
print(result)  # prints: 11

"""
NAMED ARGUMENTS
Arguments can be specified by their names when calling the function.
"""


def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type + " named " + pet_name + ".")


# Using named arguments
describe_pet(animal_type="hamster", pet_name="Harry")  # prints: I have a hamster named Harry.

"""
DEFAULT VALUES
Functions can have parameters with default values.
"""


def describe_pet(pet_name, animal_type="dog"):
    print("I have a " + animal_type + " named " + pet_name + ".")


# Using default values
describe_pet(pet_name="Rover")  # prints: I have a dog named Rover.

# Overriding default values
describe_pet(pet_name="Whiskers", animal_type="cat")  # prints: I have a cat named Whiskers.
