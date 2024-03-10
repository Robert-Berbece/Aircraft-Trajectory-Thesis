from flask import Flask, send_from_directory, session, send_file
from flask import render_template, request
import json
import time
import os
import flask

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_track") #?A=Los Angeles&B=Paris&weather_score=0.2
def get_track():
    A = request.args.get('A')
    B = request.args.get('B')
    weather_score = request.args.get('weather_score')

    print(A, B, weather_score)

    arr = []
    if A == B:
        response = flask.jsonify({'data': arr})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


    with open('data.json') as file:
        data = json.load(file)

    print(data)
    # arr = data[A][B][str(weather_score)]

    try:
        arr = data[A][B][str(weather_score)]
        print("data is ", arr)
    except :
        arr = []

    response = flask.jsonify({'data': arr})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')