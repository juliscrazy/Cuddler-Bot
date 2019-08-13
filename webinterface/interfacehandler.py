import json
import os

import flask

app = flask.Flask(__name__)
pipe = None

@app.route("/")
def index():
    return flask.render_template("dashboard.html")

@app.route("/reports/")
def reports():
    return flask.render_template("reports.html")

def run(mainpipe):
    global pipe
    pipe = mainpipe
    with open("ip.json") as ip:
        app.run(host=json.load(ip)['hostip'])
