import os
import shlex
import subprocess
import pyautogui
#http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python

class cmd_data:

	def __init__(self, key, params):
		self.id = key
		self.path = params["cmd"]
		self.stdout = params["stdout"]
		self.stderr = params["stderr"]
		self.autostart = params["autostart"]
		self.autorestart = params["autorestart"]
		self.exit = params["exitcodes"]
		self.numprocs = params["numprocs"]
		self.status = "WAITING"
		self.process = None
		self.time = 0

	def start(self):
		try:
			cmd_split = shlex.split(self.path)
			stdout_path = open(self.stdout, "a")
			stderr_path = open(self.stderr, "a")
			proc = subprocess.Popen(
				cmd_split,
				stdin = subprocess.PIPE,
				stdout = stdout_path,
				stderr = stderr_path,
				env = os.environ
			)
			self.status = "RUNNING"
			self.process = proc
			self.show_status()
		except Exception, e:
			print("error execution -> " + self.id)

	def stop(self):
		self.process.terminate()

	def show_status(self):
		if (self.process):
			print('{0:20}{1:15}{2:15}{3:15}{4:15}'.format(self.id, self.status, "  pid ", str(self.process.pid), "  uptime ", str(self.time)))
		else:
			print('{0:20}{1:15}{2:15}{3:15}{4:15}'.format(self.id, self.status, "  pid ", '0', "  uptime ", str(self.time)))

	def restart(self):
		self.stop()
		self.start()

	def finish(self, signal, signum):
		print ("\n" + self.id + ": processus done return_code : " + signal)
		self.process = None
		self.status = "WAITING"
		for exit in self.exit:
			if (exit == signum):
				self.start()
		pyautogui.press('enter')
