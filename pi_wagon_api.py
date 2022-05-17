import os
from gpiozero import LED

class pi_wagon_api:

	a = LED(2)
	b = LED(3)
	c = LED(4)
	d = LED(17)
	e = LED(27)
	f = LED(22)
	g = LED(10)
	h = LED(9)
	i = LED(11)
	j = LED(0)
	
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

	def all_lights(self):
		self.a.toggle()
		self.b.toggle()
		self.c.toggle()
		self.d.toggle()
		self.e.toggle()
		self.f.toggle()
		self.g.toggle()
		self.h.toggle()
		self.i.toggle()
		self.j.toggle()


	#get the current cpu temp
	def get_cpu_temp(self):
		return os.popen('vcgencmd measure_temp').read()