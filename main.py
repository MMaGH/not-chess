from flask import Flask, render_template, url_for, request, jsonify, flash, redirect, session, make_response
from util import json_response
import game

app = Flask(__name__)
app.secret_key = '$2b$12$5MbzcQaISUKBu4MqGbZ25.G1pViRBZ5vwV.nTtF8LYXpMuYZ3BwUm'


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
