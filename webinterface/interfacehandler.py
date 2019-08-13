import json
import os

import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    print(os.getcwd())
    return flask.render_template("index.html")

def run():
    with open("ip.json") as ip:
        app.run(host=json.load(ip)['hostip'])
