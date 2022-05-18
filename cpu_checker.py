import os
from gpiozero import LED
from time import sleep

light_one = LED(2)
light_two = LED(3)
light_three = LED(4)
light_four = LED(17)
light_five = LED(27)
light_six = LED(22)
light_seven = LED(10)
light_eight = LED(9)
light_nine = LED(11)
light_ten = LED(0)

#list of LED objects already instantiated
list_of_lights = [light_one, light_two, light_three, light_four, \
light_five, light_six, light_seven, light_eight, light_nine, light_ten]


#get the current cpu info
def get_cpu_info():
	return os.popen('cat /proc/cpuinfo').read()

def lights_off():
	for light in list_of_lights:
		light.off()

def lights_on():
	for light in list_of_lights:
		light.on()

def update_led(temperature):

	#turn off all lights prior to new request
	for light in list_of_lights:
		light.off()

	for index, light in enumerate(list_of_lights):

		#if we're at 80+ degrees just turn on all lights
		if temperature >= 8:
			all_lights()
			break

		#otherwise normal operating temperatures will have a range of 1-8 lights
		if index > temperature:
			break
		
		light.on()

#get the current cpu temp
def get_curr_temp():

	temperature = os.popen('vcgencmd measure_temp').read()

	#temp returns 'temp=37.0', so i get the substring for just the number
	temperature_num = temperature[5:9:1]
	temperature = int(temperature_num[0])
	temperature_num = float(temperature_num)

	update_led(temperature)

	#return temp
	return str(temperature_num) + 'C'

def main():
	while True:
		curr_temp = get_curr_temp()
		print(curr_temp)
		sleep(10)

if __name__ == "__main__":
	main()