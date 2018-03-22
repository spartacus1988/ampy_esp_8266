import	socket
import uasyncio as asyncio



class clientSocketClass:
	
	def __init__(self):
		self.addr = ('192.168.4.1', 8080)
		self.cl_sock = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)

		

		#sock = socket.socket()
		#sock.connect(('localhost', 9090))
		#sock.send('hello, world!')

		#data = sock.recv(1024)
		#sock.close()

		#print data
	


	def __await__(self):

		while True:
			print("loop client socket")
			#yield from asyncio.sleep(1) 

			try:
				self.cl_sock.connect(self.addr)
				self.cl_sock.send('hello, world!')
				data = self.cl_sock.recv(1024)			
				self.cl_sock.close()

				print(data)

				yield from asyncio.sleep(5) 
			except:
				yield from asyncio.sleep(5) 
				pass



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