import os
import json
import logging

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    await member.guild.system_channel.send('{0.mention} felt cute.'.format(member))
    log.info('{0.mention} felt cute.'.format(member))
if __name__ == "__main__":
    log.info('Running bot')
    with open('auth.json') as auth:
        client.run(json.load(auth)['TOKEN'])