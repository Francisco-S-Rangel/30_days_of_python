# Classes and Objects
# Every element in a Python program is an object of a class

number = 10
print(type(number))
string = "random string"
print(type(string))
boolean = True
print(type(boolean))
empty_list = []
print(type(empty_list))
empty_tuple = ()
print(type(empty_tuple))
empty_set = set()
print(type(empty_set))
dct = {}
print(type(dct))

class Person:
    def __init__(self, name, surname, profession, country):
        self.name = name
        self.surname = surname
        self.profession = profession
        self.country = country

    def person_info(self):
        return f"{self.name} {self.surname} is a {self.profession}. He lives in {self.country}."
    
person_one = Person("Francisco", "Rangel", "Softwaree Engineer", "Brazil")

print(person_one.name, person_one.surname, person_one.profession, person_one.country)
print(person_one.person_info())

class Person_Default:
    def __init__(self, firstname="Francisco", lastname="Rangel", profession="Software Engineer", country="Brazil"):
        self.firstname = firstname
        self.lastname = lastname 
        self.profession = profession
        self.country = country

    def person_info(self):
        return f"{self.firstname} {self.lastname} is a {self.profession}. He lives in {self.country}."
    
person_two = Person_Default()
print(person_two.person_info())
person_three = Person_Default("Peter", "Parker", "Super Hero", "USA")
print(person_three.person_info())


class Person_Modify:
    def __init__(self, firstname="Francisco", lastname="Rangel", profession="Software Engineer", country="Brazil"):
        self.firstname = firstname
        self.lastname = lastname
        self.profession = profession
        self.country = country
        self.skills = []

    def person_info(self):
        return f"{self.firstname} {self.lastname} is a {self.profession}. He lives in {self.country}"
    
    def add_skill(self, skill):
        self.skills.append(skill)

    def skills_info(self):
        return f"Skills: {self.skills}"

person_four = Person_Modify()
person_four.add_skill("HTML")
person_four.add_skill("CSS")
person_four.add_skill("JavaScript")
person_four.add_skill("Python")
print(person_four.person_info())
print(person_four.skills_info())

# Inheritance

class Employee(Person_Modify):
    pass

employee_one = Employee()
employee_two = Employee("Peter","Parker", "Photographer", "USA")

employee_one.add_skill("HTML")
employee_one.add_skill("CSS")
employee_one.add_skill("JavaScript")
employee_one.add_skill("Python")

print(employee_one.person_info())
print(employee_one.skills_info())

print("------------")

employee_two.add_skill("Super reflexes")
employee_two.add_skill("He can shoot webs")
employee_two.add_skill("Super human strength")

print(employee_two.person_info())
print(employee_two.skills_info())

print("------------------------------")

class Employee_Override(Person_Modify):
    def __init__ (self, firstname="Francisco", lastname="Rangel", profession="Software Engineer", country="Brazil", city="Mogi das Cruzes", gender="Male"):
        self.city = city
        self.gender = gender
        super().__init__(firstname, lastname, profession, country)

    def person_info(self):
        pronoun = "He" if self.gender.lower() == "male" else "She"
        return f"{self.firstname} {self.lastname} ia {self.profession}. {pronoun} lives in {self.city}, {self.country}"

employee_three = Employee_Override()
employee_four = Employee_Override("Hermione", "Granger", "English Teacher", "United Kingdom", "London", "Female")

employee_three.add_skill("HTML")
employee_three.add_skill("CSS")
employee_three.add_skill("JavaScript")
employee_three.add_skill("Python")

print(employee_three.person_info())
print(employee_three.skills_info())

employee_four.add_skill("Magical Powers")
employee_four.add_skill("Fly")
employee_four.add_skill("Read people's minds")

print(employee_four.person_info())
print(employee_four.skills_info())