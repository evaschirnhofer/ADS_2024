"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""
# Write your solution here
# Ask the user for a number
number = int(input("Enter a number: "))

# Determine if the number is even or odd using the modulo operator
remainder = number % 2

# Check if the remainder is 0 (even) or 1 (odd)
if remainder == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
# Write your solution here
#
# Ask the user for their exam grade (as a percentage)
grade = float(input("Enter your exam grade (as a percentage): "))

# Check the grade and print out the appropriate message
if grade < 50:
    print("Unfortunately, you failed the exam.")
elif grade >= 90:
    print("You are excellent!")
else:
    print("You passed the exam!")


"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""
# Write your solution here
# Ask the user for their lunch choice
choice = input("Would you like a sandwich, salad, or wrap? "

if choice == 'sandwich':
    sandwich_type = input("What kind of sandwich would you like? (chicken, beef, veggie) ")
    print(f"Your order: {sandwich_type} sandwich")
elif choice == 'salad':
    dressing = input("What kind of dressing would you like? (vinaigrette, ranch, caesar) ")
    print(f"Your order: Salad with {dressing} dressing")
elif choice == 'wrap':
    toasted = input("Would you like your wrap toasted? (yes/no) >> ")
    if toasted == 'yes':
        print("Your order: Toasted wrap")
    else:
        print("Your order: Wrap")
else:
    print("Invalid choice!")