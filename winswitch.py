#!/usr/bin/python
from subprocess import Popen, PIPE

class wininfo:
    def __init__(self, line):
        pieces = line.strip().split()
        self.id = int(pieces[0])
        self.desktop = int(pieces[1])
        self.xoff = int(pieces[2])
        self.yoff = int(pieces[3])
        self.width = int(pieces[4])
        self.height = int(pieces[5])
        self.host = pieces[6]
        self.name = pieces[7]


def window_list():
    p = Popen(['wmctrl','-l','-G'],stdout=PIPE, stderr=PIPE, shell=False)
    raw, error = p.communicate()
    return [wininfo(line) for line in raw.strip().split('\n')]



