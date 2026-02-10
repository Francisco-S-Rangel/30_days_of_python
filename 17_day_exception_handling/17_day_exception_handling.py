try:
    print(10 + "5")
except:
    print("Something went wrong") 

from datetime import date

current_year = date.today().year

# try:
#     name = input("Enter your name:")
#     year_born = input("Year you were born:")
#     age = current_year - year_born
#     print(f"You are {name}. And your age is {age}.")
# except:
#     print("Something went wrong")

# try:
#     name = input("Enter your name:")
#     year_born = input("Year you were born:")
#     age = current_year - year_born
#     print(f"You are {name}. And your age is {age}.")
# except TypeError:
#     print("Type error occored")
# except ValueError:
#     print("Value error occored")
# except ZeroDivisionError:
#     print("Zero division error occored")

# try:
#     name = input("Enter your name:")
#     year_born = input("Year you born:")
#     age = current_year - int(year_born)
#     print(f"You are {name}. And your age is {age}.")
# except TypeError:
#     print("Type error occorred")
# except ValueError:
#     print("Value error occorred")
# except ZeroDivisionError:
#     print("Zero division error occorred")
# else:
#     print("I usually run with this try block")
# finally:
#     print("I always run")

# try:
#     name = input("Enter your name:")
#     year_born = input("Year you born:")
#     age = current_year - year_born
#     print(f"You are {name}. And your age is {age}.")
# except Exception as e:
#     print(e)

def sum_of_five_numbers(a, b, c, d, e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
# print(sum_of_five_numbers(lst))
print(sum_of_five_numbers(*lst))

numbers = range(2,7)
print(list(numbers))

args = [2, 7]
numbers = range(*args)
print(numbers)

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]

fin, swe, nor, *rest = countries
print(fin, swe, nor, rest)
numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(one, middle, last)

def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old."

dct = {"name": "Francisco", "country": "Brazil", "city": "Mogi das Cruzes", "age": 25}
print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6,7))

def packing_person_info(**args):
    for key in args:
        print(f"{key} = {args[key]}")
    return args

print(packing_person_info(name="Francisco",country="Brazil",city="Mogi das Cruzes", age=25))

lst_one = [1,2,3]
lst_two = [4,5,6]
lst_three = [0, *lst_one, *lst_two]

print(lst_three)

country_lst_one = ["Finland", "Sweeden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

for index, item in enumerate([20,30,40]):
    print(index, item)

contries = ["Finland", "sweeden", "Norway", "Denmark", "Iceland"]

for index, i in enumerate(countries):
    if i == "Denmark":
        print(f"The counntry {i} has been found at index {index}")
    
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["tomato", "potato", "cabbage", "onion", "carrot"]

fruits_and_vegetables = []

for fruit, vegetable in zip(fruits, vegetables):
    fruits_and_vegetables.append({"fruit": fruit, "vegetable": vegetable})

print(fruits_and_vegetables)