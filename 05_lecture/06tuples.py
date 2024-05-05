"""
Tuples

Tuple is a data structure which is, in many ways, similar to a list. The most important differences between the two are:
    Tuples are enclosed in parentheses (), while lists are enclosed in square brackets []
    Tuples are immutable, while the contents of a list may change
The following bit of code creates a tuple containing the coordinates of a point:
"""
point = (10, 20)

"""
The items stored in a tuple are accessed by index, just like the items stored in a list:
"""
point = (10, 20)
print("x coordinate:", point[0])    # x coordinate: 10
print("y coordinate:", point[1])    # y coordinate: 20

"""
The values stored in a tuple cannot be changed after the tuple has been defined. The following will not work:
"""
point = (10, 20)
# point[0] = 15   # TypeError: 'tuple' object does not support item assignment


"""
Because tuples are immutable, unlike lists, they can be used as keys in a dictionary. The following bit of code creates 
a dictionary, where the keys are coordinate points:
"""
points = {}
points[(3, 5)] = "monkey"
points[(5, 0)] = "banana"
points[(1, 2)] = "song"
print(points[(3, 5)])   # monkey


"""
Tuples without parentheses

The parentheses are not strictly necessary when defining tuples. The following two variable assignments are identical in their results:
"""
numbers = (1, 2, 3)
numbers = 1, 2, 3

# This means we can also easily return multiple values using tuples. Let's have alook at he following example:
def minmax(my_list):
  return min(my_list), max(my_list)

my_list = [33, 5, 21, 7, 88, 312, 5]

min_value, max_value = minmax(my_list)
print(f"The smallest item is {min_value} and the greatest item is {max_value}") # The smallest item is 5 and the greatest item is 312

my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"

for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)