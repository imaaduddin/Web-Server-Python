from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
  return render_template("index.htm")

@app.route("/about.htm")
def about():
  return render_template("about.htm")

@app.route("/blog")
def blog():
  return "This is a nice blog!"