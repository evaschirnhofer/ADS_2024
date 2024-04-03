"""
Write a program which asks the user for a number.
The program then prints out the number multiplied by five.
Example:
    Please type in a number: >> 7
    7 times 5 is 35
"""
# Write your solution here
# Ask the user for a number
number = input("Please type in a number: ")

# Convert the input to an integer
number = int(number)

# Multiply the number by 5
result = number * 5

# Print the result
print(f"{number} times 5 is {result}")


"""
Write a program which asks the user for their name and year of birth. 
The program then prints out a message as follows:
    What is your name? >> Frances Fictitious
    Which year were you born? >> 1990
    Hi Frances Fictitious, you will be 34 years old at the end of the year 2024
"""
# Write your solution here

# Ask the user for their name
name = input("What is your name? ")
# Ask the user for their year of birth
year_of_birth = input("Which year were you born? ")
# Convert the input to an integer
year_of_birth = int(year_of_birth)
# Calculate the age
current_year = 2024
age = current_year - year_of_birth
# Print out the message
print(f"Hi {name}, you will be {age} years old at the end of the year {current_year}.")


"""
Write a program which asks the user for a number of days. 
The program then prints out the number of seconds in the amount of days given.
Example:
    How many days? >> 7
    Seconds in that many days: >> 604800
"""
# Write your solution here
# Ask the user for the number of days
days = int(input("How many days? "))
# Calculate the number of seconds in the given number of days
seconds = days * 24 * 60 * 60  # 1 day = 24 hours * 60 minutes * 60 seconds
# Print out the result
print(f"Seconds in that many days: {seconds}")


"""
This program asks the user for three numbers. 
The program then prints out their product, that is, the numbers multiplied by each other. 
There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. 
Please fix it.
"""
# Fix the code
number = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number * number2 * number2

print("The product is", product)


"""
Write a program which asks the user for four numbers. 
The program then prints out the sum and the mean of the numbers.
Example: 
    Number 1: >> 2
    Number 2: >> 1
    Number 3: >> 6
    Number 4: >> 7
    The sum of the numbers is 16 and the mean is 4.0
"""
# Write your solution here
# Initialize variables to hold sum and count
total_sum = 0
count = 0

# Iterate to get four numbers from the user
for i in range(4):
    # Ask the user for a number
    num = float(input(f"Number {i + 1}: >> "))

    # Add the number to the sum
    total_sum += num

    # Increment the count
    count += 1

# Calculate the mean
mean = total_sum / count

# Print out the sum and mean
print(f"The sum of the numbers is {total_sum} and the mean is {mean}.")

"""
Write a program that asks the user for a three-digit number input.
Reverse the given number by using modulo and division operator.
Example:
    Enter a number: >> 123
    The reversed number is: >> 321
"""
# Write your solution here

# Ask the user for a three-digit number input
number = int(input("Enter a three-digit number: "))

# Reverse the given number using modulo and division operator
reversed_number = 0

# Extract digits from the input number and reverse it
while number != 0:
    digit = number % 10  # Extract the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number = number // 10  # Remove the last digit from the number

# Print the reversed number
print("The reversed number is:", reversed_number)
