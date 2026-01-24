# Sets

# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
# The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. 
# In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

st = set()

st = {"item1", "item2", "item3", "item4"}
print(len(st))

fruits = {'banana', 'orange', 'mango', 'lemon', "apple", "peache"}
print(len(fruits))

st = {"item1", "item2", "item3", "item4"}
print("Does set st contain item3? ", 'item3' in st)

fruits = {"banana", "orange", "mango", "lemon"}
print("mango" in fruits)

st.add("item5")
fruits.add("lime")

print(st, fruits)

# Check that there is 2 "item9", the reason is cause Sets do not allow 2 elemnts with same value, so check the set bellow and you will se that there will be only one "item9"
item_list = ["item6", "item7", "item8", "item9", "item9", "item10"]
st.update(item_list)
print(st)

vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)
print(fruits)

st = {"item1", "item2", "item3", "item4"}
st.remove("item2")
print(st)

fruits = {"banana", "orange", "mango", "lemon"}
print(fruits.pop())

st = {"item1", "item2", "item3", "item4"}
st.clear()
print(st)

del st
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# The line bellow is commented cause it will give an error since... both st and fruits were deleted
# print(st, fruits)

# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
item_list = ["item1", "item2", "item3", "item4", "item1", "item5", "item2", "item1"]
print(item_list)

item_set = set(item_list)
print(item_set)

#We can join two sets using the union() or update() method or | symbol

#union() and | symbol created a new set
st1 = {"item1", "item2", "item3", "item4", "item5"}
st2 = {"item6", "item7", "item8", "item9", "item10"}
st3 = st1.union(st2)
st4 = st1 | st2

print(st3)
print(st4)

#when update()... you're basically updating the set already existent
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
fruits.update(vegetables)
print(fruits)

#Intersection returns a set of items which are in both the sets or using "&"" symbol. See the example

st1 = {"item1", "item2", "item3", "item4", "item5"}
st2 = {"item1", "item2", "item3"}
print(st1.intersection(st2))
print(st1 & st2)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection_numbers = whole_numbers.intersection(even_numbers)

print(intersection_numbers)

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
python_dragon_intersection = python & dragon
print(python_dragon_intersection)

#Checking Subset and Super set - A set can be a subset or super set of other sets: Subset: issubset() ; Super set: issuperset

st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item1", "item2"}
st3 = {"item6", "item7","item1", "item2", "item3", "item4"}
st4 = {"item6", "item6", "item7", "item7", "item1", "item1", "item1"}

print(st2.issubset(st1),st1.issuperset(st2))
print(st3.issubset(st1),st3.issuperset(st1))
print(st4.issubset(st3))

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
odd_numbers = {1,3,5,7,9}

print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))
print(whole_numbers.issubset(even_numbers | odd_numbers))

python = {"p","y","t","h","o","n"}
dragon = {"d","r","a","g","o","n"}
python_dragon = {"p","y","t","h","o","n","-","d","r","a","g","o","n"}

print(python.issubset(dragon))
print(python.issubset(python_dragon), python_dragon.issuperset(python))

st1 = {"item1","item2","item3","item4","item5"}
st2 = {"item2","item3"}

print(st2.difference(st1), st1.difference(st2))

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
odd_numbers = whole_numbers.difference(even_numbers)
print(odd_numbers)

python = {"p","y","t","h","o","n"}
dragon = {"d","r","a","g","o","n"}

print(python.difference(dragon))
print(dragon.difference(python))

st1 = {"item1","item2","item3","item4","item5"}
st2  = {"item2","item3"}

print(st2.symmetric_difference(st1))

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
some_numbers = {1,2,3,4,5}

print(whole_numbers.symmetric_difference(even_numbers), whole_numbers.symmetric_difference(some_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.symmetric_difference(dragon))

#If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
st1 = {"item1", "item2", "item3", "item4", "item5"}
st2 = {"item2", "item3"}

print(st1.isdisjoint(st2))

even_numbers = {0,2,4,6,8,10}
odd_numbers = {1,3,5,7,9}

print(even_numbers.isdisjoint(odd_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.isdisjoint(dragon))