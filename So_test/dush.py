#!/usr/bin/env python

import cmd
import random
import sys
import time
import random
import sys
from threading import Thread, RLock
import threading
import logging
import time

verrou = RLock()


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

# class MyThreadWithArgs(threading.Thread):_____________________________________

class Afficheur(Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		return

	def run(self):
		print ("A")
		# logging.debug('running with %d', self)
		return

    # # def __init__(self):
    #     # Thread.__init__(self)
    #     # self.mot = mot

    # def run(self):
    #     i = 0
    #     while i < self:
    #     	print ("A")
    #     	i += 1
#_______________________________________________________________________________
# thread_2 = Afficheur("TORTUE")


def start_process(arg):
	i = 0
	print("START PROCESS" + arg)
	thread_1 = Afficheur(int(arg))
	thread_1.start()
	thread_1.join()
	# while i < int(arg):
	# 	time.sleep(1)
	# 	sys.stdout.write(str(i))
	# 	sys.stdout.flush()
	# 	attente = 1
	# 	# attente += random.randint(1, 60) / 100
	# 	i += 1


class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_status(self, line):
    	print("statut: \n")

    def do_start(self, line):
    	print("start: \n" + line)
    	start_process(line)

    def do_stop(self, line):
    	print("stop: " + line)

    def do_restart(self, line):
    	print("restart: " + line)

    def do_reload(self, line):
    	print("reload: " + line)

    def do_help(self, line):
    	print ("cmd: <status/start/stop/restart> [all/name/pid] || <reload/quit> ")

    def do_quit(self, line):
        return True

if __name__ == '__main__':


	try:
		str = HelloWorld().cmdloop()
		print ("Goodbye")
	except Exception, e:
		print ("unknow cmd")
		str = HelloWorld().cmdloop()

