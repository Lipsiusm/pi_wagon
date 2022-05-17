import os
from gpiozero import LEDBarGraph, CPUTemperature, LED
from signal import pause
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

	list_of_lights = [a,b,c,d,e,f,g,h,i,j]
	
	def __init__(self):
		print('Created Pi Wagon Object')

	#get the current cpu info
	def get_cpu_info(self):
		return os.popen('cat /proc/cpuinfo').read()

	def lights_off(self):
		for light in self.list_of_lights:
			light.off()

	def lights_on(self):
		for light in self.list_of_lights:
			light.on()


	#get the current cpu temp
	def get_cpu_temp(self):

		temp = os.popen('vcgencmd measure_temp').read()

		# cpu = CPUTemperature(min_temp=20, max_temp=80)
		# leds = LEDBarGraph(2, 3, 4, 17, 27, 22, 10, 9, 11, 0, pwm=True)

		# leds.source = cpu

		#temp returns 'temp=37.0', using the substring for just the number
		temp_num = temp[5:9:1]
		temp = int(temp_num[0])
		temp_num = float(temp_num)
		
		#turn off all lights prior to new request
		for light in self.list_of_lights:
			light.off()

		for index, light in enumerate(self.list_of_lights):

			#if we're at 80+ degrees just turn on all lights
			if temp >= 8:
				all_lights()
				break

			#otherwise normal operating temperatures will have a range of 1-8 lights
			if index > temp:
				break
			#if light
			light.on()

		#return temp
		return str(temp_num) + '\n'