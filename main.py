from flask import Flask, render_template, url_for, request, jsonify, flash, redirect, session, make_response
from util import json_response
import game

app = Flask(__name__)
app.secret_key = '$2b$12$5MbzcQaISUKBu4MqGbZ25.G1pViRBZ5vwV.nTtF8LYXpMuYZ3BwUm'
current_user = []


@app.route('/')
def index():
    if "nickname" not in session:
        return redirect("/create-nickname")
    map = game.map
    symbols = game.symbols
    return render_template("game.html", map=map, symbols=symbols)


@app.route('/create-nickname', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        nickname = request.form["nickname"]
        if nickname != "" and nickname[0] != " " and nickname not in current_user:
            session["nickname"] = nickname
            current_user.append(nickname)
            return redirect("/")
        else:
            return render_template("create-nickname.html", message="Nickname is taken or invalid!")
    return render_template("create-nickname.html")


if __name__ == '__main__':
    app.run(debug=True)
