# import fileinput

# for line in fileinput.input():
#     pass
# import sys

# for line in sys.stdin:
#     print (line)


#_______________________________________________________________________________



# import sys,tty,termios
# class _Getch:
#     def __call__(self):
#             fd = sys.stdin.fileno()
#             old_settings = termios.tcgetattr(fd)
#             try:
#                 tty.setraw(sys.stdin.fileno())
#                 ch = sys.stdin.read(3)
#             finally:
#                 termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#             return ch

# def get():
#         inkey = _Getch()
#         while(1):
#                 k=inkey()
#                 if k!='':break
#         if k=='\x1b[A':
#                 print ("up")
#         elif k=='\x1b[B':
#                 print ("down")
#         elif k=='\x1b[C':
#                 print ("right")
#         elif k=='\x1b[D':
#                 print ("left")
#         else:
#                 print ("not an arrow key!")

# def main():
#         for i in range(0,20):
#                 get()

# if __name__=='__main__':
#         main()


#_______________________________________________________________________________

# import curses
# import os
# from os import system
# from interface_tt import Interface

# # get the curses screen window
# screen = curses.initscr()

# # turn off input echoing
# # curses.noecho()

# # respond to keys immediately (don't wait for enter)
# curses.cbreak()

# # map arrow keys to special values
# screen.keypad(True)

# try:
#     while True:
#         char = screen.getch()
#         if char == ord('q'):
#             break
#         elif char == curses.KEY_RIGHT:
#             # print doesn't work with curses, use addstr instead
#             screen.addstr(0, 0, 'right')
#         elif char == curses.KEY_LEFT:
#             screen.addstr(0, 0, 'left ')
#         elif char == curses.KEY_UP:
#             screen.addstr(0, 0, 'up   ')
#         elif char == curses.KEY_DOWN:
#             screen.addstr(0, 0, 'down ')
#         elif char == curses.KEY_SDC:
#             screen.addstr(0, 0, '\DELETE ')
#         screen.refresh()
# finally:
#     # shut down cleanly
#     curses.nocbreak(); screen.keypad(0); curses.echo()
#     curses.endwin()


#_______________________________________________________________________________



# import sys,tty,termios
# class _Getch:
#     def __call__(self):
#             fd = sys.stdin.fileno()
#             old_settings = termios.tcgetattr(fd)
#             try:
#                 tty.setraw(sys.stdin.fileno())
#                 ch = sys.stdin.read(2)
#             finally:
#                 termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#             return ch

# def get():
#         inkey = _Getch()
#         while(1):
#                 k=inkey()
#                 if k!='':break
#         if k=='\x1b[A':
#                 print ("up")
#         elif k=='\x1b[B':
#                 print ("down")
#         elif k=='\x1b[C':
#                 print ("right")
#         elif k=='\x1b[D':
#                 print ("left")
#         else:
#                 print ("not an arrow key!")

# def main():
#         for i in range(0,20):
#                 get()

# if __name__=='__main__':
#         main()







# #!/usr/bin/env python

# import curses
# import curses.textpad
# import time

# stdscr = curses.initscr()

# curses.noecho()
# #curses.echo()


# begin_x = 0
# begin_y = 0
# height = 5
# width = 40
# win = curses.newwin(height, width, begin_y, begin_x)
# tb = curses.textpad.Textbox(win)
# text = tb.edit()
# curses.addstr(4,1,text.encode('utf_8'))

# #hw = "Hello world!"
# while 1:
# 	c = stdscr.getch()
# 	if c == ord('p'):
# 		exit
# 	elif c == ord('q'):
# 		break # Exit the while()
# 	elif c == curses.KEY_HOME:
# 		x = y = 0

# curses.endwin()



import curses
import sys
import readline
from sys import stdin

sys.stdin.readline()
