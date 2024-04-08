"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# Write your solution here
def main():
  while True:
    print("Hello world!")
    answer = input("shall we continue? ")
    if answer == "no":
        print("okay then")
        break

if __name__ == "__main__":
    main()

"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""
# Write your solution here
from math import sqrt
def main():
    while True:
        number = int(input("Please type in a number: "))
        if number == 0:
            print("Exiting...")
            break
        elif number < 0:
            print("invalid number")
        else:
            print(sqrt(number))

if __name__ == "__main__":
    main()

"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""
# Fix the code
number = 5
print("Countdown!")
while number > 0:
  print(number)
  number = number - 1

print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# Write your solution here
def is_leap_year(year):
    # Leap years are divisible by 4
    # But if they are divisible by 100, they must also be divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def find_next_leap_year(current_year):
    next_year = current_year + 1
    while not is_leap_year(next_year):
        next_year += 1
    return next_year

def main():
    year = int(input("Year: "))
    next_leap_year = find_next_leap_year(year)
    print(f"The next leap year after {year} is {next_leap_year}")

if __name__ == "__main__":
    main()


"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""
# Write your solution here
def main():
    story = []
    while True:
        word = input("Please type in a word: ")
        if word == "end":
            break
        else:
            story.append(word)

    print(" ".join(story))

if __name__ == "__main__":
    main()

"""
Change the program above so that the loop ends also if the user types in the same word twice in a row.
"""
# Write your solution here
def main():
    story = []
    prev_word = None
    while True:
        word = input("Please type in a word: ")
        if word == "end":
            break
        elif word == prev_word:
            print("You've typed the same word twice in a row. Ending the story.")
            break
        else:
            story.append(word)
            prev_word = word

    print(" ".join(story))

if __name__ == "__main__":
    main()

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
# Write your solution here
def main():
    numbers = []
    positive_count = 0
    negative_count = 0

    while True:
        num = int(input("Please type in an integer number (0 to stop): "))
        if num == 0:
            break
        else:
            numbers.append(num)
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1

    num_count = len(numbers)
    num_sum = sum(numbers)
    if num_count > 0:
        mean = num_sum / num_count
    else:
        mean = 0

    print(f"Numbers typed in: {num_count}")
    print(f"The sum of the numbers is: {num_sum}")
    print(f"The mean of the numbers is: {mean}")
    print(f"Positive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")

if __name__ == "__main__":
    main()


"""
Largest Number

Write a program which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# Write your solution here
def largest_number():
    num = float(input("Number 1: "))
    if num <= 0:
        print("No number entered.")
        return

    largest = num
    count = 1

    while True:
        count += 1
        num = float(input(f"Number {count}: "))
        if num <= 0:
            break
        if num > largest:
            largest = num

    print(f"The largest number is {largest}")

largest_number()


"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# Write your solution here
def generate_output(n):
    if n <= 0:
        print("Invalid number!")
        return

    count = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()


try:
    n = int(input("n: "))
    generate_output(n)
except ValueError:
    print("Invalid input! Please enter a valid integer number.")


"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""
# Write your solution here
def create_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


rows = 6
create_pyramid(rows)


"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# Write your solution here
def calculate_average():
    total = 0
    count = 0
    negative_count = 0

    while True:
        mark = int(input(f"Mark {count + 1}: >> "))
        if mark == 0:
            break
        elif 1 <= mark <= 5:
            total += mark
            count += 1
            if mark == 5:
                negative_count += 1
        else:
            print("Invalid mark!")

    if count > 0:
        average = total / count
        print(f"Average: {average:.2f}")
        print(f"Negative marks: {negative_count}")
    else:
        print("No valid marks entered.")


calculate_average()
