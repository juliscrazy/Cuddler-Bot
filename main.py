#!/usr/bin/python3.7
import threading
import time

from bot import botmain
from webinterface import interfacehandler

interfacethrd = threading.Thread(target=interfacehandler.run)
botthrd = threading.Thread(target=botmain.run)
interfacethrd.start()
botthrd.start()
