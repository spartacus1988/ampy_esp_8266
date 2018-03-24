
import	socket
from	machine	import	ADC
import uasyncio as asyncio
import network
import urandom



class serverSocketClass:
	
	def __init__(self):
		self._init_ap_if()
		#self.ap_if = network.WLAN(network.AP_IF)
		#self.ap_if.active(True)
		
		# self.my_ssid = self.ap_if.config('essid')
		# channel = urandom.getrandbits(4)
		# if channel > 11:
		# 	channel =  16 - channel
		# self.my_channel = channel
		# self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)
		# network.phy_mode(1)

		#self.ap_if.config(essid='FUCK_YOU_SSID', channel=7)
		#print(self.ap_if.config('channel'))
		#print(self.ap_if.config('essid'))
		#print(network.phy_mode())
		


		self.addr = ('192.168.4.1', 8080)
		self.serverSocket = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)
		#self.serverSocket.settimeout(1)
		self.serverSocket.bind(self.addr)
		self.serverSocket.listen(3)
		#init ADC	
		self.LSB = 3.3/1024	
		self.Dn = None
		self.vin = None
		self.sVin = None
		self.adc = ADC(0)



	def _init_ap_if(self):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		# self.my_ssid = self.ap_if.config('essid')
		# print(self.my_ssid)
		# channel = urandom.getrandbits(4)
		# if channel > 11:
		# 	channel =  16 - channel
		# self.my_channel = channel
		# self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)
		# network.phy_mode(3)



	def __await__(self, timeout):
		self.serverSocket.settimeout(timeout)
		#self.ap_if.active(True)
		#self.my_ssid = self.ap_if.config('essid')

		#self.ap_if.config(essid=self.my_ssid, channel=13)
		#self.ap_if.config(essid='FUCK_YOU_SSID', channel=7)
		#print('serverSocketClass__await__')


		#print(self.ap_if.config('channel'))
		#print(self.ap_if.config('essid'))
		#print(network.phy_mode())

		#await asyncio.sleep(1)
		while True:
			try:
				print("loop socket")
				#self._init_ap_if()
				#self.ap_if.active(True)
				# self.my_ssid = self.ap_if.config('essid')
				# channel = urandom.getrandbits(4)
				# if channel > 11:
				# 	channel =  16 - channel
				# self.my_channel = channel
				# self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)
				# network.phy_mode(1)
				
				
				print(self.ap_if.config('channel'))



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
				<h3>dfsdfsdgsdgsdgsd=%s</h3>
				</body>
				</html>\n""" % self.my_ssid# self.sVin# 'ssid', '5.0'


				#response = sVin
				cl.send(response)
				cl.close()
			except:
				await asyncio.sleep(timeout)
				

	__iter__ = __await__ 