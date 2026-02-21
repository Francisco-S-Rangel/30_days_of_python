# Pandas is an open source, high-performance, easy-to-use data structures aand data analysis
# tools for the Python programming language. Pandas adds data structure and tools designed to work 
# with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation.

# reshaping
# merging
# sorting
# slicing
# aggregation

# python -m pip install pandas 

# Pandas data structure is based on Series and DataFrames.

# A series is a column and a DataFrame is a multidimensional table made up of collection of series. 
# In order to create a pandas series we should use numpy to create a one dimensional arrays or a python list.

import pandas as pd
import numpy as np

numbers = [1,2,3,4,5]

series = pd.Series(numbers)
print(series)

names = ["Francisco", "Ana Julia", "James", "Laura", "Logan", "Mary", "Edward"]

names_series = pd.Series(names)
print(names_series)


dct_name = {"name": "Francisco", "surname": "Rangel", "country": "Brazil", "city": "Mogi das Cruzes"}
print(pd.Series(dct_name))

# Creating a constant pandas series

series = pd.Series(10, index = [1,2,3])
print(series)

# Creating a pandas series using linspace

series = pd.Series(np.linspace(5, 20, 10))
print(series)

#  DataFrames
# Basically a cluster of Series that will lead to an organized table of data
data = [
    ["Francisco", "Brazil", "Mogi das Cruzes"],
    ["David", "United States", "Los Angeles"],
    ["Taylor", "Canada", "Calgary"]
]

data_frame = pd.DataFrame(data, columns=["Names", "Country", "City"])
print(data_frame)

# Creating DataFrame Using Dictionary
data = { 
    "Name": ["Francisco", "Lauren", "Justin", "Donald"],
    "Country": ["Brazil", "Canada", "Australia", "United States of America"],
    "City": ["Mogi das Cruzes", "Vancouver", "Melbourne", "New York City"]
}

data_frame = pd.DataFrame(data)
print(data_frame)

# Creating DataFrames from a List of Dictionaries 
data = [
    {"Name": "Francisco", "Country": "Brazil", "City": "Mogi das Cruzes"},
    {"Name": "Mary", "Country": "France", "City": "Paris"},
    {"Name": "Alexey", "Country": "Russia", "City": "Moscow"},
    {"Name": "Alexandre", "Country": "Italy", "City": "Millan"}
]

data_frame = pd.DataFrame(data)
print(data_frame)

print("-------------------------------")

# You can also create a DataFrame using a file(most used way!)

import pandas as pd

data_frame = pd.read_csv("./files/weight-height.csv")
print(data_frame)

# Data Exploration 
# We can read only the first 5 rows using head()

print(data_frame.head())

print("-------------------------------")

# We can read only the last 5 rows using tail()
print(data_frame.tail())

# As you can see the csv file has three columns and 1000 rows - but you can see this without print the full data frame 
print(data_frame.shape)
print(data_frame.columns)

# You can take a series of data frame by picking the name of the column
heights = data_frame["Height"]
print(heights)

print("-------------------------------")

weights = data_frame["Weight"]
print(weights)

print("-------------------------------")

# The method describe() give statistical information about data (You can do it with series and data Frame)
print(heights.describe())

print("-------------------------------")

print(data_frame.describe())

print("-------------------------------")
# The method info() five information about the dataset
print(data_frame.info())

# Modifying a DataFrame

# We can create a new DataFrame. We can create a new column and add it to the DataFrame. We can remove an existing column from a DataFrame.
# We can modify an existing column in a DataFrame. We can change the data type of column values in the DataFrame.

import pandas as pd
import numpy as np 

data = [
    {"Name": "Francisco", "Country": "Brazil", "City": "Mogi das Cruzes"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}
]

data_frame = pd.DataFrame(data)
print(data_frame)

# Adding a column 

weights = [74, 78, 69]
data_frame["Weight"] = weights

print(data_frame)

heights = [179, 190, 163]
data_frame["Height"] = heights

print(data_frame)

data_frame["Height"] = data_frame["Height"] * 0.01

print(data_frame)