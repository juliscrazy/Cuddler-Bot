#!/usr/bin/python3.7
from bot import botmain
from webinterface import interfacehandler
import threading
import time

interfacethrd = threading.Thread(target=interfacehandler.run)
botthrd = threading.Thread(target=botmain.run)
interfacethrd.start()
botthrd.start()