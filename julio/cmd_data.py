import os
import shlex
import subprocess

#http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

class cmd_data:

	def __init__(self, key, params):
		self.id = key
		self.path = params["cmd"]
		self.stdout = params["stdout"]
		self.stderr = params["stderr"]
		self.autostart = params["autostart"]
		self.autorestart = params["autorestart"]
		self.status = "WAITING"
		self.pid = 0
		self.time = 0
		self.process = None

	def start(self):
		print("start " + self.id)
		try:
			cmd_split = shlex.split(self.path)
			stdout_path = open(self.stdout, "a")
			stderr_path = open(self.stderr, "a")
			proc = subprocess.Popen(cmd_split,
					stdin = subprocess.PIPE,
					stdout = stdout_path,
					stderr = stderr_path,
					env = os.environ
					)
			self.status = "RUNNING"
			self.pid = proc.pid
			self.process = proc
		except Exception, e:
			print("error execution -> " + self.id)

	def restart(self):
		print("restart " + self.id)

	def stop(self):
		print("kill " + self.id)
		if (self.process):
			self.process.terminate()
			self.status = "WAITING"
			self.pid = 0
			self.time = 0
			self.process = None
		else:
			print "not start"

	def show_status(self):
		print(self.id + "\t\t\t\t" + self.status + "\t  pid " + str(self.pid) + "\t  uptime " + str(self.time))


