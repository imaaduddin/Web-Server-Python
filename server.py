from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
  print(url_for("static", filename="spade.ico"))
  return render_template("index.htm")

@app.route("/about.htm")
def about():
  return render_template("about.htm")

@app.route("/blog")
def blog():
  return "This is a nice blog!"