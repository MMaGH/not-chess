from flask import Flask, render_template, url_for, request, jsonify, flash, redirect, session, make_response
from util import json_response
import game

app = Flask(__name__)
app.secret_key = '$2b$12$5MbzcQaISUKBu4MqGbZ25.G1pViRBZ5vwV.nTtF8LYXpMuYZ3BwUm'
current_user = []
rooms = [{'id': '1', 'name': 'test', 'password': 'test', '1': '', '2': '', '3': '', '4': ''},
         {'id': '2', 'name': 'test2', 'password': 'test2', '1': '', '2': '', '3': '', '4': ''}]


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


@app.route("/create-room")
def create_room():
    return render_template("create-room.html")


@app.route("/list-rooms")
def list_rooms():
    return render_template("list-rooms.html", rooms=rooms)


@app.route("/room/<id>", methods=["GET", "POST"])
def room(id):
    selected_room = {}
    for room in rooms:
        if room["id"] == id:
            selected_room = room
            break
    if request.method == "POST":
        password = request.form["password"]
        if password == selected_room["password"]:
            if "room_id" in session:
                session.pop("room_id", None)
            session["room_id"] = id
            if put_player_into_room(selected_room, session["nickname"]):
                return redirect("")
            else:
                session.pop("room_id", None)
    if "room_id" not in session or session["room_id"] != id:
        return render_template("join_room.html", room=selected_room)
    print(selected_room)
    return render_template("room.html", room=selected_room)


def put_player_into_room(room, player):
    for num in range(4):
        if room[f"{num + 1}"] == "":
            room[f"{num + 1}"] = player
            for selected_room in rooms:
                if selected_room["id"] == room["id"]:
                    selected_room = room
                    return True
    return False


def remove_player_from_room(room, player):
    for num in range(4):
        if room[f"{num + 1}"] == player:
            room[f"{num + 1}"] = ""

if __name__ == '__main__':
    app.run(debug=True)
