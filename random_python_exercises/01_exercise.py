name = "Edward John Cleveland"
salary = 1500.00

print("Name:", name, "- Salary:", salary)
print("Name: " + name + " - Salary: " + str(salary))
print(f"Name: {name} - Salary: {salary}")

# Using masks
digit = 10
name = "John Rambo"
salary = 7500.00
status = True

print("Digit: %d"% digit)
print("Name: %s"% name)
print("Salary: %.2f"% salary)
print("Status: %r"% status)

# Using Input
# digit = int(input("Type emplyoee digit: "))
# name = input("Emplyoee name: ")
# salary = float(input("Emplyoee salary: "))

print("Digit: %d"% digit)
print("Name: %s"% name)
print("Salary: %.2f"% salary)

print("-------------------")

a = 5 
b = 15
c = 20

print("A == B AND B > C:", a == b and b > c)
print("A < B OR B > C:", a < b or b > c)
print("not A == B:", not a == b)

print("-------------------")

# age = int(input("Type your age: "))

# if age > 18:
#     print("You can drink!")
# else:
#     print("You're not allowed to drink.")


first_grade = float(input("Type first grade: "))
second_grade = float(input("Type socnd grade: "))
final_grade = (first_grade + second_grade)/2

if final_grade >= 6:
    print("Final score: %.1f - Approved"% final_grade)
else:
    print("Final score: %.1f - Failed"% final_grade)

weight = int(input("Type the weight of this man(1m80cm):"))

if weight > 100:
    print("This man is overweight.")
elif weight < 70:
    print("This man is underweight.")
else: 
    print("Normal weight.")

print("-------------")

for number in range(10):
    print(number)

print("-------------")

for value in range(5, 16):
    print(value)

print("-------------")

for value in range(10, 0, -2):
    print(value)

print("-------------")

reps = 0
while reps <= 5:
    print(reps)
    reps+=1