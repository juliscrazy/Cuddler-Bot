#!/usr/bin/python3.7
import multiprocessing
import time

from bot import botmain
from webinterface import interfacehandler

if __name__ == "__main__":
    multiprocessing.set_start_method("fork")
    botpipe, interfacepipe = multiprocessing.Pipe()
    botprocess = multiprocessing.Process(target=botmain.run, args=(botpipe,))
    interfaceprocess = multiprocessing.Process(target=interfacehandler.run, args=(interfacepipe,))
    interfaceprocess.start()
    botprocess.start()
