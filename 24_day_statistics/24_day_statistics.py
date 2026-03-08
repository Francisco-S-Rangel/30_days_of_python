# Python for Statistical Analysis

# Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation and presentation of data. 
# Statistics is a branch of Mathematics that is recommended to be a prerequisite for data science and machine learning. 

# Data

# What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. 
# It can be any character, including text and numbers, pictures, sound, or video. 

# Statistics Module

# The Python statistics module provides functions for calculating mathematical statistics of numerical data.
# It is aimed at the level of graphing and scientific calculators.

# NumPy

# NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.

import numpy

print("Numpy version:", numpy.__version__)

# checking the available methods
# print(dir(numpy))

python_list = [1,2,3,4,5]

print(type(python_list))
numpy_array_from_list = numpy.array(python_list)
print(type(numpy_array_from_list))

print(python_list)
print(numpy_array_from_list)

numpy_array_from_list_two = numpy.array(python_list, dtype=float)
print(numpy_array_from_list_two)

numpy_boolean_array = numpy.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_boolean_array)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)

numpy_two_dimensional_list = numpy.array(two_dimensional_list)

print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print("one dimensional array: ", np_to_list)
print("two dimensional array: ", numpy_two_dimensional_list.tolist())

python_tuple = (1,2,3,4,5)
print(type(python_tuple))
print("pyhton tuple: ", python_tuple)

numpy_array_from_tuple = numpy.array(python_tuple)
print(type(numpy_array_from_tuple))
print("numpy array from tuple: ", numpy_array_from_tuple)

# Shape of numpy array

# The shape method provide the shape of the array as a tuple. The first is the row and the second is the column.
# If the array is just one dimensional it returs the size of the array.

numbers = numpy.array([1,2,3,4,5])
print(numbers)
print("Shape of numbers: ", numbers.shape)
numpy_two_dimensional_list = numpy.array([[0,1,2],[3,4,5],[6,7,8]])
print(numpy_two_dimensional_list)
print("Shape of numpy_two_dimensional_list: ", numpy_two_dimensional_list.shape)
# three_by_four_array = numpy.array([
#     [0,1,2],
#     [3,4,5,6],
#     [7,8,9,10,11]
#     ])
# print(three_by_four_array)
# print("Shape of three_by_four_array: ", three_by_four_array.shape) - Error cause it is not a regular array, the arrays have different sizes

three_by_four_array = numpy.array([
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]) # Regular array so it works

print(three_by_four_array)
print("Shape of three_by_four_array: ", three_by_four_array.shape)

# Data  Type of numpy array 

# Type of data types: str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = numpy.array(int_lists)
float_array = numpy.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

numpy_array_from_list = numpy.array([1, 2, 3, 4, 5])
two_dimensional_list = numpy.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

# Mathematical Operation using numpy

# NumPy array is not like exactly like python list. 
# To do mathematical operation in Python list we have to loop through the items but numpy can allow to do any mathematical operation without looping. 

# Addition
numpy_array_from_list = numpy.array([1,2,3,4,5])
print("original array: ", numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print("Plus ten: ", ten_plus_original)

# Subtraction 
numpy_array_from_list = numpy.array([1,2,3,4,5])
print("original array: ", numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print("Minus ten: ", ten_minus_original)

# Multiplication
numpy_array_from_list = numpy.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print("times ten: ", ten_times_original)

# Division
numpy_array_from_list = numpy.array([1, 2, 3, 4, 5])
print("original array: ", numpy_array_from_list)
ten_div_original = numpy_array_from_list / 10
print("ten division: ", ten_div_original)

import  numpy as np

# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

# Checking data types

numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# Converting types

numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
np.array([-3, -2, 0, 1,2,3], dtype='bool')

numbers = np.array([1,2,3,4,5]).astype("str")

print(numbers)

# Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(type(two_dimension_array))
print(two_dimension_array)
print("Shape: ", two_dimension_array.shape)
print("Size: ", two_dimension_array.size)
print("Data type: ", two_dimension_array.dtype)

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

# Slicing Numpy array

two_dimension_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_dimension_array)
print("------")
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
print("------")
three_rows_and_two_columns = two_dimension_array[0:3,0:2]
print(three_rows_and_two_columns)
print("------")
two_rows_and_three_columns = two_dimension_array[0:2,0:3]
print(two_rows_and_three_columns)
print("------")

# Generating Random Numbers 
random_float = np.random.random()
print(random_float)

random_floats = np.random.random(5)
print(random_floats)

random_int = np.random.randint(0, 11)
print(random_int)

random_int = np.random.randint(2, 10, size = 4)
print(random_int)

random_int = np.random.randint(2, 10, size=(3,3))
print(random_int)

list_arange = range(0, 11, 2)

for value in list_arange:
    print(value)

list_arange = np.arange(0, 11, 2)
print(list_arange)

# You can use Python for many other things. There are many modules for performing statistics in Python. 
# This file is just an introduction to numpy and statistics, but there are many other things that will not be covered in depth for now. 