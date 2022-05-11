import os

class pi_wagon_api:

	def __init__(self):
		print('Created Pi Wagon Object')

	#get the current cpu info and return it
	def get_cpu_info(self):
		return os.popen('cat /proc/cpuinfo').read()