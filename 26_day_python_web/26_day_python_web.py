# Python for Web

# Python is a general purpose programming language and it can be used for many places. In this section, we will see how we use Python for the web. 
# There are many Python web frame works. Django and Flask are the most popular ones. Today, we will see how to use Flask for web development.

#  Flask

# Flask is a lightweight, open-source Python web framework classified as a "microframework" because it requires no specific tools or libraries to operate,
# focusing on simplicity and flexibility.
# It is designed for quickly building web applications, REST APIs, and microservices, allowing developers to add extensions for features like databases or authentication only as needed.

# pip install flask

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
# to stop caching static file
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/") # this decorator create the base route
def home():
    # return "<h1>Welcome</h1>"
    techs = ["HTML", "CSS", "Flask", "Python"]
    name = "30 Days of Python Programming"
    return render_template("home.html", techs = techs, name = name, title="Home")

@app.route("/about")
def about():
    # return "<h1>About us</h1>"
    name = "This project was created with the goal of learning Python basics."
    return render_template("about.html", name = name, title = "About us")

@app.route("/post", methods=["GET","POST"])
def post():
    name = "Text Analyzer"
    if request.method == "GET":
        return render_template("post.html", name = name, title = name)
    if request.method == "POST":
        content = request.form["content"]
        print(content)
        return redirect(url_for("result"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host="0.0.0.0", port=port)