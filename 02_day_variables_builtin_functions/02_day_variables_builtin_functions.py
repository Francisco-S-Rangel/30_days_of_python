first_name = 'Francisco'
last_name = 'Rangel'
country = 'Brazil'
city = 'Mogi das Cruzes'
age = 25
is_married = False
skills = ['HTML','CSS','JS','Angular','Python']
person_info = {
    'firstname': 'Francisco',
    'lastname': 'Rangel',
    'country': 'Brazil',
    'city': 'Mogi das Cruzes',
}


print('First Name:', first_name)
print('First Name length:', len(first_name))
print('Last Name:', last_name)
print('Last Name length:', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person Information:', person_info)

first_name, last_name, country, city, age, is_married = 'Chico', 'Rangel', 'Brazil', 'Mogi das Cruzes', 25, False

print('First Name:', first_name)
print('First Name length:', len(first_name))
print('Last Name:', last_name)
print('Last Name length:', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)

# first_name = input('What is your name: ')
# age = input('How old are you?')

# print(first_name)
# print(age)

num_int = 10
print('num_int:', num_int)
num_float = float(num_int)
print('num_float:', num_float)

gravity = 9.82
print(gravity)
print(int(gravity))


num_int = 10
print(num_int)
print(str(num_int))

num_str =  '10.9'
num_float = float(num_str)
print('num_float:', num_str, num_float)
num_int = int(num_float)
print('num_int', int(num_int))

first_name = 'Francisco'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
