count = 0
while count < 5:
    print(count)
    count = count + 1

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print("Final value:", count)

count = 0
while count < 5:
    print(count)
    count = count +1
    if count == 3:
        break

count = 0
while count < 5:
    if count ==3:
        count += 1
        continue
    print(count)
    count +=1

print("-------------------------")

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

language = "Python"
for letter in language:
    print(letter)

print("-------------------------")

for i in range(len(language)):
    print(language[i])

print("--------------------------")

numbers_tpl = (0,1,2,3,4,5,6,7,8,9,10)
for number in numbers_tpl:
    print(number)

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

for key in person:
    print(key)

for key, value in person.items():
    print(key,":", value)

it_companies = {"Facebook", "Google", "Microsoft", "apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)

numbers = (0,1,2,3,4,5)
for number in numbers:
    if number == 3:
        break
    print(number)

for number in numbers:
    print(number)
    if number ==3:
        continue
    print("next number should be: ",  number + 1) if number !=5 else print("loop's end")

print("outside the loop")


print("--------------------------")
# The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, 
# ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). 
# Creating sequences using range

lst = list(range(11))
print(lst)
lst_set = set(range(1,11))
print(lst_set)

lst = list(range(0,11,2))
print(lst)

lst_set = set(range(1,11,2))
print(lst_set)

# for backward from start to end
lst = list(range(11,0,-2))
print(lst)

for number in range(11):
    print(number)

print("--------------------------")

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

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

for number in range(11, 0, -3):
    print(number)
else:
    print("the loop stops at:", number)

for number in range(6):
    pass