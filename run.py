#!/usr/bin/python
import time
import yaml
from record import XEvents
from os import path

filename = "kbdstat.yaml"
diFilename = "kbddistat.yaml"

events = XEvents()
events.start()

stat = {}
diStat = {}

if path.exists(filename):
    stat = yaml.load(file(filename, "r"))
if path.exists(diFilename):
    stat = yaml.load(file(diFilename, "r"))

while not events.listening():
    # Wait for init
    time.sleep(1)

def save():
    yaml.dump(stat, file(filename, "w"), default_flow_style=False)
    yaml.dump(diStat, file(diFilename, "w"), default_flow_style=False)

try:
    i = 0
    lastSym = None
    while events.listening():
        evt = events.next_event()
        if not evt:
            time.sleep(0.5)
            continue
        if evt.type != "EV_KEY" or evt.value != 1:
            continue
        sym = str(evt.code)
        if lastSym is not None:
            diSym = lastSym + ":" + sym
            if diSym in diStat:
                diStat[diSym] += 1
            else:
                diStat[diSym] = 1
        lastSym = sym
        if sym in stat:
            stat[sym] += 1
        else:
            stat[sym] = 1
        i += 1
        if i > 100:
            save()
            i = 0
except KeyboardInterrupt:
    events.stop_listening()
    save()
