"""
LISTS
"""

"""
LIST INITIALIZATION
Lists can be initialized with square brackets containing elements.
"""

numbers = [1, 2, 3, 4, 5]
print(numbers)  # prints: [1, 2, 3, 4, 5]

"""
ACCESSING ITEMS
Items in a list can be accessed using their index, starting from 0.
"""

first_item = numbers[0]
print(first_item)  # prints: 1

"""
MUTABILITY
Lists are mutable, meaning their elements can be changed.
"""

numbers[0] = 10
print(numbers)  # prints: [10, 2, 3, 4, 5]

"""
APPEND METHOD
Items can be appended to the end of the list using the append() method.
"""

numbers.append(6)
print(numbers)  # prints: [10, 2, 3, 4, 5, 6]

"""
INSERT METHOD
Items can be inserted at any position using the insert() method.
"""

numbers.insert(0, 0)  # Inserts 0 at the index 0
print(numbers)  # prints: [0, 10, 2, 3, 4, 5, 6]

"""
REMOVING ITEMS
Items can be removed by value with remove(), and by index with pop().
"""

numbers.remove(10)  # Removes the first occurrence of 10
print(numbers)  # prints: [0, 2, 3, 4, 5, 6]
popped_item = numbers.pop(0)  # Removes and returns the item at index 0
print(popped_item)  # prints: 0
print(numbers)  # prints: [2, 3, 4, 5, 6]

"""
SORT METHOD
Lists can be sorted in place using the sort() method.
"""

numbers.sort()
print(numbers)  # prints: [2, 3, 4, 5, 6]

"""
SORTING FUNCTION
The sorted() function returns a new sorted list without altering the original.
"""

new_numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(new_numbers)
print(sorted_numbers)  # prints: [1, 1, 3, 4, 5]
print(new_numbers)  # prints: [3,1,4,1,5]

"""
MIN, MAX, AND SUM FUNCTIONS
The min(), max(), and sum() functions can be used to find the minimum, maximum, and the sum of the elements.
"""

print(min(numbers))  # prints: 2
print(max(numbers))  # prints: 6
print(sum(numbers))  # prints: 20

"""
SLICING LISTS WITHOUT STEP AND WITH STEP
Lists can be sliced to create sublists, specifying start, stop, and step indices.
"""

sublist = numbers[1:4]  # Slices from index 1 to 3
print(sublist)  # prints: [3, 4, 5]
stepped_sublist = numbers[0:5:2]  # Slices from index 0 to 4 with a step of 2
print(stepped_sublist)  # prints: [2, 4, 6]
