# Tuples 

# A Tuple is a collection of different data types which is ordered and unchangeable(immutable). Tuples are written with round brackets, ().
# Once tuple is created, we cannot  change its values.

empty_tuple = ()
empty_tuple = tuple()

tuple_example = ("item1", "item2", "item3")
print(tuple_example)

fruits = ("banana", "orange", "mango", "lemon")
print(fruits)
print(len(fruits))
first_item, second_item, last_item = fruits[0], fruits[1], fruits[len(fruits) - 1]
print(first_item, second_item, last_item)

last_fruits, second_last_fruit = fruits[-1], fruits[-2]
print(last_fruits, second_last_fruit)

all_items = fruits[0:4]
all_items_2 = fruits[0:]
print(all_items, all_items_2)

all_fruits = fruits[-4:]
print(all_fruits)
orange_mango = fruits[-3:-1]
print(orange_mango)

# We can change tuples to lists and lists to tuples.

tpl = ("item1", "item2", "item3", "item4", "item5")
lst = list(tpl)
print(lst)

fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)

fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)
print("aaple" in fruits)

tpl1 = ("item1", "item2", "item3")
tpl2 = ("item4", "item5", "item6")
tpl3 = tpl1 + tpl2
print(tpl3)

fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.

tpl1 = ("item1", "item2", "item3")
# Works because it exists 
print(tpl1) 
del tpl1
# Does not work cause it does not exist
print(tpl1)

fruits("banana", "orange", "mango", "lemon")
# Works because it exists 
print(fruits)
del(fruits)
# Does not work cause it does not exist
print(fruits)
