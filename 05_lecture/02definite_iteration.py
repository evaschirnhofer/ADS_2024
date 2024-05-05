"""
You can use a while loop to go through the items in a list, just like we used while loops to go through strings.
The following program prints out the items in the list, each on a separate line:
"""

my_list = [3, 2, 4, 5, 2]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1


"""
This obviously works, but it is a rather complicated way of going through a list, as you have to use a helper variable 
index to remember which item in the list you're at. Fortunately, Python offers a more intuitive way of traversing 
through lists, strings and other similar structures.

THE FOR LOOP

When you want to go through some ready collection of items, the Python for loop will do this for you. 
For instance, the loop can go through all items in a list from first to last.

When using a while loop the program doesn't "know" beforehand how many iterations the loop will perform. 
It will repeat until the condition becomes false, or the loop is otherwise broken out of. 
That is why it falls under indefinite iteration. With a for loop the number of iterations is determined when 
the loop is set up, and so it falls under definite iteration.

The idea is that the for loop takes the items in the collection one by one and performs the same actions on each. T
he programmer does not have to worry about which item is being handled when. The syntax of the for loop is as follows:

for <variable> in <collection>:
    <block>
"""

my_list = [3, 2, 4, 5, 2]

for item in my_list:
    print(item)


"""
Range and For loop

Often you know how many times you want to repeat a certain bit of code. You might, for example, wish to go through all the numbers between 1 and 100. The range function plugged into a for loop will do this for you.

There are a few different ways to call the range function. The simplest way is to give the function just one argument, 
which signifies the end-point of the range. The end-point itself is excluded, just like with string slices. 
In other words, the function call range(n) provides a loop with a range from 0 to n-1:
"""

for i in range(5):
    print(i, end="") # prints 01234

"""
With two arguments, the function will return a range between the two numbers. The function range(a,b) provides a range starting from a and ending at b-1:
"""
for i in range(3, 7):
    print(i, end="") # prints 3456

"""
Finally, with a third argument you can also specify the size of the step the range takes between each value. 
The function call range(a, b, c) provides a range starting from a, ending at b-1, and changing by c with every step:
"""
for i in range(1, 9, 2):
    print(i, end="") # prints 1357

"""
A step can also be negative. Then the range will be in reversed orded. Notice the first two arguments are also flipped here:
"""
for i in range(6, 2, -1):
    print(i, end="") # prints 6543


"""
The function range returns a range object, which in many ways behaves like a list, but isn't actually one. 
If you try printing out the value the function returns, you will only see a description of a range object:
"""

numbers = range(2, 7)
print(numbers) # prints range(2, 7)

"""
The function list will convert a range into a list. The list will contain all the values that are in the range. 
The Advanced Course in Programming course, which follows this one, will shed more light on this subject.
"""
numbers = list(range(2, 7))
print(numbers) # prints [2, 3, 4, 5, 6]