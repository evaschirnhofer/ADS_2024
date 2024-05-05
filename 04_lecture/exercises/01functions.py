"""
Exercises "Functions"
"""

"""
### Function Definition / Execution ###

Define a function called "bark()". When executed, "Woof" should get printed to the console.
Execute the function after its definition and run the program!
"""

# Write your solution here
def bark():
    print("Woof")

bark()

"""
### Function with 1 Argument, additional logic ###

Write a program that asks the user to enter an animal. The program should respond with the corresponding animal sound.
Define a function called "makeSound(animal)". The function should use the given input to print the correct animal sound.
Add functionality for at least 3 animals and print the right sounds.
If the animal doesn't exists in the program, print "???".
Use a loop to repeatedly ask the user to enter another animal.
Make sure that upper- and lowercase letters both work when entering an animal.

Examples:
    Please enter an animal: >> dog
    Woof
    Please enter an animal: >> Cat
    Meow
    ...
"""

def make_sound(animal):
    print(animal)


while True:
    animal = str(input("Please enter an animal: "))
    if animal.lower() == "cat":
        make_sound("Meow")
    elif animal.lower() == "dog":
        make_sound("Woof")
    elif animal.lower() == "bird":
        make_sound("chirp")
    else:
        make_sound("???")
        break


"""
### Function with 2 Arguments ###

Write a function named print_many_times(text, times), which takes a string and an integer as arguments. 
The integer argument specifies how many times the string argument should be printed out.

Example:
    print_many_times("Gimme Five!", 5)
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!

Additional Task:
Instead of "hard coding", let the user enter the text and the number of times to print it!
Ask the user repeatedly using a loop.
"""

# Write your solution here
# variante 1
def print_many_times(text, times):
    """
    Prints the given text for the specified number of times.

    Args:
        text (str): The text to be printed.
        times (int): Number of times to print the text.
    """
    for _ in range(times):
        print(text)

# Example usage
print_many_times("Gimme Five!", 5)

# Variante 2
def print_many_times(text, times):
    """
    Prints the given text for the specified number of times.

    Args:
        text (str): The text to be printed.
        times (int): Number of times to print the text.
    """
    for _ in range(times):
        print(text)

# Loop to ask for user input repeatedly
while True:
    # Ask for text and number of times to print
    text = input("Enter the text to print (or 'q' to quit): ")
    if text.lower() == 'q':  # Check if the user wants to quit
        break
    try:
        times = int(input("Enter the number of times to print: "))
        if times < 0:  # Check if the number of times is negative
            raise ValueError("Number of times must be a positive integer.")
        print_many_times(text, times)  # Call the function to print the text
    except ValueError as e:
        print("Invalid input:", e)

"""
### Return Values ###

Define a function named greatest_number, which takes three arguments. The function returns the greatest in value of the 
three. Use the already defined function "print_greatest" and pass the return value of your function to it!

Example:
    return_value = greatest_number(3, 4, 1)
    print_greatest(return_value)
    The greatest number is 4!
    
Additional Task:
Add a type hint to the return value of the function!
"""
def greatest_number(a: int, b: int, c: int) -> int:
    """
    Returns the greatest of three numbers.

    Args:
        a (int): First number.
        b (int): Second number.
        c (int): Third number.

    Returns:
        int: The greatest number among the three.
    """
    return max(a, b, c)

def print_greatest(number: int):
    """
    Prints the greatest number.

    Args:
        number (int): The greatest number to print.
    """
    print(f"The greatest number is {number}!")

# Example usage
return_value = greatest_number(3, 4, 1)
print_greatest(return_value)

"""
### Type Hints ###

Refactor your programs from above and add type hints to all function arguments and return values (if available)!
"""

# No code here, refactor the programs above!

"""
### Named arguments ###

Define a function named super_print which takes two arguments, a string and a boolean value.
If the boolean value is false, print the text as it was. If its True, print it in all upper case.
Use named arguments to use a different order of the arguments. First, use the string as first argument. For the second
call, use the boolean value as the first argument. Also, make use of type hints for the function arguments.

Example Outputs:
    HELLO WORLD
    hello world
"""

# Write your solution here
def super_print(text: str, upper_case: bool):
    if upper_case:
        print(text.upper())
    else:
        print(text)

# First call with string as first argument
super_print("hello world", False)

# Second call with boolean as first argument
super_print(upper_case=True, text="hello world")



"""
### Default Values ###

Define a simple function greet() that takes one argument "name". The function should print a greeting for the entered 
name. Ask the user for his/her name and execute the greet function, passing the name as an argument.
If nothing was entered, use a default value for the name to greet "Unknown".

Hint: An empty string is still a value you can pass, be careful :-)

Example:
    Please enter your name: >> René
    Hello René!
    Please enter your name: >> 
    Hello Unknown!
"""

# Write your solution here
def greet(name="Unknown"):
    """
    Prints a greeting for the entered name.

    Args:
        name (str): The name to greet. Default is "Unknown" if no name is provided.
    """
    print(f"Hello {name}!")

# Ask for user input
user_name = input("Please enter your name: >> ")

# Execute the greet function
if user_name.strip():  # Check if the input is not empty or only whitespace
    greet(user_name)
else:
    greet()  # No input provided, use the default value "Unknown"

