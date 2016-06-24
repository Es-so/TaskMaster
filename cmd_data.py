import os

class cmd_data:

	def __init__(self, key, params):
		self.id = key
		self.path = params["cmd"]
		self.autostart = params["autostart"]
		self.autorestart = params["autorestart"]
		self.status = "WAITING"
		self.pid = '0'
		self.time = '0'

	def start(self):
		print("start " + self.id)
		try:
			os.system(self.path)
			self.status = "RUNNING"
		except Exception, e:
			print("error exec -> " + self.id)

	def restart(self):
		print("restart " + self.id)

	def kill(self):
		print("kill " + self.id)

	def show_status(self):
		print(self.id + "\t\t\t\t" + self.status + "\t  pid " + self.pid + "\t  uptime " + self.time)


