from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    return render_template("new.html")