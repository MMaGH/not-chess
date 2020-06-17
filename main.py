from flask import Flask, render_template, url_for, request, jsonify, flash, redirect, session, make_response
from util import json_response
import game

app = Flask(__name__)
app.secret_key = '$2b$12$5MbzcQaISUKBu4MqGbZ25.G1pViRBZ5vwV.nTtF8LYXpMuYZ3BwUm'
current_user = []
characters_stat = []
rooms = [{'id': '1', 'name': 'test', 'password': 'test', '1': '', '2': '', '3': '', '4': ''},
         {'id': '2', 'name': 'test2', 'password': 'test2', '1': '', '2': '', '3': '', '4': ''}]


@app.route('/')
def index():
    if "nickname" not in session:
        return redirect("/create-nickname")
    return render_template("game.html", user_id=session['user_id'])


@app.route('/create-nickname', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        nickname = request.form["nickname"]
        if nickname != "" and nickname[0] != " " and nickname not in current_user:
            session["nickname"] = nickname
            return redirect("/list-rooms")
        else:
            return render_template("create-nickname.html", message="Nickname is taken or invalid!")
    return render_template("create-nickname.html")


@app.route("/create-room")
def create_room():
    if "nickname" not in session:
        return redirect("/create-nickname")
    return render_template("create-room.html")


@app.route("/list-rooms")
def list_rooms():
    if "nickname" not in session:
        return redirect("/create-nickname")
    if "room_id" in session:
        remove_player_from_room(session["nickname"], session["room_id"])
        session.pop("room_id", None)
    return render_template("list-rooms.html", rooms=rooms)


@app.route("/room/<id>", methods=["GET", "POST"])
def room(id):
    if "nickname" not in session:
        return redirect("/create-nickname")
    selected_room = {}
    for room in rooms:
        if room["id"] == id:
            selected_room = room
            break
    else:
        return redirect("/list-rooms")
    if request.method == "POST":
        password = request.form["password"]
        if password == selected_room["password"]:
            if put_player_into_room(selected_room, session["nickname"]):
                session["room_id"] = id
                current_user.append(session["nickname"])
                characters_stat.append(
                    game.create_character(session["nickname"], session["user_id"]))
                return redirect(f"/room/{id}")
    if "room_id" not in session or session["room_id"] != id:
        return render_template("join_room.html", room=selected_room)
    return render_template("room.html", room=selected_room)


@app.route("/logout")
def logout():
    if "nickname" in session and "room_id" in session:
        remove_player_from_room(session["nickname"], session["room_id"])
        current_user.remove(session["nickname"])
        session.pop("nickname")
        session.pop("room_id")
    elif "nickname" in session:
        current_user.remove(session["nickname"])
        session.pop("nickname")
    return redirect("/list-rooms")


@app.route('/player-move', methods=['POST'])
@json_response
def player_move():
    my_dict = request.json
    game.step_player(my_dict['state'], my_dict['next'], my_dict['isBomb'], characters_stat, session["nickname"])
    return True


@app.route('/player-place-bomb', methods=['POST'])
@json_response
def place_bomb():
    my_dict = request.json
    game.show_bomb(my_dict['bombState'], my_dict['userId'])
    return True


@app.route('/map')
@json_response
def map():
    return game.my_map


def put_player_into_room(room, player):
    for num in range(4):
        if room[f"{num + 1}"] == "":
            room[f"{num + 1}"] = player
            session["user_id"] = num + 1
            for selected_room in rooms:
                if selected_room["id"] == room["id"]:
                    selected_room = room
                    return True
    return False


def remove_player_from_room(player, room_id):
    for selected_room in rooms:
        if selected_room["id"] == room_id:
            room = selected_room
            for num in range(4):
                if room[f"{num + 1}"] == player:
                    room[f"{num + 1}"] = ""
                    break


if __name__ == '__main__':
    app.run(debug=True)
