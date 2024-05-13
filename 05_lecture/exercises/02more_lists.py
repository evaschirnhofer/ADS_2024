"""
Write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

    ***
    *******
    *
    *
    **

"""
# Provide your solution here
def list_of_stars(star_counts):
    for count in star_counts:
        print('*' * count)

# Test the function
list_of_stars([3, 7, 1, 1, 2])


"""
Write a function named anagrams, which takes two strings as arguments. 
The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
"""
# Provide your solution here
def anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

# Test the function
print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False

"""
Write a function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.

    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result) # prints The result is 9

"""
# Provide your solution here
def sum_of_positives(nums):
    return sum(num for num in nums if num > 0)

# Test the function
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)  # prints The result is 9

# This function utilizes a generator expression to iterate through the list of integers (nums)
# and sum up only the positive values.

from typing import List

def sum_of_positives(nums: List[int]) -> int:
    positive_sum = 0
    for num in nums:
        if num > 0:
            positive_sum += num
    return positive_sum

# Test the function
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)  # prints The result is 9

# with a Loop

"""
Write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    Prints:
        original [1, 2, 3, 4, 5]
        new [2, 4]
"""
# Provide your solution here
def even_numbers(nums):
    return [num for num in nums if num % 2 == 0]

# Test the function
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

# for uneven numbers:
def uneven_numbers(nums):
    return [num for num in nums if num % 2 != 0]

# Test the function
my_list = [1, 2, 3, 4, 5]
uneven_list = uneven_numbers(my_list)
print("original", my_list)
print("uneven", uneven_list)

# without num for
def even_numbers(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Test the function
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)


"""
Write a function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the two original lists. 
You may assume both lists have the same number of items.

An example of the function at work:

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
"""
# Provide your solution here
def list_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

# Test the function
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))  # [8, 10, 12]


# without zip:
from typing import List


def list_sum(list1: List[int], list2: List[int]) -> List[int]:
    # Create a new list to store the sums
    result = []

    # Iterate over the indices of the lists
    for i in range(len(list1)):
        # Add the elements at the same index and append to the result list
        result.append(list1[i] + list2[i])

    return result

# Test the function
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))  # Output: [8, 10, 12]

# calling functions (for example with empty list)

# how to iterate a list:
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(my_list[i])

my_list = [1, 2, 3, 4, 5]
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")

my_list = [1, 2, 3, 4, 5]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# searching within lists:
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list")

my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print("Index of 3:", index)

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    if item == 3:
        print("Found 3 in the list")
        break

my_list = [1, 2, 3, 3, 4, 5, 3]
count_of_3 = my_list.count(3)
print("Count of 3:", count_of_3)


my_list = [1, 2, 3, 4, 5]
found = [item for item in my_list if item == 3]
if found:
    print("Found 3 in the list")

# comparing values in lists:
# Checking if Two Lists Are Equal:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
    print("The lists are equal")

# Checking if Two Lists Have the Same Elements (Regardless of Order):
list1 = [1, 2, 3]
list2 = [3, 2, 1]
if sorted(list1) == sorted(list2):
    print("The lists have the same elements")

# Checking if a Value Exists in a List:
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list")

# Checking if Two Lists Have the Same Length:
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
if len(list1) == len(list2):
    print("The lists have the same length")

# Comparing Lists Element-wise:
list1 = [1, 2, 3]
list2 = [1, 4, 3]
if all(x == y for x, y in zip(list1, list2)):
    print("The lists are equal element-wise")

# how to return a value:
def my_function():
    # Do something...
    result = 42
    return result

# Call the function and store the returned value
returned_value = my_function()

# Print the returned value
print("Returned value:", returned_value)

# multiple values:
def my_function():
    # Do something...
    value1 = 42
    value2 = "Hello"
    return value1, value2

# Call the function and store the returned values
returned_value1, returned_value2 = my_function()

# Print the returned values
print("Returned value 1:", returned_value1)
print("Returned value 2:", returned_value2)
