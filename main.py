#!/usr/bin/python3.7
import json
from bot import bothandler
from webinterface.interfacehandler import FlaskService

from flask import Flask 

from threading import Thread
import discord
import asyncio
import logging

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    log = logging.getLogger('cuddler-logger')
    allowedloggers = ['cuddler-logger']
    for loggers in logging.Logger.manager.loggerDict:
        if loggers not in allowedloggers:
            logging.getLogger(loggers).disabled = True
        else:
            pass

    bot = bothandler.Cuddler()
    service = FlaskService(bot, log)

    flask_thread = Thread(target=service.run)
    flask_thread.start()
    log.info('Started flask thread')
    
    bot.bindbot(bot)
    bot.bindlog(log)

    bot.startbot()