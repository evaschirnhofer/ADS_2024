"""
Write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary.
The number is the key, and the factorial of that number is the value mapped to it.

A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself.
For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

An example of the function in action:
    k = factorials(5)
    print(k[1]) # 1
    print(k[3]) # 6
    print(k[5]) # 120
"""
# Provide your solution here

"""
Write a function named histogram, which takes a string as its argument. The function should print out a histogram 
representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented 
by a star on the specific line for that letter.

For example, the function call histogram("abba") should print out
    a **
    b **
while histogram("statistically") should print out
    s **
    t ***
    a **
    i **
    c *
    l **
    y *
"""
# Provide your solution here

"""
Write a phone book application. It should work as follows:

    command (1 search, 2 add, 3 quit): >> 2
    name: >> peter
    number: >> 040-5466745
    ok!
    command (1 search, 2 add, 3 quit): >> 2
    name: >> emily
    number: >> 045-1212344
    ok!
    command (1 search, 2 add, 3 quit): >> 1
    name: >> peter
    040-5466745
    command (1 search, 2 add, 3 quit): >> 1
    name: >> mary
    no number
    command (1 search, 2 add, 3 quit): >> 2
    name: >> peter
    number: >> 09-22223333
    ok!
    command (1 search, 2 add, 3 quit): >> 1
    name: >> peter
    09-22223333
    command (1 search, 2 add, 3 quit): >> 3
    quitting...

As you can see above, each name can be attached to a single number only. 
If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.
"""
# Provide your solution here

"""
Please write an improved version of the phone book application. 
Each entry should now accommodate multiple phone numbers. 
The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.

    command (1 search, 2 add, 3 quit): >> 2
    name: >> peter
    number: >> 040-5466745
    ok!
    command (1 search, 2 add, 3 quit): >> 2
    name: >> emily
    number: >> 045-1212344
    ok!
    command (1 search, 2 add, 3 quit): >> 1
    name: >> peter
    040-5466745
    command (1 search, 2 add, 3 quit): >> 1
    name: >> mary
    no number
    command (1 search, 2 add, 3 quit): >> 2
    name: >> peter
    number: >> 09-22223333
    ok!
    command (1 search, 2 add, 3 quit): >> 1
    name: >> peter
    040-5466745
    09-22223333
    command (1 search, 2 add, 3 quit): >> 3
    quitting...
"""
# Provide your solution here


"""
Write a function named invert(dictionary: dict), which takes a dictionary as its argument. 
The dictionary should be inverted in place so that values become keys and keys become values.

An example of its use:
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)    # {"first": 1, "second": 2, "third": 3, "fourth": 4}
"""
# Provide your solution here


"""
Write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.

The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.

    name
    director
    year
    runtime
    
The values attached to these keys are given as arguments to the function.

An example of its use:
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database) # [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
"""
# Provide your solution here

"""
Write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. 
The function should formulate a new list, which contains only the movies whose title includes the word searched for. 
Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.

An example of its use:

    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
    
    my_movies = find_movies(database, "python")
    print(my_movies)    # [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
"""
# Provide your solution here