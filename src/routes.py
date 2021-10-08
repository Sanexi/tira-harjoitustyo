from app import app
from constructor import Constructor
from flask import redirect, render_template, request, session, abort

class Data():
    constructor = Constructor()
    output = None
    score = [0, 0, 0]
def add_score():
    result = data.output[0]
    data.score[result] += 1

data = Data()

@app.route("/")
def index():
    output = data.output
    score = data.score
    return render_template("index.html", output=output, score=score)

@app.route("/rock", methods=["POST"])
def rock():
    data.output = data.constructor.play(1)
    add_score()
    return redirect("/")

@app.route("/paper", methods=["POST"])
def paper():
    data.output = data.constructor.play(2)
    add_score()
    return redirect("/")

@app.route("/scissors", methods=["POST"])
def scissors():
    data.output = data.constructor.play(3)
    add_score()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    data.constructor = Constructor()
    data.output = None
    data.score = [0, 0, 0]
    return redirect("/")
