import cmd
from cmd_info import cmd_info

task = None

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_status(self, line):
    	task.status()

    def do_start(self, line):
    	task.start(line)

    def do_stop(self, line):
    	task.stop(line)

    def do_restart(self, line):
    	task.restart(line)

    def do_reload(self, line):
    	print("reload: " + line)

    def do_help(self, line):
    	print ("cmd: <status/start/stop/restart> [all/name/pid] || <reload/quit> ")

    def do_quit(self, line):
        return True

if __name__ == "__main__":
	task = cmd_info()
	task.status()
	task.autostart()
	HelloWorld().cmdloop()


