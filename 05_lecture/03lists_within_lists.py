"""
Any types of values can be stored in lists. A list of strings could look like this:
"""

names = ["Marlyn", "Ruth", "Paul"]
print(names) # ['Marlyn', 'Ruth', 'Paul']
names.append("David")
print(names) # ['Marlyn', 'Ruth', 'Paul', 'David']

print("Number of names on the list:", len(names))
print("Names in alphabetical order:")
names.sort()
for name in names:
  print(name)

"""
Floating point numbers are also valid list items:
"""
measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]

for measure in measurements:
    print(f"{measure} ", end="") # -2.5 1.1 7.5 14.6 21.0 19.2

mean = sum(measurements) / len(measurements)

print()
print("The mean is:", mean)

"""
The items in a list can be lists themselves:
"""
my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
print(my_list)      # [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
print(my_list[1])   # [4, 1]
print(my_list[1][0])# 4


"""
Remember that lists can contain items of different types. You could store information about a person in a list. 
For instance, you could include their name as the first item, their age as the second item, and their height in meters as the third item:
"""
persons = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]

for person in persons:
  name = person[0]
  age = person[1]
  height = person[2]
  print(f"{name}: age {age} years, height {height} meters")

"""
MATRICES

A two-dimensional array, or a matrix, is also a natural application of a list within a list.
"""

my_matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

print(my_matrix[0][1]) # 2
my_matrix[1][0] = 10
print(my_matrix)       # [[1, 2, 3], [10, 2, 1], [4, 5, 6]]


"""
Like any other list, the rows of the matrix can be traversed wth a for loop. The following code prints out each row of the matrix on a separate line:
"""
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print(row)

"""
Likewise, nested loops can be used to access the individual elements. The following code prints out each element in the matrix on a separate line with the help of two for loops:
"""
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print("a new row")
    for element in row:
        print(element)

"""
Accessing a single row within a matrix is simple - just choose the desired row. The following function calculates the sum of the elements on a chosen row:
"""
def sum_of_row(my_matrix, row_no: int):
    # choose the desired row from within the matrix
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item

    return row_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_row(m, 1)
print(my_sum) # prints out 33 (which equals 9 + 1 + 12 + 11)

"""
Working with columns within a matrix is slightly more complicated, as the matrix is stored by rows:
"""
def sum_of_column(my_matrix, column_no: int):
    # go through each row and select the item at the chosen position
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]

    return column_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_column(m, 2)
print(my_sum) # prints out 39 (which equals 3 + 12 + 9 + 15)


"""
Sudoku Grid example
"""

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

def print_grid(sudoku):
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print()

print_grid(sudoku)