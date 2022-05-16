import socket
import pi_wagon_api

#echo server built along side https://realpython.com/python-sockets/

ip_addr = "192.168.1.81"
port = 42069
pi = pi_wagon_api.pi_wagon_api()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((ip_addr, port))
	s.listen()

	conn, addr = s.accept()

	with conn:
		print(f'Connected from {addr}')

		while True:
			data = conn.recv(1024)
			if not data:
				break
			#stripping the newline characters
			if data.decode('utf-8').strip() == 'cpuinfo':
				cpu_info = pi.get_cpu_info()
				#send pi cpu info to client
				conn.sendall(cpu_info.encode('utf-8'))

			if data.decode('utf-8').strip() == 'red':
				color_red = pi.red_light()
				
			if data.decode('utf-8').strip() == 'blue':
				color_blue = pi.blue_light()
				
			if data.decode('utf-8').strip() == 'green':
				color_green = pi.green_light()

			if data.decode('utf-8').strip() == 'temp':
				cpu_temp = pi.get_cpu_temp()
				conn.sendall(cpu_temp.encode('utf-8'))
			
			
			#conn.sendall(data)