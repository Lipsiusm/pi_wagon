import threading
import os

def do_stress():
	os.system('yes')

command = do_stress()

for i in range(20):
	i = threading.Thread(target=command)
	i.start()
	print(i)