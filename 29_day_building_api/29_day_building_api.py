# Building API

from flask import Flask, request
import pymongo
from bson.objectid import ObjectId 
from bson.errors import InvalidId
import os

app = Flask(__name__)

# CHANGE TO YOUR MONGODB URL THIS ONE WILL NOT WORK FOR YOU - DATABASE USER WILL BE DELETED
MONGODB_URL = "mongodb+srv://test_30_days_of_python:327473249872472387@30daysofpython.4iwlgag.mongodb.net/?appName=30DaysOfPython"
client = pymongo.MongoClient(MONGODB_URL)
db = client["thirty_days_of_python"]

@app.route("/api/students", methods = ["GET"])
def get_students():
    # students_list = [
    #     {
    #         "name": "Francisco Rangel",
    #         "country": "Brazil",
    #         "city": "São Paulo"
    #     },
    #     {
    #         "name": "Diego Garcia",
    #         "country": "Argentina",
    #         "city": "Buenos Aires"
    #     },
    #     {
    #         "name": "John Carter",
    #         "country": "United States of America",
    #         "city": "Miami"
    #     }
    # ]
    students_list = list(db.students.find({}, {"_id": 0}))
    
    return students_list, 200

@app.route("/api/students/<id>", methods=["GET"])
def get_student_by_id(id: str):
    try:
        student = db.students.find_one({"_id": ObjectId(id)}, {"_id": 0})
    except InvalidId:
        return {"error": "Invalid Id"}, 400

    if student is None:
        return {"error": "Student with this id not found"}, 404
    
    return student, 200

@app.route("/api/students", methods=["POST"])
def create_student():
    student_data = request.json

    if not student_data:
        return {"error": "Request body must be JSON"}, 400

    student = {
        "name": student_data["name"],
        "country": student_data["country"],
        "city": student_data["city"]
    }

    db.students.insert_one(student)
    return {"message": "Student created"}, 201

@app.route("/api/students/<id>", methods = ["PUT"])
def update_student_by_id(id: str):
    try:
        query = {"_id":ObjectId(id)}
    except InvalidId:
        return {"error": "Invalid student id"}, 400
    
    student_data = request.json

    if not student_data:
        return {"error": "Request body must be JSON"}, 400

    student = {
        "name": student_data["name"],
        "country": student_data["country"],
        "city": student_data["city"]
    }

    result = db.students.update_one(query, {"$set": student})

    if result.matched_count == 0:
        return {"error": "Student not found"}, 404
    
    return {"message": "Student info updated"}, 200

@app.route("/api/students/<id>", methods=["DELETE"])
def delete_student(id: str):
    try:
        student_deleted = db.students.delete_one({"_id":ObjectId(id)})
    except InvalidId:
        return {"error": "Invalid student id"}, 400
    
    if student_deleted.deleted_count == 0:
        return {"error": "Student with this id not found"}, 404
    
    return {"message": "Student deleted"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)