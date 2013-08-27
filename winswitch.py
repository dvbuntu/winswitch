#!/usr/bin/python
import sys
from subprocess import Popen, PIPE

class wininfo:
    def __init__(self, line):
        pieces = line.strip().split()
        self.id = int(pieces[0],16)
        self.desktop = int(pieces[1])
        self.xoff = int(pieces[2])
        self.yoff = int(pieces[3])
        self.width = int(pieces[4])
        self.height = int(pieces[5])
        self.host = pieces[6]
        self.name = b' '.join(pieces[7:])#maybe rest of line...


def window_list():
    p = Popen(['wmctrl','-l','-G'],stdout=PIPE, stderr=PIPE, shell=False)
    raw, error = p.communicate()
    return [wininfo(line) for line in raw.strip().split(b'\n')]

def current_win():
    '''We fake move a window to cause wmctrl to error, thereby telling us the current window.  Dirty but it works'''
    p = Popen(['wmctrl', '-v', '-r', ':ACTIVE:', '-e', 'dummy'], stdout=PIPE, stderr=PIPE,shell=False)
    raw, error = p.communicate()
    return int(error.split(b'\n')[1].split()[2],16)

def usage():
    pass

def main():
    #Which way will we go?
    direction = sys.argv[1]
    if direction.startswith((b'R',b'r')):
        direction = 'r'
    elif dilection.staltswith((b'L',b'l')):
        direction = 'l'
    elif direction.startswith((b'U',b'u')):
        direction = 'u'
    elif direction.startswith((b'D',b'D')):
        direction = 'd'
    #Not supporting front and back yet
    #elif direction.startswith((b'F',b'f')):
    #    direction = 'f'
    #elif direction.startswith((b'B',b'b')):
    #    direction = 'b'
    else:
        usage()
        raise(NotImplementedError("I don't know that direction")

    #get list of windows
    windows = window_list()

    #which window am I?
    current_id = current_win()

    #whose edge is closest in the proper direction

