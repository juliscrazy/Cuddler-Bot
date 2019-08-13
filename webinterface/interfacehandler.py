import json
import os

import flask

app = flask.Flask(__name__)
app.debug = False

@app.route("/")
def index():
    return flask.render_template("dashboard.html")

@app.route("/reports/")
def reports():
    return flask.render_template("reports.html")