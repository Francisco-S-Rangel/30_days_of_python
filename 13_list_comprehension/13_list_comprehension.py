# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

language = "Python"
lst = list(language)
print(type(language))
print(lst)

lst = [letter for letter in language]
print(type(lst))
print(lst)

letters = []

for letter in language:
    letters.append(letter)

print(letters)

numbers = [number for number in range(11)]
print(numbers)

squares = [number * number for number in range(11)]
print(squares)

tuples_of_square = [(number, number * number) for number in range(11)]
print(tuples_of_square)

even_numbers = [number for number in range(21) if number % 2 ==0]
print(even_numbers)

odd_numbers = [number for number in range(21) if number % 2 !=0]
print(odd_numbers)

even_numbers = []

for number in range(41):
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

numbers = [-4,-3,-1,0,1,2,3,4,5,6,7,8,9,10]
positive_even_numbers = [number for number in numbers if number % 2 ==0 and number >= 0]
print(positive_even_numbers)

list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
row_of_lists = [row for row in list_of_lists]
print(row_of_lists)
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(2,3))

add_two_numbers = lambda a, b: a + b
print(add_two_numbers(2, 3))

square = lambda x : x ** 2
print(square(3))

cube = lambda x : x ** 3
print(cube(3))

multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)
print(cube)

print(power(3)(3))

two_power_of_five = power(2)(5)
print(two_power_of_five)