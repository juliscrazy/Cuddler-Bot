import json
import os

import discord

from bot.commands import commandhandler
from aiohttp import client_exceptions

class Cuddler(discord.Client):
    def passmesomestuff(self, bot, logger):
        self.bot = bot
        self.log = logger

    async def on_ready(self):
        global CommandSelector
        CommandSelector = commandhandler.commandSelector()
        self.log.info('{0.user} is logged in and online.'.format(self.bot))

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!'):
            command = message.content.split()[0][1:]
            await getattr(CommandSelector, command)(message)

    async def on_member_join(self, member):
        # Welcome message
        await member.guild.system_channel.send('{0.mention} felt cute.'.format(member))
        self.log.info('{0.mention} joined the server.'.format(member))

    def startbot(self):
        self.log.info('Starting bot')

        with open("auth.json") as auth:
            try:
                self.bot.run(json.load(auth)['TOKEN'])
            except client_exceptions.ClientConnectorError:
                log.error("No connection to discordapp.com available.")