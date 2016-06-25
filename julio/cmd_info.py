from cmd_data import cmd_data
import yaml

def load_conf(file):
	try:
		fd = open(file, "r")
		data = yaml.load(fd)
		return data
	except Exception, e:
		print("error config -> " + file)

class cmd_info:
	def __init__(self):
		data = load_conf("config.yaml")
		cmd = data.get("programs")
		self.cmd = {}
		for k, v in cmd.iteritems():
			cmd_class = cmd_data(k, v)
			self.cmd[k] = cmd_class
	def	start(self, line):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			if (line and cmd.id == line):
				cmd.start()
				break

	def	autostart(self):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			if (cmd.autostart):
				cmd.start()

	def	restart(self, line):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			if (line and cmd.id == line):
				cmd.restart()

	def	status(self):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			cmd.show_status()

	def	stop(self, line):
		for k, v in self.cmd.iteritems():
			cmd = self.cmd[k]
			if (line and cmd.id == line):
				cmd.stop()
				break


