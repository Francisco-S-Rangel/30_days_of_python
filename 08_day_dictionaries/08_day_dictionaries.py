# Dictionary is a collection of unordered, modifiable(muable) paired (key: value) data type.

empty_dictionary = {}

example_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}

print(example_dictionary)

person = {
    "first_name": "Francisco",
    "last_name": "Rangel",
    "age": 25,
    "country": "Brazil",
    "is_married": False,
    "skills": [
        "JavaScript",
        "Angular",
        "Python",
        "C#"
    ],
    "address": {
        "street": "Street X/Y/X",
        "zipcode": "1111111111"
    }
}

print(person)
print(len(person))

print(person["first_name"])
print(person["country"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["street"])

# The best way to do it

print(person.get("first_name"))
print(person.get("country"))
print(person.get("skills"))
print(person.get("city")) #The get method returns None, which is a NoneType object data type, if the key does not exist. - Better than this print(person['city']), which will give an error

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct["key5"] = "value5"

print(dct)

person = {
    "first_name": "Francisco",
    "last_name": "Rangel",
    "age": 25,
    "country": "Brazil",
    "is_married": False,
    "skills": [
        "JavaScript",
        "Angular",
        "Python",
        "C#"
    ],
    "address": {
        "street": "Street X/Y/X",
        "zipcode": "1111111111"
    }
}

person["job_title"] = "Software Enginner"
person["skills"].append("Java")
print(person)

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct["key1"] = "value-one"

print(dct)

person = {
    "first_name": "Francisco",
    "last_name": "Rangel",
    "age": 25,
    "country": "Brazil",
    "is_married": False,
    "skills": [
        "JavaScript",
        "Angular",
        "Python",
        "C#"
    ],
    "address": {
        "street": "Street X/Y/X",
        "zipcode": "1111111111"
    }
}

person["first_name"] = "Chico"
person["age"] = 26

print(person)

#We use the in operator to check if a key exist in a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print("key2" in dct)
print("key5" in dct)

#Removing Key and Value Pairs from a Dictionary

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.pop("key1")
print(dct)

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.popitem()
print(dct)

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
del dct["key2"]
print(dct)

person = {
    "first_name": "Francisco",
    "last_name": "Rangel",
    "age": 25,
    "country": "Brazil",
    "is_married": False,
    "skills": [
        "JavaScript",
        "Angular",
        "Python",
        "C#"
    ],
    "address": {
        "street": "Street X/Y/X",
        "zipcode": "1111111111"
    }
}

person.pop("first_name")
person.popitem()
del person["is_married"]

print(person)

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4" : "value4"}
print(dct.items())

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4" : "value4"}
print(dct.clear())

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4" : "value4"}
del dct
# print(dct) give an error.... cause dcitionary does not exist dince it was deleted

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4" : "value4"}
dct_copy = dct.copy()
print(dct_copy) 
# If dct_copy = dct then you're creating another reference to the same address in memory... 
# if it changes the first object changes the second because they both appoint to the same address... use the .copy() to create a new variable with the same data but different reference to the address in memory
# Shallow Copy it is the name of the process

keys = dct.keys()
print(keys)

values = dct.values()
print(values)