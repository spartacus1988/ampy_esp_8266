import socket
#from socket import *
import urequests as requests
import uasyncio as asyncio
import network



class clientSocketClass:
	
	def __init__(self):
		self.addr = ('192.168.4.1', 8080)
		# self.cl_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		# self.cl_sock.settimeout(15)
		pass
		

		#sock = socket.socket()
		#sock.connect(('localhost', 9090))
		#sock.send('hello, world!')

		#data = sock.recv(1024)
		#sock.close()

		#print data
	


	def __await__(self):

		self.sta_if = network.WLAN(network.STA_IF)
		self.ap_if = network.WLAN(network.AP_IF)

		




		while True:
			print("loop client socket")
			#yield from asyncio.sleep(1)

			# self.sta_if = network.WLAN(network.STA_IF)
			# self.ap_if = network.WLAN(network.AP_IF)
			# self.ap_if.active(False)
			#ap_if.active(False)
			#print(self.sta_if.ifconfig()[0]) 

			# if self.ap_if.active():
			# 	self.ap_if.active(False)



			#try:
			#self.addr = ('192.168.4.1', 8080)

			#self.addr = ("www.micropython.org", 80)
			

			self.cl_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
			print('getaddrinfo ' + str(socket.getaddrinfo("192.168.4.1", 8080)))

			#self.cl_sock.settimeout(15)

			if str(self.sta_if.ifconfig()[0]) != '0.0.0.0':
				pass



				r = requests.get("http://192.168.4.1:8080/")
				#print(r)
				#print(r.content)
				print(r.text)
				#print(r.content)
				#print(r.json())

				# It's mandatory to close response objects as soon as you finished
				# working with them. On MicroPython platforms without full-fledged
				# OS, not doing so may lead to resource leaks and malfunction.
				r.close()


				# print('type_is ' + str(type(self.addr)))
				# #print(str(self.addr))

				# #self.cl_sock.connect(('192.168.4.1', 8080))

				# #self.cl_sock.connect(('www.micropython.org', 80))


				# self.addr = socket.getaddrinfo("192.168.4.1",8080)[0][-1]
				# print(self.addr)


				# #self.cl_sock.connect(('176.58.119.26', 80))
				# #self.cl_sock.connect(('192.168.4.1', 8080))
				# self.cl_sock.connect(self.addr)







				# #print(socket.getaddrinfo('www.micropython.org', 80))


				# #self.cl_sock.connect(socket.getaddrinfo('www.micropython.org', 80)[0][-1])


				# print('connect')
				# self.cl_sock.send('hello, world!')
				# print('send')
				# data = self.cl_sock.recv(1)	
				# print('recv')		
				# self.cl_sock.close()
				# print('close')	

				# print('data')
				# print(data)
			else:
				print('NO_IP')

			

			yield from asyncio.sleep(1) 
			# except:
			# 	print('except')
			# 	yield from asyncio.sleep(1) 
			# 	pass



			# cl_file	= self.cl_sock.makefile('rwb', 0)
			# while	True:
			# 	try:
			# 		line = cl_file.readline()
			# 		print(line)
			# 		if not line or line == b'\r\n':
			# 			break
			# 	except:
			# 		pass

			# 	yield from asyncio.sleep(2) 

				

			# with open(cl_file, 'r') as f:
			# 	pass
				#for line in f:
					#print(line)






	__iter__ = __await__ 