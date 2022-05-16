import os
from gpiozero import LED

class pi_wagon_api:

	red = LED(17)
	green = LED(27)
	blue = LED(22)
	
	def __init__(self):
		print('Created Pi Wagon Object')

	#get the current cpu info
	def get_cpu_info(self):
		return os.popen('cat /proc/cpuinfo').read()

	def red_light(self):
		self.red.toggle()

	def blue_light(self):
		self.blue.toggle()

	def green_light(self):
		self.green.toggle()

	#get the current cpu temp
	def get_cpu_temp(self):
		return os.popen('vcgencmd measure_temp').read()