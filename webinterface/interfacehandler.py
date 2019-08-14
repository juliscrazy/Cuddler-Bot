import json
import os

import flask

class FlaskService():
    def __init__(self, bot, log):
        self.app = flask.Flask(__name__)
        self.app.debug = False
        self.bot = bot
        self.log = log

        self.routes = [
            dict(route="/", func=self.index, page="index"),
            dict(route="/servers/", func=self.servers, page="servers"),
            dict(route="/stats/", func=self.stats, page="stats"),
            dict(route="/integrations/", func=self.integrations, page="integrations"),
            dict(route="/logs/", func=self.logs, page="logs"),
        ]

        for route in self.routes:
            self.app.add_url_rule(route["route"], route["page"], route["func"])

    def index(self):
        return flask.render_template("dashboard.html")

    def servers(self):
        return flask.render_template("servers.html")

    def stats(self):
        return flask.render_template("stats.html")

    def integrations(self):
        return flask.render_template("integrations.html")

    def logs(self):
        return flask.render_template("logs.html")
        self.bot.logout()
        self.log.info("lul")

    def run(self):
        self.log.info('Starting flask')
        with open("ip.json") as ip:
            self.app.run(host=json.load(ip)['hostip'])