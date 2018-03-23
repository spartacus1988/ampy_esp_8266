
import	socket
from	machine	import	ADC
import uasyncio as asyncio
import network


class serverSocketClass:
	
	def __init__(self):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		self.addr = ('192.168.4.1', 8080)
		self.serverSocket = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)
		self.serverSocket.settimeout(10)
		self.serverSocket.bind(self.addr)
		self.serverSocket.listen(3)
		#init ADC	
		self.LSB = 3.3/1024	
		self.Dn = None
		self.vin = None
		self.sVin = None
		self.adc = ADC(0)


	def __await__(self):

		self.ap_if.active(True)
		await asyncio.sleep(1)
		while True:
			try:
				print("loop socket")
				cl, addr = self.serverSocket.accept()
				cl_file	= cl.makefile('rwb', 0)
				while	True:
					line = cl_file.readline()
					#yield from asyncio.sleep(1) 
					#await asyncio.sleep(1)
					if not line or line == b'\r\n':
						break
				self.Dn = self.adc.read()
				self.vin = self.LSB * self.Dn
				self.sVin = "{:.3f}".format(self.vin)

				

				#Prepare the response
				response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
				response += """<!DOCTYPE html>
				<html>
				<body>
				<h3>Voltage on pin A0 =	%sV </h3>
				</body>
				</html>\n""" % self.sVin


				#response = sVin
				cl.send(response)
				cl.close()
			except:
				await asyncio.sleep(5)
				

	__iter__ = __await__ 