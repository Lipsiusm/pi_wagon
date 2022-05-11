import os
from gpiozero import LED

class pi_wagon_api:
	red = LED(17)
	green = LED(22)
	blue = LED(27)

	def __init__(self):
		print('Created Pi Wagon Object')

	#get the current cpu info and return it
	def get_cpu_info(self):
		return os.popen('cat /proc/cpuinfo').read()

	def red_light(self):
		self.red.toggle()

	def blue_light(self):
		self.blue.toggle()

	def green_light(self):
		self.green.toggle()