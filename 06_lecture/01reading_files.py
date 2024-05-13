"""
A simple way to include files in a Python program is to use the with statement.
The header line opens the file, and the block where the file can be accessed follows.
After the block the file is automatically closed, and can no longer be accessed.

So, the following code opens the file, reads the contents, prints them out, and then closes the file:
"""
with open("example.txt") as new_file:
    contents = new_file.read()
    print(contents)

"""
Going through the contents of a file

The read method is useful for printing out the contents of the entire file, but more often we will want to go through the file line by line.

Text files can be thought of as lists of strings, each string representing a single line in the file. We can go through the list with a for loop.

The following example reads our example file using a for loop, removes line breaks from the end of each line, counts the number of lines, and prints each line with its line number. 
It also keeps track of the length of the lines:
"""
with open("example.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        line = line.replace("\n", "")
        count += 1
        print("Line", count, line)
        length = len(line)
        total_length += length

print("Total length of lines:", total_length)

"""
Split method
"""
text = "monkey,banana,harpsichord"
words = text.split(",")
for word in words:
    print(word)


"""
Reading CSV files
"""
with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades)



"""
Excel is notorious for adding extra whitespace. 
In names.csv we have an extra space character between the items, after each semicolon.

We would like to print out the last names of each person on the list. 
The first line contains the headers for the data, and it can be safely ignored:
"""
last_names = []
with open("names.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        # ignore the header line
        if parts[0] == "first":
            continue
        last_names.append(parts[1])

print(last_names)

last_names = []
with open("employees.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "first":
            continue # this was the header line, so it is ignored
        last_names.append(parts[1].strip())
print(last_names)


"""
Combining data from different files
"""

names = {}

with open("employees.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        names[parts[0]] = parts[1]

salaries = {}

with open("salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        salaries[parts[0]] = int(parts[1]) +int(parts[2])

print(names)
print(salaries)
print("incomes:")

for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")


"""
Reading JSON
"""
import json

with open("courses.json") as my_file:
    data = my_file.read()

courses = json.loads(data)
print(courses)

for course in courses:
    print(course["name"])