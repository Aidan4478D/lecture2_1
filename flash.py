import datetime

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])








#@app.route("/datentime")
#def index():
#    headline = "Hello, world!"
#    now = datetime.datetime.now()
#    new_year = now.month == 1 and now.day == 1

#    names = ["Alice", "Bob", "Charli"]
#    return render_template("index.html", headline=headline, new_year=new_year, names=names)


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)


#@app.route("/<string:name>")
#def david(name):
#    name = name.capitalize()
#    return f"hello, {name}!"


@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)
