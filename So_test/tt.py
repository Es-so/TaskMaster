

import sys,tty,termios
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

#!/usr/bin/env python

import curses
import curses.textpad
import time

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
# 	print ("AAAAAAAAAAA")
# 	c = inkey()
# 	if c == curses.KEY_SDC:
# 		print ("UP");
# 	elif c == ord('q'):
# 		break # Exit the while()
# 	elif c == curses.KEY_HOME:
# 		x = y = 0

# curses.endwin()


       # inkey = _Getch()
       #  while(1):
       #          k=inkey()
       #          if k!='':break
       #  if k=='\x1b[A':
       #          print ("up")
       #  elif k=='\x1b[B':
       #          print ("down")
       #  elif k=='\x1b[C':
       #          print ("right")
       #  elif k=='\x1b[D':
       #          print ("left")
       #  else:
       #          print ("not an arrow key!")

import sys, tty, termios, codecs, unicodedata
from contextlib import contextmanager

def callback(text):
    print '\r' + text.upper()

read_input(callback)
