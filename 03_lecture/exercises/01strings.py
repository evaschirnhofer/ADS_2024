"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# Write your solution here
string = str(input("Please type in a string: "))
amount = int(input("Please type in an amount: "))

print(string * amount, end="")


"""
Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""

# Write your solution here
string1 = str(input("Please type in string 1: "))
string2 = str(input("Please type in string 2: "))

if len(string1) < len(string2):
    print(f"{string2} is longer")
elif len(string2) < len(string1):
    print(f"{string1} is longer")
else:
    print("The strings are equally long")


"""
Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
# Write your solution here
# Ask the user for a string
user_string = input("Please type in a string: ")

# Print the string in reversed order using positive indices
for i in range(len(user_string) - 1, -1, -1):
    print(user_string[i])

# Ask the user for a string
user_string = input("Please type in a string: ")

# Print the string in reversed order using negative indices
for i in range(-1, -len(user_string) - 1, -1):
    print(user_string[i])


"""
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# Write your solution here
give_string = str(input("Please type in a string: "))
index = 0

if give_string[1] == give_string[-2]:
    print("The second and the second to last characters are the same")
else:
    print("The second and the second to last characters are different")


"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# Write your solution here
width = int(input("Width: "))
print("#" * width)

"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# Write your solution here
width1 = int(input("Width: "))
height = int(input("Height: "))

for _ in range(height):
    print("#" * width)

"""
Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# Write your solution here
# Ask the user for a string
user_string = input("Please type in a string: ")

# Calculate the number of * characters needed to fill the line
asterisks_count = max(20 - len(user_string), 0)

# Print the string with leading * characters to make the total length 20
print('*' * asterisks_count + user_string)


"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing
    
    ******************************
    *          testing           *
    ******************************

    Word: >> python
    
    ******************************
    *           python           *
    ******************************
"""
# Write your solution here
# Ask the user for a word
word = input("Word: ")

# Calculate the remaining space for padding
padding = 30 - len(word)

# Calculate the padding on each side of the word
left_padding = padding // 2
right_padding = padding - left_padding

# Print the frame with the word centered
print('*' * 30)
print('*' + ' ' * left_padding + word + ' ' * right_padding + '*')
print('*' * 30)


"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# Write your solution here
string3 = str(input("Please type in a string: "))

for i in range(1, len(string3) + 1):
    print(string3[:i])

"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    st
    est
    test
"""
# Write your solution here
string4 = str(input("Please type in a string: "))
for i in range(len(string4)):
    print(string4[i:])

"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# Write your solution here
string5 = str(input("Please type in a string: "))

if "a" in string5:
    print("a found")
else:
    print("a not found")

if "e" in string5:
    print("e found")
else:
    print("e not found")

if "o" in string5:
    print("o found")
else:
    print("o not found")

"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
    Please type in a word: >> python
    Please type in a character: >> n
"""
# Write your solution here
word1 = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))

index = word.find(character)

if index != -1 and index <= len(word) - 3:
    print(word[index:index+3])

"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# Write your solution here
string6 = str(input("Please type in a string: "))
substring = str(input("Please type in a substring: "))

# Find the index of the first occurrence of the substring
first_index = string6.find(substring)

if first_index == -1:
    print("The substring does not occur in the string.")
else:
    # Find the index of the second occurrence of the substring
    second_index = string6.find(substring, first_index + len(substring))

    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")

