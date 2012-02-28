#!/usr/bin/python
import time
import yaml
from record import XEvents
from os import path

filename = "kbdstat.yaml"

events = XEvents()
events.start()

stat = {}
if path.exists(filename):
    stat = yaml.load(file(filename, "r"))

while not events.listening():
    # Wait for init
    time.sleep(1)

def save():
    yaml.dump(stat, file(filename, "w"), default_flow_style=False)

try:
    i = 0
    while events.listening():
        evt = events.next_event()
        if not evt:
            time.sleep(0.5)
            continue
        if evt.type != "EV_KEY" or evt.value != 1:
            continue
        sym = str(evt.code)
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
