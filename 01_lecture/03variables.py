"""
Variables

In the context of programming, a variable is a location for storing some value, such as a string or a number.
You can use variables to store any information that will be needed later in the program's execution.
"""

# my_name = "Leon"    # storing a string value
# my_age = 31         # storing a number value
#
# print(my_name + str(my_age))
#
#
# # The value stored in a variable can also be defined using other variables:
# firstname = "Bart"
# lastname = "Simpson"
#
# character = firstname + " " + lastname
#
# print(character)

"""
Here the values stored in the three variables are not obtained from user input. 
They remain the same every time the program is executed. 
This is called hard-coding data into the program.
"""

"""
Reassignment of variables

As implied by the name variable, the value stored in a variable can change.
"""

# word = input("Type in a word: ")
# print(word)
#
# word = input("Another word: ")
# print(word)

"""
Assigning multiple values at once
"""
# a = b = "Hello"
# print(a)
# print(b)

"""
Assigning different values to multiple variables
"""

# a, b, c = "Hello", "World", "!"
#
# print(a)
# print(b)
# print(c)


"""
Integers

Integers are numbers that do not have a decimal or fractional part, such as -15, 0 and 1.
"""
number1 = -100
number2 = "100"

print(number1)
print(number2)

"""
Variable types matter because different operations affect different types of variables in different ways. Let's have a look at an example:
"""
number1 = 100
number2 = "100"

print(number1 + number1)
print(number2 + number2)

"""
Not all operators are available for all types of variables. 
While numbers can be divided using the division operator /, attempting to divide a string by a number causes an error:
"""
number = 100
print(number / 2)

"""
Combining values while printing

The following program will not work, because "The result is " and result are of two different types:
"""

# result = 10 * 25
# # the following line produces an error
# print("The result is " + result)

"""
If we do want to print out a string and an integer in a single command, the integer can be cast as a string with 
the str function, and the two strings can then be combined normally. 
For example, this would work:
"""
# result = 10 * 25
# print("The result is " + str(result))

"""
The print command also has built-in functionalities that support combining different types of values. 
The simplest way is to add a comma between the values. 
All the values will be printed out regardless of their type:
"""

# result = 10 * 25
# print("The result is", result)

"""
Printing with f-strings

So called f-strings are another way of formatting printouts in Python. 
The syntax can initially look a bit confusing, but in the end f-strings are often the simplest way of formatting text.
"""
result = 10 * 25
print(f"The result is {result}")

name = "René"
age = 30
city = "Vienna"
print(f"Hi {name}, you are {age} years old. You live in {city}.")
print("Hi " + name + " , you are " + str(age) + " years old.")

"""
Floating point numbers

Floating point number or float is a term you will come across often in programming. 
It refers to numbers with a decimal point. They can be used much in the same way as integer values.
"""
number1 = 2.5
number2 = -1.25
number3 = 3.62

mean = (number1 + number2 + number3) / 3
print(f"Mean: {mean}")
