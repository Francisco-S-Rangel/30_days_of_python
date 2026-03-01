# Python with MongoDB

# Python is a backend technology and it can be connected with different data base applications. It can be connected to both SQL and noSQL databases.

# MongoDB

# MongoDB is a NoSQL database. MongoDB stores data in a JSON like document which make MongoDB very flexible and scalable.

#   SQL    - NO SQL
# Database - Database
# Tables   - Collections
# Rows     - Documents
# Columns  - Fields
# Index    - Index
# Join     - Embedding and Linking
# Group by - Aggregation
# Primary Key - _id field 

# 61yohEy6znGOtNhP
# mongodb+srv://franciscosouza20092000_db_user:61yohEy6znGOtNhP@30daysofpython.4iwlgag.mongodb.net/?appName=30DaysOfPython

# Python needs a mongoDB driver to access  mongoDB database. 
# pip install pymongo dnspython

from flask import Flask, render_template
from bson.objectid import ObjectId
import pymongo
import os
# CHANGE TO YOUR MONGODB URL THIS ONE WILL NOT WORK FOR YOU - DATABASE USER DELETED
MONGODB_URL = "mongodb+srv://franciscosouza20092000_db_user:61yohEy6znGOtNhP@30daysofpython.4iwlgag.mongodb.net/?appName=30DaysOfPython"

client = pymongo.MongoClient(MONGODB_URL)
# print(client.server_info())
# Creating a database and collection
# Let us create a database, database and collection in mongoDB will be created if it doesn't exist. 
# Let's create a data base name thirty_days_of_python and students collection

# collection  is equal table but in a NO SQL Data Base

# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document

# Insert One Student
# db.students.insert_one({"name": "Francisco", "country": "Brazil", "city": "Mogi das Cruzes", "age": 25})

# Inserting many documents to collection

# students = [
#     {'name':'David','country':'UK','city':'London','age':34},
#     {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#     {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
# ]

# for student in students:
#     db.students.insert_one(student)

# MongoDB Find
# find_one() gets the first one on the list or specified
student = db.students.find_one()
print(student)
student_two = db.students.find_one({"_id":ObjectId("69a3a57e8f1a4e5d9e3c50b0")})
print(student_two)

print("---------------")

# find(): returns all the occurrence from a collection if we don't pass a query object. The object is pymongo.cursor object.
# students = db.students.find()
# We can specify which fields to return by passing second object in the find({},{})). 0 means not include and 1 means include but we cannot mix 0 and 1
students = db.students.find({}, {"_id": 0, "name": 1, "country": 1, "age": 1})

# Find with Query
# In MongoDB find can take a query object. We can pass a query object and we can filter the documents we like to filter out
query = {
    "country": "Finland"
}

students = db.students.find(query)

for student in students:
    print(student)

print("------------")

# Limiting documents
# We can limit the number of documents we return using the limit() method.
students = db.students.find().limit(3)

for student in students:
    print(student)

print("------------")

# Find with sort
students = db.students.find().sort("age")
for student in students:
    print(student)

print("------------")

# Update with query
query = {"name": "Francisco"}
new_name = {"$set": {"name": "Franklin"}}

db.students.update_one(query, new_name)
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
# When we want to update many documents at once we use upate_many() method.
for student in db.students.find():
    print(student)

print("------------")

# Delete Document
# Document = Row in No SQL Data Base
query = {"name": "John"}
db.students.delete_one(query)
# When we want to delete many documents at once we use delete_many() method.
# If we pass an empty query object to delete_many({}) it will delete all the documents in the collection.
for student in db.students.find():
    print(student)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello MongoDB</h1>"

if __name__ == "__main__":
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
    # DROP A COLLECTION 
    # Using the drop() method we can delete a collection from a databse.
    # db.students.drop()