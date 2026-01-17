empty_list = list()
print(len(empty_list))

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = ["HTML", "CSS", "JS", "Angular", "Redux", "Node", "MongoDB"]
countries = ["Finland", "Estonia", "Denmark", "Sweeden", "Norway"]

print("Fruits:", fruits)
print("Number of fruits:", len(fruits))
print("vegetables:", vegetables)
print("Number of vegetables:", len(vegetables))
print("Animal products:", animal_products)
print("Number of anuimal products", len(animal_products))
print("Web tecnologies:", web_techs)
print("Number of web tecnologies:", len(web_techs))
print("Countries:", countries)
print("Number of countries:", len(countries))

fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
third_fruit = fruits[2]
print(third_fruit)
last_fruit = fruits[3]
print(last_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print(last_fruit)

fruits = ["banana", "orange", "mango", "lemon"]
last_fruit = fruits[-1]
second_last_fruit = fruits[-2]
print(last_fruit)
print(second_last_fruit)
all_fruits = fruits[0:4]
print(all_fruits)

all_fruits_2 = fruits[0:]
print(all_fruits_2)
orange_and_mango = fruits[1:3]
print(orange_and_mango)
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)

fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]
print(all_fruits)
orange_and_mango = fruits[-3:-1]
print(orange_and_mango)
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)

fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)

fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")
print(fruits)
fruits.insert(3, "lime")
print(fruits)

fruits.remove("banana")
fruits.remove("lemon")
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)

fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-1, -2, -3, -4, -5]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_vegetables = fruits + vegetables
print(fruits_vegetables)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print(num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print(negative_numbers)

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["tomato", "potato", "cabbage", "onion", "carrot"]
fruits.extend(vegetables)
print("Fruits and vegetaables: ", fruits)

fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))
ages = [22, 32, 25, 37, 24, 56, 33, 24, 89, 0, 24, 56, 100, 89, 57]
print(ages.count(24))

fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))
ages = [22, 32, 25, 37, 24, 56, 33, 24, 89, 0, 24, 56, 100, 89, 57]
print(ages.index(24))

fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)
ages = [22, 32, 25, 37, 24, 56, 33, 24, 89, 0, 24, 56, 100, 89, 57]
ages.reverse()
print(ages)

fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 32, 25, 37, 24, 56, 33, 24, 89, 0, 24, 56, 100, 89, 57]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)