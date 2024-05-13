"""
Return vs Print statement

User input vs function input parameter

"""
import random


def greet_user():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def get_user_guess(input_prompt_message: str) -> int:
    guess = input(input_prompt_message)
    guess = int(guess)
    return guess

def check(secret_number, guessed_number) -> bool:
    if guessed_number < secret_number:
        print("Too low! Try again.")
        return False
    elif guessed_number > secret_number:
        print("Too high! Try again.")
        return False
    else:
        return True
        # print(f"Congratulations! You've guessed the number {secret_number} correctly!")
        # print(f"It took you {attempts} attempts.")
        # break

# Simple number guessing game.
def guess_number():
    greet_user()

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        guess = get_user_guess("\nEnter your guess (1-100): ")

        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        correct_guess = check(secret_number, guess)

        if correct_guess == True:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break
        else:
            continue

        # if guess < secret_number:
        #     print("Too low! Try again.")
        # elif guess > secret_number:
        #     print("Too high! Try again.")
        # else:
        #     print(f"Congratulations! You've guessed the number {secret_number} correctly!")
        #     print(f"It took you {attempts} attempts.")
        #     break


guess_number()

if __name__ == '__main__':
    guess_number()

