"""
Analyse the code below and try to find out what it does!

Even though you don't know a lot of the keywords yet, you might be able to understand what's going on by reading the
code line by line. To start out, you can try to "translate" the code in natural language.

You can run the code by clicking the green Play-Button on the top right of your screen or by pressing Shift + F10
"""


def apply_printing_format_to_number(number):
    return str(round(number, 2))


name = input("What is your name?\n")
budget = float(input("What's your current budget?\n"))
print("Hello, " + name + "! Your budget is " + apply_printing_format_to_number(budget) + "€. Let's go shopping!")

groceries_to_buy = [
    ["Apple", 5, 0.45],
    ["Banana", 8, 0.80],
    ["Onion", 4, 0.70],
    ["Milk", 1, 1.90],
    ["Bread", 3, 3.50],
    ["Fish", 2, 16.90],
    ["Cake", 1, 12.60],
    ["Steaks", 4, 9.95],
]

sum_total = 0
items_total = 0

print("The following items are on your grocery-list:")
for item in groceries_to_buy:
    item_name, qty, price = item
    print(str(qty) + "x " + item_name + " á " + apply_printing_format_to_number(price) + "€")

    items_total = items_total + qty
    sum_total = sum_total + (qty * price)

budget_difference = budget - sum_total
average_price = sum_total / items_total

print("---")
print("Total items bought:", items_total)
print("Total sum to pay: " + apply_printing_format_to_number(sum_total) + "€")
print("The average price is " + apply_printing_format_to_number(average_price) + "€ per item.")
print("---")

if budget_difference < 0:
    print("Sorry, you have made " + apply_printing_format_to_number(budget_difference * (-1)) + "€ in debt!")
elif budget_difference > 0:
    print(
        "Congratulation, after buying your groceries, you have " + apply_printing_format_to_number(budget_difference) +
        "€ left!")
else:
    print("You have bought all your groceries but no more money!")

print("Goodbye " + name + "!")
