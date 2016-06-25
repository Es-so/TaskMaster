#!/usr/bin/env python

import cmd

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

