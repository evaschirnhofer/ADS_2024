"""
Conditional Statements and Comparison Operators in Python
"""

# Adjust "age" to get different results
age = 10

"""
Comparison Operators
"""

# Greater than
is_older_than_20 = age > 20
print(f"Is the person older than 20? {is_older_than_20}")
print(type(is_older_than_20))

# Less Than
is_younger_than_30 = age < 30
print(f"Is the person younger than 30? {is_younger_than_30}")

# Equal to
is_exactly_25 = age == 25
print(f"Is the person exactly 25 years old? {is_exactly_25}")

# Not equal to
is_not_35 = age != 35
print(f"Is the person not 35 years old? {is_not_35}")

# Greater than or equal to
is_at_least_25 = age >= 25
print(f"Is the person at least 25 years old? {is_at_least_25}")

# Less than or equal to
is_at_most_25 = age <= 25
print(f"Is the person at most 25 years old? {is_at_most_25}")

"""
Conditional Statements 
"""
# Basic if statement
if age >= 18:
    print("The person is considered an adult.")
    print("sdjssjd")

print("after if statement")

# if-else statement
if age >= 65:
    print("The person is a considered a senior.")
else:
    print("The person is not a senior.")

# if-elif-else chain
if age < 13:
    print("The person is a child.")
elif age < 18:
    print("The person is a teenager.")
else:
    print("The person is an adult.")

"""
Logical Operators (Combining Conditions)
"""
voting_age = 18
has_citizenship = True

# Logical "and"
can_vote = voting_age <= age and has_citizenship
print(f"Can the person vote? {can_vote}")

# Logical "or"
parents_attending = True
allowed_to_enter = age > 18 or parents_attending


