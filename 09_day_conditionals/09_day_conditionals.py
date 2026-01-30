a = 3
if a > 0:
    print("A is a positive number")

if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")

a = 0
if a > 0:
    print("A is a postive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

a = 3
print("A is positive") if a > 0 else print("A is negative")

a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even number")
    else:
        print("A is a positive and odd number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

a = 0
if a > 0 and a % 2 == 0:
    print("A is a positive and even number")
elif a > 0 and a % 2 != 0:
    print("A is a positive an odd number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

user = "software engineer"
access_level = 3
if user == "manager" or access_level > 4:
    print("Access granted!")
else:
    print*("Access denied!")