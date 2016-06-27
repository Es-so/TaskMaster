import cmd
import signal
from cmd_info import cmd_info

task = None

def sig_int(signal, frame):
	print "CTRL_C"

def sig_alarm(signum, frame):
	for k, v in task.cmd.iteritems():
		cmd = task.cmd[k]
		if (cmd.process and cmd.process.poll()):
			ret = cmd.process.returncode
			if (ret < 0):
				ret *= -1
			for k, v in signal.__dict__.iteritems():
				if k.startswith('SIG') and not k.startswith('SIG_'):
					if (v == ret):
						cmd.finish(k, v);
	signal.alarm(1)

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = 'task MASTER: '

    def emptyline(self):
    	pass

    def do_status(self, line):
    	task.status()

    def do_start(self, line):
    	task.start(line)

    def do_stop(self, line):
    	if (line != ""):
    		task.stop(line)
    	else:
    		print("task: need PID to stop")

    def do_restart(self, line):
    	task.restart(line)

    def do_reload(self, line):
    	print("reload: " + line)

    def do_help(self, line):
    	print ("cmd: <status/start/stop/restart> [all/name/pid] || <reload/quit> ")

    def do_catch(self, line):
    	for k, v in task.cmd.iteritems():
    		cmd = task.cmd[k]
    		if (cmd.process.poll):
    			print cmd.process.returncode
    		else:
    			print "not launch"
    def do_quit(self, line):
        return True


if __name__ == "__main__":
	signal.signal(signal.SIGALRM, sig_alarm)
	signal.signal(signal.SIGINT, sig_int)
	signal.alarm(1)
	task = cmd_info()
	task.status()
	task.autostart()
	HelloWorld().cmdloop()
