"""
WHILE Loop

A while loop in Python is a control flow statement that allows you to repeatedly execute a block of code
as long as a specified condition is true. It has the following syntax:
    while condition:
        # Code block to be executed repeatedly
        # as long as the condition is true

1. The condition is evaluated before executing the loop body. If the condition is true, the loop body is executed.
2. After executing the loop body, the condition is evaluated again. If it's still true, the loop body is executed again. This process continues until the condition becomes false.
3. Once the condition becomes false, the control exits the loop, and the program continues with the code that follows the loop.
"""
# i = 1
# while i <= 5:
#     print("Hello World!")
#     i = i + 1
#
# j = 1
# while j < 10:
#     print(j) # print(j, end="")
#     j += 1

"""
While True - infinite loops
A "while True" loop, also known as an infinite loop, is a construct in Python where the loop condition is always True. 
This results in a loop that continues indefinitely until it's explicitly terminated or interrupted.
To stop the loop we need to use the "break" statement, which stops the loop - the program will continue to execute after the loop block.
"""
# while True:
#     number = int(input("Please type in a number, -1 to quit: "))
#
#     if number == -1:
#         break # if this line is reached the program stops looping and resumes with the "after loop block" print statement
#
#     print(number ** 2)
#
# print("After loop block. Thanks and bye!")
#
#
# while True:
#     code = input("Please type in your PIN: ")
#     if code == "1234":
#         break
#     print("Incorrect...try again")
#
# print("Correct PIN entered!")


"""
Break vs Condition
"""

# # 1st version using the break command
# sum = 0
#
# while True:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number == -1:
#         break
#     sum += number
#
# print (f"The sum is {sum}")
#
# # 2nd version without the break command
#
# sum = 0
# number = 0
#
# while number != -1:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number != -1:
#         sum += number
#
# print (f"The sum is {sum}")

"""
Continue vs Break
break:
    When encountered inside a loop, the break statement terminates the loop immediately, regardless of whether 
    the loop condition has been evaluated to True or not.
    It is commonly used to prematurely exit a loop when a certain condition is met.
continue:
    Unlike break, the continue statement doesn't terminate the loop; instead, it skips the remaining code inside 
    the loop for the current iteration and moves on to the next iteration.
    It is typically used to skip specific iterations or values within a loop.
"""

# sum = 0
#
# while True:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number == -1:
#         break
#     if number >= 10:
#         continue
#     sum += number
#
# print (f"The sum is {sum}")

"""
Nested Loops
Nested loops in programming refer to the situation where one loop is placed inside another loop. 

Nested loops are used for various purposes, including:
    Matrix Operations: When dealing with matrices or multi-dimensional lists, nested loops are commonly used 
    to iterate over each element in the matrix.
    
    Searching and Sorting Algorithms: Many searching and sorting algorithms involve nested loops. For example, 
    in a two-dimensional list, nested loops might be used to compare each element with every other element for sorting purposes.
    
    Pattern Printing: Nested loops are often used to print patterns, such as triangles, rectangles, or other shapes.
    
    Generating Combinations and Permutations: Nested loops can be used to generate combinations or permutations of elements.
    
    Traversal of Hierarchical Data Structures: Nested loops are useful for traversing hierarchical data structures such 
    as trees or graphs, where each node may have multiple children.
"""

# number = int(input("Please type in a number: "))
# while number > 0:
#     i = 0
#     while i < number:
#         print(f"{i} ", end="")
#         i += 1
#     print()
#     number -= 1

"""
Pattern printing example.
"""
# rows = 5
#
# # Outer loop for rows
# i = 1
# while i <= rows:
#     # Inner loop for columns
#     j = 1
#     while j <= i:
#         print("*", end=" ")  # Print asterisk
#         j += 1
#     print()  # Move to the next line after printing each row
#     i += 1

"""
PIN and number attempts

The following program keeps asking the user for a PIN code until they type in the correct one, which is 1234.
The program the prints the number of attempts.
"""
# attempts = 0
# pin = 1234
#
# while True:
#     number = int(input("PIN:"))
#     attempts += 1
#     if number == pin:
#         break
#     else:
#         print("Wrong")
#
# if attempts == 1:
#     print("Correct! It only took you one single attempt!")
# else:
#     print("Correct! It took you 4 attempts.")

"""
Concatenating strings with the + operator

The above example with PIN checking used a helper variable attempts to keep track of how many times 
the user had tried to type in a code. A similar idea of incrementation works with string variables as well. 
The program could, for instance, keep track of all the PIN codes the user typed in:
"""

# codes = ""
# attempts = 0
# pin = "1234"
#
# while True:
#     code = input("Please type in your PIN: ")
#     attempts += 1
#     codes += code + ", "
#     attempts += 1
#     if code == pin:
#         break
#     else:
#         print("Wrong")
#
# print("Correct! Your attempts: " + codes)
