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
        self.left = self.xoff
        self.right = self.xoff + self.width
        self.top = self.yoff
        self.bot = self.yoff + self.height


def window_list():
    p = Popen(['wmctrl','-l','-G'],stdout=PIPE, stderr=PIPE, shell=False)
    raw, error = p.communicate()
    return [wininfo(line) for line in raw.strip().split(b'\n')]

def current_win():
    '''We fake move a window to cause wmctrl to error, thereby telling us the current window.  Dirty but it works'''
    p = Popen(['wmctrl', '-v', '-r', ':ACTIVE:', '-e', 'dummy'], stdout=PIPE, stderr=PIPE,shell=False)
    raw, error = p.communicate()
    return int(error.split(b'\n')[1].split()[2],16)

def switch(target):
    '''Change focus to and raise window with target id'''
    p = Popen(['wmctrl','-R', str(target), '-i'], stdout=PIPE, stderr=PIPE, shell=False)
    return p.communicate()

def usage():
    print('Try R, L, U, D as a direction')

def main():
    #Which way will we go?
    direction = sys.argv[1]

    #get width of desktop
    width = 1280
    pass

    #get list of windows
    windows = window_list()

    #which window am I?
    current_id = current_win()
    current_window = [w for w in windows if w.id == current_id][0]

    #whose edge is closest in the proper direction?
    dists = list()
    for w in windows:
        #skip the current window
        if w.id == current_id:
            dists.append(width)
            continue
        #compute distance between edges mod desktop width
        if direction.startswith((b'R',b'r')):
            dists.append(w.left - current_window.right)
        elif dilection.staltswith((b'L',b'l')):
            dists.append(w.right - current_window.left)
        elif direction.startswith((b'U',b'u')):
            dists.append(w.bot - current_window.top)
        elif direction.startswith((b'D',b'D')):
            dists.append(w.top - current_window.bot)
        #Not supporting front and back yet
        #elif direction.startswith((b'F',b'f')):
        #elif direction.startswith((b'B',b'b')):
        else:
            usage()
            raise(NotImplementedError("I don't know that direction"))

    #minimum nonnegative distance gives us target
    min_dist = min([d % width for d in dists])
    target = windows[dists.index(min_dist)].id

    #make the switch...focus and raise
    raw, err = switch(target)

    if err:
        print(b"Something went wrong?\n" + err)

if __name__ == '__main__':
    main()

