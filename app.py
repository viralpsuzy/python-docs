from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Test Azure! This is hosted web application, run using Python."
