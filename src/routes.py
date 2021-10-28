from app import app
from constructor import Constructor
from flask import redirect, render_template, request, session, abort

class Data:
    result = None
    game = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reset", methods=["POST"])
def reset():
    Data.game = Constructor()
    Data.result = None
    return redirect("/rps")

@app.route("/rps")
def rps():
    score = Data.game.get_score()
    output = Data.result
    return render_template("rps.html", output=output, score=score)

@app.route("/rock", methods=["POST"])
def rock():
    Data.result = Data.game.play(1)
    return redirect("/rps")

@app.route("/paper", methods=["POST"])
def paper():
    Data.result = Data.game.play(2)
    return redirect("/rps")

@app.route("/scissors", methods=["POST"])
def scissors():
    Data.result = Data.game.play(3)
    return redirect("/rps")
