# Python PIP - Python Package Manager

# PIP stands for Preferred installer program. We use pip to install different Python packages.
# Package is a Python module that can contain one or more modules or other packages.


# NumPy 
# It is one of the most popular packages in machine learning and data science community.

# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
# a powerful N-dimensional array object
# sophisticated (broadcasting) functions
# tools for integrating C/C++ and Fortran code
# useful linear algebra, Fourier transform, and random number capabilities

import numpy
print(numpy.version.version)

# Panda

# panda is an open source, BSD-licensed library providing high-performance, 
# easy-to-use data structures and data analysis tools for the Python programming language.

import pandas  
print(pandas.__version__)

print("-------------")

# Let us import a web browser module, which can help us to open any website. 
# We do not need to install this module, it is already installed by default with Python 3. 

import webbrowser

url_list = [
    "http://www.python.org",
    "https://www.linkedin.com/in/francisco-s-rangel/",
    "https://github.com/Francisco-S-Rangel"
]

for url in url_list:
    webbrowser.open_new_tab(url)

# Uninstalling Packages
# You can remove a package using the following command.

# pip uninstall packagename

# List of Packages
# To see the installed packages on our machine. 
# pip list

# Show Package
# To show information about a package

# pip show packagename

# PIP Freeze
# Generate installed Python packages with their version and the output is suitable to use it in a requirements file.

# pip freeze

# Reading from URL
# Sometimes, we would like to read from a website using url or from an API not necessarily a local file.

import requests

url = "https://docs.python.org/3/whatsnew/3.14.html"

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)
print(response.json)

from my_package import arithmetics

print(arithmetics.add_numbers(7,5,3,1))
print(arithmetics.subtract(17, 5))
print(arithmetics.multiple(5, 3))
print(arithmetics.division(8,4))
print(arithmetics.remainder(15, 5))
print(arithmetics.power(10,3))

from my_package import greet

print(greet.greet_person("Francisco", "Rangel"))
