# SyntaxError 

# print "Hello World!"
print("Hello World!")

# NameError

# print(age)
age = 26
print(age)

# IndexError

numbers = [1,2,3,4,5]

# print(numbers[5])
print(numbers[4])

# ModuleNotFoundError

# import maths
import math

# AttributeError

import math

# math.PI
math.pi

# KeyError 

users = {
    "name": "Francisco",
    "country": "Brazil"
}

# users["county"]
print(users["country"])

# TypeError

# 4 + "3"
print(4 + 3)

# ImportError

# from math import power
from math import pow
pow(2,3)

# ValueError

# int("12a")
# In this case we cannot change the given string to a number, because of the "a" letter in it

# ZeroDivisionError 

# 1/0
# We cannot divide a number by zero 