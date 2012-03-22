#!/usr/bin/python

import sys

for l in sys.stdin:
    c, n = l.split(":")
    n = int(n.strip())
    c = c.strip()
    if not c.startswith("KEY_"):
        continue
    c = c[4:].lower()
    if c.startswith("alt_") or c.startswith("control_") or \
            c.startswith("shift_"):
        continue
    elif c == "backspace" or c == "end" or c == "escape" or \
            c == "left" or c == "right" or c == "up" or c == "down" or \
            c == "insert":
        continue
    elif c == "backslash":
        c = '\\'
    elif c == "bracketleft":
        c = '['
    elif c == "bracketright":
        c = ']'
    elif c == "comma":
        c = ','
    elif c == "equal":
        c = '='
    elif c == "minus":
        c = '-'
    elif c == "period":
        c = '.'
    elif c == "quoteright":
        c = '\''
    elif c == "return":
        c = '\n'
    elif c == "semicolon":
        c = ';'
    elif c == "slash":
        c = '/'
    elif c == "space":
        c = ' '
    elif c == "tab":
        c = '\t'
    for i in range(int(n)):
        sys.stdout.write(c)
