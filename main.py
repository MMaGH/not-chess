from flask import Flask, render_template, url_for, request, jsonify, flash, redirect, session, make_response
from util import json_response
import game

app = Flask(__name__)
app.secret_key = '$2b$12$5MbzcQaISUKBu4MqGbZ25.G1pViRBZ5vwV.nTtF8LYXpMuYZ3BwUm'


@app.route('/')
def index():
    map = game.my_map
    symbols = game.symbols
    return render_template("game.html", map=map, symbols=symbols)


@app.route('/player-move', methods=['GET', 'POST'])
@json_response
def player_move():
    if request.method == 'POST':
        my_dict = request.json
        map = game.step_player(my_dict['state'], my_dict['next'])
        return map


if __name__ == '__main__':
    app.run(debug=True)
