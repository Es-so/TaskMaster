from cmd_data import cmd_data
import yaml

def load_conf(file):
	try:
		fd = open(file, "r")
		data = yaml.load(fd)
		return data
	except Exception, e:
		print("error config -> " + file)

def check_pid(cmd, line):
	try:
		for k, v in cmd.iteritems():
			curr = cmd[k]
			if (curr.process and curr.process.pid == int(line)):
				return (curr)
	except Exception, e:
		return (None)

class cmd_info:

	def __init__(self):
		i = 1
		data = load_conf("config.yaml")
		cmd = data.get("programs")
		self.cmd = {}
		for k, v in cmd.iteritems():
			cmd_class = cmd_data(k, v)
			self.cmd[k] = cmd_class
			while (i < cmd_class.numprocs):
				name = k + str(i)
				self.cmd[name] = cmd_data(name, v)
				i += 1

	def	autostart(self):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			if (cmd.autostart):
				cmd.start()

	def	start(self, line):
		find = False
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			if (line and cmd.id == line):
				find = True
				if (cmd.status == "WAITING"):
					cmd.start();
				elif (cmd.status == "RUNNING"):
					print ("task: Command " + line + " already RUNNING")
				break
		if (find == False):
			print ("task: no process found " + line)

	def	restart(self, line):
		curr = check_pid(self.cmd, line)
		if (curr != None):
			curr.restart()
		else:
			print ("task: no process found " + line)

	def	stop(self, line):
		curr = check_pid(self.cmd, line)
		if (curr != None):
			curr.stop()
		else:
			print ("task: no process found " + line)

	def	status(self):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			cmd.show_status()


