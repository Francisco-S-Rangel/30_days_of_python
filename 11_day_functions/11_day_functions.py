def generate_full_name ():
    first_name = "Francisco"
    last_name = "Rangel"
    full_name = first_name + " " + last_name
    print(full_name)

generate_full_name()

def add_two_numbers ():
    num_one = 2
    num_two = 3
    final_number = num_one + num_two
    print(final_number)

add_two_numbers()

print("------------------")

def generate_full_name ():
    first_name = "Francisco"
    last_name = "Rangel"
    return first_name + " " + last_name

print(generate_full_name())

def add_two_numbers ():
    number_one = 2
    number_two = 3
    return number_one + number_two

print(add_two_numbers())

def greetings (name):
    return name +", Welcome to python for Everyone!"

print(greetings("Francisco"))

def person_age (age):
    return "Age: " + str(age)

print(person_age(25))

def square_number(x):
    return x * x

print(square_number(3))

def area_of_circle (x):
    PI = 3.14
    return PI * (x ** 2)

print(area_of_circle(3))

def sum_of_numbers (n):
    total = 0
    for i in range (n+1):
        total+=i
    return total

print(sum_of_numbers(3))
print(sum_of_numbers(4))
print(sum_of_numbers(5))


def generate_full_name (first_name, last_name):
    return first_name + " " + last_name

print(generate_full_name("Francisco", "Rangel"))

def sum_two_numbers (num_one, num_two):
    return num_one + num_two

print(sum_two_numbers(10,6))

def calculate_age (current_year, birth_year):
    return current_year - birth_year

print("Age: ", calculate_age(2026,2000))

def weight_of_object (mass, gravity):
    return str(mass * gravity) + " N"

print("Weight of an object in Newtons: ", weight_of_object(100, 9.81))

# If we pass the arguments with key and value, the order of the arguments does not matter.

def print_fullname(first_name, last_name):
    return first_name + " " + last_name

print(print_fullname(last_name="Rangel", first_name="Francisco"))

def add_two_numbers (num_one, num_two):
    return num_one + num_two

print(add_two_numbers(num_two=23, num_one=5))

def print_name (first_name):
    return first_name

print(print_name("Francisco"))

def is_even (number):
    if number %  2 == 0:
        return True
    return False

print(is_even(4))
print(is_even(5))

def find_even_numbers (number):
    evens = []
    for i in range(number):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(find_even_numbers(12))
print(find_even_numbers(3))

def greetings (name="Peter"):
    return name + ", welcome to Python for Everyone!"

print(greetings())
print(greetings("Francisco"))

def generate_full_name (first_name = "Francisco", last_name = "Rangel"):
    return first_name + " " + last_name

print(generate_full_name())
print(generate_full_name("Chico","The Greatest!"))

def calculate_age (birth_year, current_year = 2026):
    return current_year - birth_year

print(calculate_age(2000))
print(calculate_age(current_year = 2000, birth_year = 1970))

def weight_of_object (mass, gravity = 9.81):
    return str(mass * gravity) + " N"

print(weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print(weight_of_object(100, 1.62)) # 1.62 - average gravity of the Moon

# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

def sum_all_numbers (*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_all_numbers(4))
print(sum_all_numbers(3,6,8))
print(sum_all_numbers(4,8,10,28,12))

def generate_groups (team, *names):
    print(team)
    for name in names:
        print(name)

generate_groups("Team 1: ", "Francisco", "Jack", "Laura", "Justin", "Maria")

# [Dictionary unpacking] You can call a function which has named arguments using a dictionary with matching key names. You do so using **.

def greet(name, location):
    print("Hi there", name, "how is the weather in", location, "?")

greet("Francisco", "São Paulo - Brazil")

my_dictionarie = {"name": "Francisco", "location": "São Paulo - Brazil"}

greet(**my_dictionarie)

def square_number (number):
    return number ** number

def sum_with_five(number_x, number_five = 5):
    return number_five + number_x

print(sum_with_five(square_number(3)))