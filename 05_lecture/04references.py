"""
Thus far we have thought of a variable as a sort of a "box" which contains the value of the variable.
Technically this is not true in Python. What is stored in a variable is not the value per se, but a reference to the object which is the actual value of the variable.
The object can be e.g. a number, a string or a list.

In practice, this means that the value of the variable is not stored in the variable itself.
Instead, there is information about the location in computer memory where the value can be found.

The function "id" can be used to find out the exact location the variable points to.
The reference, or the ID of the variable, is an integer, which can be thought of as the address in computer memory where
the value of the variable is stored. If you execute the below code on your own computer, the result will likely be different,
as your variables will point to different locations - the references will be different.
"""
a = [1, 2, 3]
print(id(a))    # 2017306800960
b = "This is a reference, too"
print(id(b))    # 2017306988576


"""
What actually happens when you assign a list variable to a new variable - is the list copied over?
"""
a = [1, 2, 3]
b = a
b[0] = 10

list1 = [1, 2, 3, 4]
list2 = list1

list1[0] = 10
list2[1] = 20

print(list1)    # [10, 20, 3, 4]
print(list2)    # [10, 20, 3, 4]


"""
Copying a list
"""

my_list = [1, 2, 3, 3, 5]

new_list = []
for item in my_list:
    new_list.append(item)

new_list[0] = 10
new_list.append(6)
print("the original:", my_list) # the original: [1, 2, 3, 3, 5]
print("the copy:", new_list)    # the copy: [10, 2, 3, 3, 5, 6]

"""
An easier way to copy a list is the bracket operator [],  which we used for slices previously. The notation [:] selects all items in the collection. 
As a side effect, it creates a copy of the list:
"""
my_list = [1,2,3,4]
new_list = my_list[:]

my_list[0] = 10
new_list[1] = 20

print(my_list)  # [10, 2, 3, 4]
print(new_list) # [1, 20, 3, 4]