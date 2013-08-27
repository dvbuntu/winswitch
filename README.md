==========================
Positional Window Switcher
==========================

The Positional Window Switcher will allow the user to issue a keyboard shortcut to change the window focus to the nearest window in a cardinal direction (left, right, up, down, in front, behind).

It will use the X Window system libraries in C and hopefully work under openbox.

Flow
----

* Get current window position
* Fetch list of all windows and positions
** XQueryTree()
** http://cboard.cprogramming.com/linux-programming/125534-accessing-windows-x11.html
** get a list of windows and print out their names
* Compare current position to other window positions
** Generally want nearest window to right that I'm not covering, i.e. smallest positive distance between edges (his left vs my right)
* Decide which window to switch to
* switch (using XSetInputFocus?)

Challenges
----------

PWS will have to run in the background, yet it will have to intercept keyboard commands.  I can get around this by having it be a command line argument and have an openbox shortcut.  So the command line must contain the info necessary as far as what direction to switch.  I don't think openbox will change the focus just for a keyboard shortcut.

This will make debugging a little easier since I'll be constantly switching the window nearest right of wherever I'm coding.

Todo
----

* Get a skeleton X11 C program compiling
** get one running
* Change focus from a fixed window to another
* Get a list of windows and their positions using X11
* Other Flow tasks

Info
----

wmctrl
    This is a command line tool for switching windows, it can also give list
    information.  I suspect that I can hack together a script that will first
    print out a listing of windows, parse the positional information, comput
    e the switch, then call wmctrl again to actually switch focus.
    So what I wanted to do is basically already doable with wmctrl.  Damn