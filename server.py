from os import name
from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
  return render_template("index.htm", name=username, post_id=post_id)

@app.route("/about.htm")
def about():
  return render_template("about.htm")

@app.route("/blog")
def blog():
  return "This is a nice blog!"