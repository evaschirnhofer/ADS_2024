"""
Regular expressions
"""
# import re to use regular expression features in python
import re


words = ["Python", "Pantone", "Pontoon", "Pollute", "Pantheon"]

for word in words:
    # the string should begin with "P" and end with "on"
    if re.search("^P.*on$", word):
        print(word, "found!")


sentence = "First, 2 !#third 44 five 678xyz962"

numbers = re.findall("\d+", sentence)

for number in numbers:
    print(number)



print("Test your regular expressions here:")

# expression = input("Please type in an expression: ")
#
# while True:
#     input_string = input("Please type in a string: ")
#     if input_string == "":
#         break
#     if re.search(expression, input_string):
#         print("Found!")
#     else:
#         print("Not found.")



def check_match(regex: str, input_string: str) -> str:
    if re.search(regex, input_string):
        return f"MATCH '{input_string}' with regex '{regex}'"
    else:
        return f"NO match '{input_string}' and regex '{regex}'"

# The vertical bar |, also called the pipe character, allows you to match alternate substrings
print(check_match("aa|ee|ii", "aardvark"))
# Square brackets are used to signify groups of accepted characters.
print(check_match("[C-FRSO]", "C"))

#* repeats for any number of times, including zero
#+ repeats for any number of times, but at least once
#{m} repeats for exactly m times
print(check_match("1[234]*5", "125"))
print(check_match("1[234]*5", "127"))
print(check_match("1[234]+5", "15"))

# The ^ character specifies that the match must be at the beginning of the string,
# and $ specifies that the match must be at the end of the string
print(check_match("^[123]*$", "333333"))

# escape characters with "\"
print(check_match("^\*", "*moi"))

# round brackets can be used to group together different parts of the expression
print(check_match("^(jabba).*(hut)$", "jabba the hut"))
print(check_match("^(jabba).*(hut)$", "jabba a hut"))

