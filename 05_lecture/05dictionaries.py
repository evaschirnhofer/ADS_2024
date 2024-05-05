"""
Lists can be handy in many situations, but they are limited by the fact that the items are accessed through indexes; 0, 1, 2, and so forth.
If you want to find some item in a list, you will either have to know its index, or, at worst, traverse through the entire list.

Another central data structure in Python is the dictionary. In a dictionary, the items are indexed by keys.
Each key maps to a value. The values stored in the dictionary can be accessed and changed using the key.

The following example shows you how the dictionary data structure works. Here is a simple dictionary from German to English:
"""
my_dictionary = {}

my_dictionary["affe"] = "monkey"
my_dictionary["banane"] = "banana"
my_dictionary["lied"] = "song"

print(len(my_dictionary))       # 3
print(my_dictionary)            # {'affe': 'monkey', 'banane': 'banana', 'lied': 'song'}
print(my_dictionary["affe"])    # monkey

word = input("Please type in a word: ")
if word in my_dictionary:
    print("Translation: ", my_dictionary[word])
else:
    print("Word not found")


"""
All kinds of data types for either keys and values:
"""
results = {}
results["Mary"] = 4
results["Alice"] = 5
results["Larry"] = 2

lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2, 3]

"""
Unique keys in dictionaries

Each key can appear only once in the dictionary. If you add an entry using a key that already exists in the dictionary, 
the original value mapped to that key is replaced with the new value:
"""

my_dictionary["affe"] = "monkey"
my_dictionary["affe"] = "ape"
print(my_dictionary["affe"])    # ape

"""
All keys in a dictionary must be immutable. So, a list cannot be used as a key, because it can be changed. For example, executing the following code causes an error:
"""
# my_dictionary[[1, 2, 3]] = 5    # TypeError: unhashable type: 'list'

"""
The familiar for item in collection loop can be used to traverse a dictionary, too. When used on the dictionary directly, the loop goes through the keys stored in the dictionary, one by one. 
In the following example, all keys and values stored in the dictionary are printed out:
"""
my_dictionary = {}

my_dictionary["affe"] = "monkey"
my_dictionary["banane"] = "banana"
my_dictionary["lied"] = "song"

for key in my_dictionary:
    print("key:", key)
    print("value:", my_dictionary[key])

"""
Sometimes you need to traverse the entire contents of a dictionary. The method items returns all the keys and values stored in the dictionary, one pair at a time:
"""
for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)


"""
Advanced use cases for dictionaries

A dictionary can be a useful tool in managing this kind of information. 
In the example below, we go through the items in the list one by one. Using the words in the list as keys in a new dictionary, 
the value mapped to each key is the number of times the word has appeared:
"""
word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

def counts(my_list):
    words = {}
    for word in my_list:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    return words

# call the function
print(counts(word_list))    # {'banana': 1, 'milk': 1, 'beer': 3, 'cheese': 2, 'sourmilk': 3, 'juice': 1, 'sausage': 2, 'tomato': 1, 'cucumber': 1, 'butter': 2, 'margarine': 1, 'chocolate': 1}


"""
Categorize the words based on the initial letter in each word, using list from above.
One way to accomplish this would be to use dictionaries:
"""

def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups

groups = categorize_by_initial(word_list)

print(groups)   # {'b': ['banana', 'beer', 'butter', 'beer', 'butter', 'beer'], 'm': ['milk', 'margarine'], 'c': ['cheese', 'cucumber', 'cheese', 'chocolate'], 's': ['sourmilk', 'sausage', 'sausage', 'sourmilk', 'sourmilk'], 'j': ['juice'], 't': ['tomato']}

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)


"""
Removing keys and values from a dictionary

It is naturally possible to also remove key-value paris from the dictionary. There are two ways to accomplish this. The first is the command del:
"""

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["David"]
print(staff) # {'Alan': 'lecturer', 'Emily': 'professor'}

"""
If you try to use the del command to delete a key which doesn't exist in the dictionary, there will be an error:
"""
# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# del staff["Paul"]

"""
So, before deleting a key you should check if it is present in the dictionary:
"""
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
if "Paul" in staff:
  del staff["Paul"]
  print("Deleted")
else:
  print("This person is not a staff member")

"""
The other way to delete entries in a dictionary is the method pop:
"""
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("David")
print(staff)    # {'Alan': 'lecturer', 'Emily': 'professor'}
print(deleted, "deleted")   # lecturer deleted

"""
By default, pop will also cause an error if you try to delete a key which is not present in the dictionary. 
It is possible to avoid this by giving the method a second argument, which contains a default return value. 
This value is returned in case the key is not found in the dictionary. 
The special Python value None will work here:
"""
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("Paul", None)
if deleted == None:
  print("This person is not a staff member")
else:
  print(deleted, "deleted")

"""
DON'T USE LOOPS to delete the all key values! Use .clear() instead. Here is why:

You will receive an error message: RuntimeError: dictionary changed size during iteration.

When traversing a collection with a for loop, the contents may not change while the loop is in progress.

"""
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# for key in staff:
#   del staff[key]

staff.clear()


"""
Structuring data with dictionaries
"""
country1 = { "name": "USA", "capital": "Washington, D.C.", "language": ["English", "Spanish"], "population": 333300000}
country2 = { "name": "Austria", "capital": "Vienna", "language": ["German"], "population": 9042000}

countries = [country1, country2]

for country in countries:
    print(country["name"])

combined_population = 0
for country in countries:
    combined_population += country["population"]

print("The average population is ", combined_population/len(countries))