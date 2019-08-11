import json
import logging
import os
from bot.commands.commandhandler import CommandSelector

from aiohttp import client_exceptions
import discord

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('cuddler-logger')
allowedloggers = ['cuddler-logger']
for loggers in logging.Logger.manager.loggerDict:
    if loggers not in allowedloggers:
        logging.getLogger(loggers).disabled = True
    else:
        pass

client = discord.Client()

@client.event
async def on_ready():
    log.info('{0.user} is logged in and online.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        try:
            getattr(CommandSelector, message.content.split()[0][1:])(message)
        except AttributeError:
            CommandSelector.help(message)

@client.event
async def on_member_join(member):
    # Welcome message
    await member.guild.system_channel.send('{0.mention} felt cute.'.format(member))
    log.info('{0.mention} joined the server.'.format(member))

def run()
    log.info('Starting up bot')
    with open('auth.json') as auth:
        try:
            client.run(json.load(auth)['TOKEN'])
        except client_exceptions.ClientConnectorError:
            log.error("No connection to discordapp.com available.")
