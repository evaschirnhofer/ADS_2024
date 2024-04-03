"""
Write a program which asks for two integer numbers.
The program should then print out whichever is greater.
If the numbers are equal, the program should print a different message.
Examples:
    Please type in the first number: >> 5
    Please type in another number: >> 3
    The greater number was: 5

    Please type in the first number: >> 5
    Please type in another number: >> 8
    The greater number was: 8

    Please type in the first number: >> 5
    Please type in another number: >> 5
    The numbers are equal!

"""
# Write your solution here
# Ask the user for the first number
first_number = int(input("Please type in the first number: "))

# Ask the user for the second number
second_number = int(input("Please type in another number: "))

# Compare the numbers
if first_number > second_number:
    print("The greater number was:", first_number)
elif second_number > first_number:
    print("The greater number was:", second_number)
else:
    print("The numbers are equal!")


"""
Python comparison operators can also be used on strings. 
String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if
- the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
- only the standard English alphabet of a to z, or A to Z, is used.

Write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Examples:
Please type in the 1st word: >> car
Please type in the 2nd word: >> scooter
scooter comes alphabetically last.

Please type in the 1st word: >> zorro
Please type in the 2nd word: >> batman
zorro comes alphabetically last.

Please type in the 1st word: >> python
Please type in the 2nd word: >> python
You gave the same word twice.

"""
# Write your solution here
first_word = str(input("Please type in a first word: "))
second_word = str(input("Please type in a second word: "))

if first_word > second_word:
    print(first_word, "comes alphabetically last.")
elif second_word > first_word:
    print(second_word, "comes alphabetically last.")
else:
    print("You gave the same word twice.")

"""
Write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

Examples:
    Please type in your name: >> Morty
    I think you might be one of Mickey Mouse's nephews.
    
    Please type in your name: >> Huey
    I think you might be one of Donald Duck's nephews.
    
    Please type in your name: >> Ken
    You're not a nephew of any character I know of.
"""
# Write your solution here
name = str(input("Please type in your name: "))

if name in ['huey', 'dewey', 'louie']:
    print("I think you might be one of Mickey Mouse's nephews.")
elif name in ["morty", "ferdie"]:
    print("I think you might be one of Donald Duck's nephews.")
else:
    print("You're not a nephew of any character I know of.")

"""
FizzBuzz
Write a program which asks the user for an integer number. 
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz. 
If the number is divisible by both three and five, the program should print out FizzBuzz.

Examples:
    Number: >> 9
    Fizz
    
    Number: >> 7
    
    Number: >> 20
    Buzz
    
    Number: >> 45
    FizzBuzz
"""
# Write your solution here
number = int(input("Number: "))

# Check if the number is divisible by both three and five
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
# Check if the number is divisible by three only
elif number % 3 == 0:
    print("Fizz")
# Check if the number is divisible by five only
elif number % 5 == 0:
    print("Buzz")
# If none of the above conditions are met, print the number itself
else:
    print(number)

"""
LeapYear
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

Examples:
    Please type in a year: >> 2011
    That year is not a leap year.
    
    Please type in a year: >> 2020
    That year is a leap year.
    
    Please type in a year: >> 1800
    That year is not a leap year.
"""
# Write your solution here
# Ask the user for a year
year = int(input("Please type in a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
