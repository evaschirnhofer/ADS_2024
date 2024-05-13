# import and install pandas library: https://pandas.pydata.org/
import pandas as pd

# import and install numpy library: https://numpy.org/
import numpy as np


"""
Read data from csv with pandas
Create a DataFrame
"""
data = pd.read_csv("employees2.csv")

df = pd.DataFrame(data)

print(df)


"""
Checking for missing values using isnull() and notnull()
"""

# dictionary of lists with dummy data - np.nan is to simulate non existing values
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
print(df.isnull())

"""
Using isNull to only show the rows having Gender = NULL.
"""
# making data frame from csv file
data = pd.read_csv("employees2.csv")

# creating bool series True for NaN values
bool_series = pd.isnull(data["Gender"])

# filtering data
# displaying data only with Gender = NaN
print(data[bool_series])