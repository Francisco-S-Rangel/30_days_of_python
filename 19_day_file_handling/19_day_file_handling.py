# File handling is an important part of programming which allows us to create, read, update and delete files. 
# In Python to handle data we use open() built-in function

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

example = open("./files/reading_file_example.txt")
print(example)
text_example = example.read()
print(text_example)
print(type(text_example))
example.close()

example = open("./files/reading_file_example.txt")
text_example = example.read(10)
print(text_example)
print(type(text_example))
example.close()

example = open("./files/reading_file_example.txt")
read_first_line = example.readline()
print(read_first_line)
print(type(read_first_line))
example.close()

# readlines(): read all the text line by line and returns a list of lines
example = open("./files/reading_file_example.txt")
lines = example.readlines()
print(lines)
print(type(lines))
example.close()

example = open("./files/reading_file_example.txt")
lines = example.read().splitlines()
print(lines)
print(type(lines))
example.close()

# After we open a file, we should close it. There is a high tendency of forgetting to close them.
# There is a new way of opening files using with - closes the file by itself.

with open("./files/reading_file_example.txt") as example:
    lines = example.readlines()
    print(lines)
    print(type(lines))

# Opening Files for Writing and Updating

# "a" - append - will append to the end of the file, if the file does not exist it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

with open("./files/reading_file_example.txt", "a") as example:
    example.write("This text has to be appended at the end")

with open("./files/reading_file_example.txt", "w") as examble:
    examble.write("THIS TEXT WILL BE WRITTEN ABOVE THE PREVIOUS ONE.")

# Deleting Files

import os 

# if os.path.exists("./files/example_to_delete.txt"):
#     os.remove("./files/example_to_delete.txt")
# else:
#     print("No file was found with this path")

# Changing JSON to Dictionary:

person_json = '''{
    "name": "Francisco",
    "surname": "Rangel", 
    "country": "Brazil",
    "skills": [
        "JavaScript",
        "Angular",
        "Python"
    ]
}
'''

# change JSON to dictionary
import json

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)

person_dct = {
    "name": "Francisco",
    "surname": "Rangel", 
    "country": "Brazil",
    "skills": [
        "JavaScript",
        "Angular",
        "Python"
    ]   
}

# convert dictionary to json
person_json = json.dumps(person_dct, indent=4) # indent just beautifies the json in order to be in multiplelines not everything gathered in one...
print(type(person_json))
print(person_json)

# Saving as JSON File

person = {
    "name": "Francisco",
    "surname": "Rangel",
    "city": "Mogi das Cruzes",
    "skills": [
        "JavaScript",
        "Angular",
        "Java",
        "Python"
    ]
}

with open("./files/json_example.json", "w", encoding="utf-8") as example: # enconding ="utf-8" defines the format the text will be saved in bytes - utf-8 is the World standard
    json.dump(person, example, ensure_ascii=False, indent=4) #ensure_ascci=False defines to keep special caracters in the JSON - [Ç~^] this like this 

# File with csv
import csv 

with open("./files/csv_example.csv") as example:
    csv_reader = csv.reader(example, delimiter=",") # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are: {", ".join(row)}")
            line_count +=1
        else:
            print(f"\t{row[0]} {row[1]} is a software enginner. He lives in {row[2]}, {row[3]}.")
            line_count += 1
    print(f"Number of lines: {line_count}")

print("---------")

import xml.etree.ElementTree as ET

tree = ET.parse("./files/xml_example.xml")
root = tree.getroot()
print("Root tag:", root.tag)
print("Atribute:", root.attrib)
for child in root:
    print(f"field: {child.tag} = {child.text.strip()}") # .strip() will verify if there's something like "\n "(It will be invisable) in xml file
    if child.tag == "skills":
        for skill in child:
            print("skill: ", skill.text)
    
