from flask import Flask, render_template, url_for, request, jsonify, flash, redirect, session, make_response
from util import json_response
import game
import persistance as ps
import os

app = Flask(__name__)
app.secret_key = '$2b$12$5MbzcQaISUKBu4MqGbZ25.G1pViRBZ5vwV.nTtF8LYXpMuYZ3BwUm'
rooms_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'rooms.csv')
users_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'users.csv')
map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'map.csv')
characters_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'characters.csv')

@app.route('/')
def index():
    if "nickname" not in session:
        return redirect("/create-nickname")
    return render_template("game.html", user_id=session['user_id'])


@app.route('/create-nickname', methods=["GET", "POST"])
def create_user():
    current_user = ps.get_users(users_path)
    if request.method == "POST":
        nickname = request.form["nickname"]
        if nickname != "" and nickname[0] != " " and nickname not in current_user:
            session["nickname"] = nickname
            current_user.append(nickname)
            ps.export_users(users_path, current_user)
            return redirect("/list-rooms")
        else:
            return render_template("create-nickname.html", message="Nickname is taken or invalid!")
    return render_template("create-nickname.html")


@app.route("/create-room", methods=["GET", "POST"])
def create_room():
    rooms = ps.get_rooms(rooms_path)
    if "nickname" not in session:
        return redirect("/create-nickname")
    if "room_id" in session:
        remove_player_from_room(session["nickname"], session["room_id"])
    if request.method == "POST":
        data = request.form
        password = data["password"]
        name = data["name"]
        if name != "" and name[0] != " " and \
                password != "" and password[0] != " " and \
                check_room_name_availability(name):
            next_id = str(int(rooms[-1]["id"]) + 1)
            new_room = {'id': next_id, 'name': name, 'password': password, '1': '', '2': '', '3': '', '4': '',
                        "game_state": "lobby"}
            rooms.append(new_room)
            ps.export_rooms(rooms_path, rooms)
            return redirect(f"/room/{next_id}")
        else:
            return render_template("create-room.html", message="Invalid name or password")
    return render_template("create-room.html")


@app.route("/list-rooms")
def list_rooms():
    rooms = ps.get_rooms(rooms_path)
    if "nickname" not in session:
        return redirect("/create-nickname")
    if "room_id" in session:
        remove_player_from_room(session["nickname"], session["room_id"])
        session.pop("room_id", None)
    return render_template("list-rooms.html", rooms=rooms)


@app.route("/room/<id>", methods=["GET", "POST"])
def room(id):
    rooms = ps.get_rooms(rooms_path)
    characters_stat = ps.get_characters(characters_path)
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
                characters_stat.append(
                    game.create_character(session["nickname"], session["user_id"]))
                ps.export_rooms(rooms_path, rooms)
                ps.export_characters(characters_path, characters_stat)
                return redirect(f"/room/{id}")
        else:
            return render_template("join_room.html", room=selected_room, message="Password is incorrect")
    if "room_id" not in session or session["room_id"] != id:
        return render_template("join_room.html", room=selected_room)
    return render_template("room.html", room=selected_room)


@app.route("/logout")
def logout():
    current_user = ps.get_users(users_path)
    if session["nickname"] in current_user:
        current_user.remove(session["nickname"])
        ps.export_users(users_path, current_user)
    if "nickname" in session and "room_id" in session:
        remove_player_from_room(session["nickname"], session["room_id"])
        session.pop("nickname")
        session.pop("room_id")
    elif "nickname" in session:
        session.pop("nickname")
    return redirect("/list-rooms")


@app.route('/player-move', methods=['POST'])
@json_response
def player_move():
    characters_stat = ps.get_characters(characters_path)
    my_dict = request.json
    game.step_player(my_dict['state'], my_dict['next'], characters_stat, session["nickname"])
    ps.export_characters(characters_path, characters_stat)


@app.route('/player-place-bomb', methods=['POST'])
@json_response
def place_bomb():
    characters_stat = ps.get_characters(characters_path)
    my_dict = request.json
    game.show_bomb(my_dict['bombState'], my_dict['userId'], characters_stat, session["nickname"])


@app.route('/map')
@json_response
def map():
    return ps.get_map(map_path)


@app.route("/room/<id>/info")
@json_response
def room_info(id):
    rooms = ps.get_rooms(rooms_path)
    current_room = {}
    for room in rooms:
        if room["id"] == id:
            current_room = room
            break
    return current_room


@app.route("/room/<id>/start")
def room_start(id):
    rooms = ps.get_rooms(rooms_path)
    for room in rooms:
        if room["id"] == str(id):
            room["game_state"] = "playing"
            ps.export_rooms(rooms_path, rooms)
            game.initialize_my_map()
            return redirect(f"/")


@app.route("/reset-rooms")
def reset_rooms():
    rooms = [{'id': '1', 'name': 'test', 'password': 'test', '1': '', '2': '', '3': '', '4': '', "game_state": "lobby"},
             {'id': '2', 'name': 'test2', 'password': 'test2', '1': '', '2': '', '3': '', '4': '',
              "game_state": "lobby"}]
    ps.export_rooms(rooms_path, rooms)
    return redirect("/list-rooms")


def put_player_into_room(room, player):
    rooms = ps.get_rooms(rooms_path)
    for num in range(4):
        if room[f"{num + 1}"] == "":
            room[f"{num + 1}"] = player
            session["user_id"] = num + 1
            for selected_room in rooms:
                if selected_room["id"] == room["id"]:
                    selected_room = room
                    ps.export_rooms(rooms_path, rooms)
                    return True
    return False


def remove_player_from_room(player, room_id):
    rooms = ps.get_rooms(rooms_path)
    for selected_room in rooms:
        if selected_room["id"] == room_id:
            room = selected_room
            for num in range(4):
                if room[f"{num + 1}"] == player:
                    room[f"{num + 1}"] = ""
                    ps.export_rooms(rooms_path, rooms)
                    break


def check_room_name_availability(name):
    rooms = ps.get_rooms(rooms_path)
    for room in rooms:
        if room["name"] == name:
            return False
    return True


if __name__ == '__main__':
    app.run(debug=True)
