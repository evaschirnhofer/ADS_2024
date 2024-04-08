"""
STRING OPERATIONS

Strings can be combined -> concatenated with the `+` operator
"""

# begin = "ex"
# end = "ample"
# word = begin+end
# print(word) # prints: example

"""
The `*` operator can also be used with a string, when the other operand is an integer. 
The string operand is then repeated the number of times specified by the integer. 
For example this would work:
"""

# word = "banana"
# print(word*3)   # prints: bananabananabanana

"""
Using string operations together with a loop we can write a program which draws a pyramid.
How it works:
    The print command within the loop prints a line, which begins with n spaces, 
    followed by whatever is stored in the variable row. Then two stars are added 
    to the end of the variable row, and the value of the variable n is decreased by 1.
"""
# n = 10 # number of layers in the pyramid
# row = "*"
#
# while n > 0:
#     print(" " * n + row)
#     row += "**"
#     n -= 1


"""
LENGTH and INDEX of a string

The function ``len`` returns the number of characters in a string, which is always an integer value. 
For example, len("hey") returns 3, because there are three characters in the string hey.

The following program asks the user for a string and then prints it "underlined". 
The program prints a second line with as many - characters as is the length of the input:
"""
# input_string = input("Please type in a string: ")
# print(input_string)
# print("-"*len(input_string))


"""
Since len returns an integer, it is also possible to compare their results:
"""
# input_string = input("Please type in a string 1: ")
# input_string2 = input("Please type in a string 2: ")
#
# if len(input_string) < len(input_string2):
#     print(f"{input_string2} has more characters than {input_string}")

"""
As strings are essentially sequences of characters, any single character in a string can also be retrieved. 
The operator [] finds the character with the index specified within the brackets.
The index refers to a position in the string, counting up from zero. 
The first character in the string has index 0, the second character has index 1, and so forth.
"""
# input_string = input("Please type in a string: ")
# print(input_string[0])
# print(input_string[1])
# print(input_string[3])

"""
Since the first character in a string has the index 0, the last character has the index length - 1. 
The following program prints out the first and the last characters of a string:
"""
# input_string = input("Please type in a string: ")
# print("First character: " + input_string[0])
# print("Last character: " + input_string[len(input_string) - 1])

"""
The following program loops through all the characters in a string from first to last:
"""
# input_string = input("Please type in a string: ")
# index = 0
# while index < len(input_string):
#     print(input_string[index])
#     index += 1

"""
You can also use negative indexing to access characters counting from the end of the string. 
The last character in a string is at index -1, the second to last character is at index -2, and so forth. 
You can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].
"""
# input_string = input("Please type in a string: ")
# print("First character: " + input_string[0])
# print("Last character: " + input_string[-1])

"""
IndexError: string index out of range

If you tried the above examples for yourself, you may already have come across the error message 
IndexError: string index out of range. 
This error appears if you try to access an index which is not present in the string.
"""
# input_string = input("Please type in a string: ")
# print("The tenth character: " + input_string[9])    # throws an error if input_string has less than 10 characters


"""
Substrings and slices

A substring of a string is a sequence of characters that forms a part of the string. 
For example, the string ``example`` contains the substrings ``exam``, ``amp`` and ``ple``, among others. 
In Python programming, the process of selecting substrings is usually called slicing, 
and a substring is often referred to as a slice of the string. The two terms can often be used interchangeably.

If you know the beginning and end indeces of the slice you wish to extract, you can 
do so with the notation [a:b]. This means the slice begins at the index ``a`` and ends at the last character before 
index ``b`` - that is, including the first, but excluding the last. 

Let's have a closer look at some sliced strings:
"""
# input_string = "presumptious"
#
# print(input_string[0:3])
# print(input_string[4:10])
#
# # if the beginning index is left out, it defaults to 0
# print(input_string[:3])
#
# # if the end index is left out, it defaults to the length of the string
# print(input_string[4:])

"""
In Python string processing the interval [a:b] is half open, which in this case means 
that the character at the beginning index ``a`` is included in the interval, but the character 
at the end index ``b`` is left out. 
Half open intervals may feel unintuitive, but in practice they do have some advantages. 
For example, you can easily calculate the length of a slice with ``b-a``. 
On the other hand, you must always remember that the character at the end index ``b`` will not be included in the slice.
"""

"""
Searching for substrings

The in operator can tell us if a string contains a particular substring. 
The Boolean expression a in b is true, if b contains the substring a.

For example, this bit of code
"""
# input_string = "test"
#
# print("t" in input_string)      # True
# print("x" in input_string)      # False
# print("es" in input_string)     # True
# print("ets" in input_string)    # False

"""
The program below lets the user search for substrings within a string hardcoded into the program:
"""
# input_string = "perpendicular"
#
# while True:
#     substring = input("What are you looking for? ")
#     if substring in input_string:
#         print("Found it")
#     else:
#         print("Not found")
#

"""
FIND Method

The operator in returns a Boolean value, so it will only tell us if a substring exists in a string, 
but it will not be useful in finding out where exactly it is. Instead, the Python string method find 
can be used for this purpose. It takes the substring searched for as an argument, and returns either 
the first index where it is found, or -1 if the substring is not found within the string.
"""
# input_string = "test"
#
# print(input_string.find("t"))       # 0
# print(input_string.find("x"))       # -1
# print(input_string.find("es"))      # 1
# print(input_string.find("ets"))     # -1

"""
The above substring search example implemented with find:
"""

# input_string = "perpendicular"
#
# while True:
#     substring = input("What are you looking for? ")
#     index = input_string.find(substring)
#     if index >= 0:
#         print(f"Found it at the index {index}")
#     else:
#         print("Not found")

"""
Above we used the string method find. 
Methods work quite similarly to the functions covered in the previous part. 
What distinguishes them from functions is that methods are always attached to the object they are called on. 
The object is the entity named before the method in the method call. In the case of find 
the object is the string where the method looks for the substring it has as an argument.
"""

"""
STRING Methods

str.capitalize()

This method returns a copy of the string with its first character capitalized and the others in lowercase.
"""
# cap = "i Enjoy traveling. Do you?".capitalize() # I enjoy traveling. do you?
# print(cap)

"""
str.lower()

This method returns a copy of the string with any character in uppercase to lowercase.
"""
# lower = "i Enjoy traveling. Do you?".lower()    # i enjoy traveling. do you?
# print(lower)

"""
str.replace(old, new[, count])

This method returns a string with all occurrences of the substring old substituted by the new. If the count 
argument is given, all count number of occurrences are replaced.
"""
sentence = "i Enjoy traveling. Do you?"
sentence.replace('Enjoy','dislike')             # "i dislike traveling. Do you?"
"Things fall apart".replace('a','e',1)   # "Things fell apart"

"""
More Examples
"""
# my_string = "hello world"
# print(my_string.upper())  # "HELLO WORLD"
# print(my_string.lower())  # "hello world"
#
# my_string = "   hello world   "
# print(my_string.strip())   # "hello world"
# print(my_string.lstrip())  # "hello world   "
# print(my_string.rstrip())  # "   hello world"

"""
Looping String with For-Loop

Strings are so called iterable objects (since the contain a sequence of characters). 
That means, we can iterate through them, using a for-loop
"""

# name = "LEON"
# for character in name:
#     print(character)
#
#
# my_string = "hello"
#
# # Using a while loop to iterate over each character in the string
# index = 0
# while index < len(my_string):
#     print(my_string[index])
#     index += 1
#
# my_string = "hello"
#
# # Using index to access each character in the string
# for i in range(len(my_string)):
#     print(my_string[i])


