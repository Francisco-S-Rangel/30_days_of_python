# A module is a file containing a set of codes or a set of functions which can be included to an application. 
# A module could be a file containing a single variable, a function or a big code base.

import my_module

print(my_module.generate_full_name("Francisco", "Rangel"))

from my_module import generate_full_name, sum_two_numbers, gravity, person
print(generate_full_name("Francisco", "Rangel"))
print(sum_two_numbers(7,5))
weight = str(int(100 * gravity)) + " N"
print(weight)
print(person["name"])

# During importing we can rename the name of the module.

from my_module import generate_full_name as full_name, sum_two_numbers as total, person as p, gravity as g
print(full_name("Francisco", "Rangel"))
print(total(7,5))
weight = str(int(100 * g)) + " N"
print(weight)
print(person["name"])

# import os

# os.mkdir("directory_name")
# os.chdir("path")
# os.getcwd()
# os.rmdir()

# import sys 

# print("Welcome {}. Enjoy {} challenge!".format(sys.argv[1], sys.argv[2]))

from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math

print(math.pi)
print(math.sqrt(2))
print(math.pow(2, 3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log(100))

from math import pi as PI
print(PI)

import string 
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

from random import random, randint 
print(random())
print(randint(5, 20))