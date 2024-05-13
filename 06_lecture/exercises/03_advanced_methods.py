with open("..\Bee Movie Script.txt") as bee_script:
    bee_script = [line for line in bee_script.readlines()]

with open("..\Calories.txt") as calories:
    calories = [line for line in calories.readlines()]

def countWordOccurences():
    """
    Count the number of times each word appears inside the bee movie script
    and save each word with the amount of times it occurred in a dictionary
    Don't differentiate between capitalized and non-capitalized letters
    :return: A dictionary containing all words and the amount of times they occur
    """
    pass

def largestCalories():
    """
    Inside the Calories.txt, multiple 'boxes' of calories are listed, each box
    being seperated by an empty line. In the Calories_small.txt you have an easier list to test with
    In the example, the first box would contain 1000, 2000 and 3000 calories, the second box
    contains only 4000 calories. In this example the largest box would be box 4 with
    a sum of 24000 calories. Find the largest box.
    :return: The amount of calories in the largest box
    """
    pass


if __name__ == "__main__":
    countWordOccurences()