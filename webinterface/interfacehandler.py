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

    async def index(self):
        await self.bot.get_channel(607236109621002252).send("test")
        return flask.render_template("dashboard.html")

    async def servers(self):
        return flask.render_template("servers.html")

    async def stats(self):
        return flask.render_template("stats.html")

    async def integrations(self):
        return flask.render_template("integrations.html")

    async def logs(self):
        return flask.render_template("logs.html")

    def run(self):
        self.log.info('Starting flask')
        with open("ip.json") as ip:
            self.app.run(host=json.load(ip)['hostip'])

    async def test(self):
        await self.bot.get_channel(607236109621002252).send("test")