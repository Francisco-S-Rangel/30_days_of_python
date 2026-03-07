# Application Programming Interface(API)

# API stands for Application Programming Interface. The kind of API we will cover in this section is going to be Web APIs.
# Web APIs are the defined interfaces through which interactions happen between an enterprise and applications that use its assests,
# which also is a Service Level Agreement (SLA) to specify the functional provider and expose the service path or URL for its API users.

# Building API 

# Restful API is an application program interface that uses HTTP requests to GET, PUT, POST and DELETE data. In the previous sections,
# we have learned about python, flask and mongoDB. We will use the knowledge we acquired to develop a Restful API using Python flask and MongoDB database. 
# Every application which has CRUD(Create, Read, Update, Delete) operation has an API to create data, to get data, to update data or to delete data from a database.

# HTTP (Hypertext Transfer Protocol)

# HTTP ia an established communication protocol between a client and a server. A client in this case is a browser and server is the place where you access data.
# HTTP is a network protocol used to deliver resources which could be files on the World Wide Web, whether they are HTML files, image files, query results, scripts or other files types.
# A brownser is an HTTP client because it sends requests to an HTTP server (Web server), which then send responses back to the client.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
users = {}
next_id = 1

# CREATE
@app.route("/users", methods=["POST"])
def create_user():
    global next_id

    data = request.json
    user = {
        "id": next_id,
        "name": data["name"]
    }

    users[next_id] = user
    next_id += 1

    return jsonify(user), 201
# GET 
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))
# UPDATE
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404
    
    data = request.json
    users[user_id]["name"] = data["name"]

    return jsonify(users[user_id])
# DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404
    
    del users[user_id]
    return {"message": "User deleted"}

app.run(debug=True)