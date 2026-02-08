# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters/ A function can be returned as a result of another function
# A function can be modified/ A function can be assigned to a variable 

def sum_numbers(numbers):
    return sum(numbers)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1,2,3,4,5])
print(result)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x > 0:
        return x
    return -x

def higher_order_function(type):
    if type == "square":
        return square
    elif type =="cube":
        return cube
    elif type =="absolute":
        return absolute
    
result = higher_order_function("square")
print(square(3))
result = higher_order_function("cube")
print(cube(3))
result = higher_order_function("absolute")
print(result(3))
result = higher_order_function("absolute")
print(result(-3))

# Python allows a nested function to access the outer scope of the enclosing function.
# In Python, closure is created by nesting a function inside another encapsulating function and then returning te inner function.

def add_ten():
    ten = 10
    def add(number):
        return number + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

# Python decorator is a design pattern that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are ussually called before the definition of a function you want to decorate.

def greeting():
    return "Welcome to Python"

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

greeting_example = uppercase_decorator(greeting)
print(greeting_example())

# this decorator function is a higher order function that takes a function as a parameter

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator 
def greeting():
    return "Welcome to Python"

print(greeting())

# You can add multiple decorators to a single function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python!"

print(greeting())

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(param, param_two, param_three):
        function(param, param_two, param_three)
        print("I live in {}".format(param_three))
    return wrapper_accepting_parameters 

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to learn.".format(first_name, last_name))

print(print_full_name("Francisco", "Rangel", "Brazil"))

numbers = [1,2,3,4,5]
def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))

numbers_str = ["1", "2", "3", "4","5"]
numbers_int = map(int, numbers_str)

print(list(numbers_int))

names = ["Francisco", "Jake", "Julia", "Ana", "Sarah", "Gabriel"]

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(number):
    if number % 2 ==0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

def is_odd(number):
    if number % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

names = ["Francisco", "Jake", "Julia", "Ana", "Sarah", "Gabriel", "Maria Eduarda"]

def names_with_more_than_seven_letters(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(names_with_more_than_seven_letters, names)
print(list(long_names))

from functools import reduce

numbers_str = ["1","2","3","4","5"]

def add_two_numbers(x, y):
    return int(x) + int(y)

total = reduce(add_two_numbers, numbers_str)
print(total)