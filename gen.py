#!/usr/bin/python

import sys

for l in sys.stdin:
    c, n = l.split()
    for i in range(int(n)):
        sys.stdout.write(c.lower())
