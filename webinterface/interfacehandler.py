import json
import os

import flask

app = flask.Flask(__name__)
app.debug = False

@app.route("/")
def index():
    return flask.render_template("dashboard.html")

@app.route("/servers/")
def Servers():
    return flask.render_template("servers.html")

@app.route("/stats/")
def stats():
    return flask.render_template("stats.html")

@app.route("/integrations/")
def integrations():
    return flask.render_template("integrations.html")

@app.route("/logs/")
def logs():
    return flask.render_template("logs.html")