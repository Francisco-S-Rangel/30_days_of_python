letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

multiline_string = """I am a programmer and eternal learner.
I am always learning something new, and this time it's Python."""

print(multiline_string)

first_name = "Francisco"
last_name = "Rangel"
space = " "
full_name = first_name + space + last_name

print(full_name)

print(len(first_name))
print(len(last_name))
print((len(first_name)) > len(last_name))
print(len(full_name))

language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

language = "Python"
last_letter = language[-1]
print(last_letter)
second_last_letter = language[-2]
print(second_last_letter)

language = "Python"
first_three_letter = language[0:3]
print(first_three_letter)
second_three_letter = language[3:6]
print(second_three_letter)

last_three_letter = language[-3:]
print(last_three_letter)
last_three_letter = language[3:]
print(last_three_letter)

language = "Python"
pto = language[0:6]
print(pto)
pto = language[0:6:2]
print(pto)

print("I hope every one enjoying the python challenge.\nDo you?")
print("Days\tTopics\tExercises")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")
print("Day 4\t3\t5")
print("This is a back slash symbol (\\)")
print("In every programming language it starts with \"Hello, World!\"")

challenge = "thirty days of python"
print(challenge.capitalize())

print(challenge.count("y"))
print(challenge.count("y", 7, 14))
print(challenge.count("y", 7, 21))
print(challenge.count("th"))

print(challenge.endswith("on"))
print(challenge.endswith("tion"))

challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))

print(challenge.find("y"))
print(challenge.find("th"))

first_name = "Francisco"
last_name = "Rangel"
job = "Software Engineer"
country = "Brazil"
sentence = "I am {} {}. I am a {}. I live in {}.".format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * (radius ** 2)
result = "The area of circle with {} radius is {}".format(str(radius), str(area))
print(result)

challenge = "Thirty days of python"
print(challenge.index("y"))
print(challenge.index("th"))

challenge = "ThirtyDaysPython"
print(challenge.isalnum())

challenge = "30DaysPyhton"
print(challenge.isalnum())

challenge = "Thirty days of python"
print(challenge.isalnum())

challenge = "Thirty days of python 2026"
print(challenge.isalnum())

challenge = "Thirty days of python"
print(challenge.isalpha())
num = "123"
print(num.isalpha())


print(challenge.isdecimal())
print(num.isdecimal())

challenge = "Thirty"
print(challenge.isdigit())
num = "30"
print(num.isdigit())

num = "10"
print(num.isdecimal())
num = "20.5"
print(num.isdecimal())

challenge = "30DaysOfPython"
print(challenge.isidentifier())
challenge = "Thirty Days Of Python"
print(challenge.isidentifier())
challenge = "ThirtyDaysOfPython"
print(challenge.isidentifier())
challenge = "thirty_days_of_python"
print(challenge.isidentifier())

challenge = "thirty days of python"
print(challenge.islower())
challenge = "Thirty days of python"
print(challenge.islower())

challenge = "thirty days of python"
print(challenge.isupper())
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())

num = "10"
print(num.isnumeric())
print("ten".isnumeric())

web_tech = ["HTML", "CSS", "javaScript", "Angular"]
result = "#, ".join(web_tech)
print(result)
result = " - ".join(web_tech)
print(result)

challenge = " thirty days of python "
print(challenge.strip("y"))
challenge = "ythirty days of pythony"
print(challenge.strip("y"))

challenge = "thirty days of python"
print(challenge.replace("python","coding"))
print(challenge.split())
print(challenge.title())

print(challenge.swapcase())
challenge = "Thirty Days Of Python"
print(challenge.swapcase())

challenge = "thirty days of python"
print(challenge.startswith("thirty"))
challenge = "30 days of python"
print(challenge.startswith("thirty"))