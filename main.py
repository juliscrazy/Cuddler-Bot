#!/usr/bin/python3.7
import json
from bot import bothandler
from webinterface.interfacehandler import *
from aiohttp import client_exceptions

from flask import Flask 

from threading import Thread
import discord
import asyncio
import logging

bot = bothandler.Cuddler()

def startFlask():
    log.info('Starting flask')
    with open("ip.json") as ip:
        app.run(host=json.load(ip)['hostip'])

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    log = logging.getLogger('cuddler-logger')
    allowedloggers = ['cuddler-logger']
    for loggers in logging.Logger.manager.loggerDict:
        if loggers not in allowedloggers:
            logging.getLogger(loggers).disabled = True
        else:
            pass

    flask_thread = Thread(target=startFlask)
    flask_thread.start()
    log.info('Started flask thread')
    
    bot.passmesomestuff(bot, log)

    # discord_thread = Thread(target=startDiscord)
    # discord_thread.start()
    # log.info('Started discord thread')

bot.run()

    