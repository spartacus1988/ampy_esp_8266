
import	socket
from	machine	import	ADC
import uasyncio as asyncio
import network
import urandom

class serverSocketClass:
	
	def __init__(self):
		self._init_ap_if()
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		self.addr = ('192.168.4.1', 8080)
		self.serverSocket = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)
		self.serverSocket.settimeout(5)
		self.serverSocket.bind(self.addr)
		self.serverSocket.listen(5)
		#init ADC	
		self.LSB = 3.3/1024	
		self.Dn = None
		self.vin = None
		self.sVin = None
		self.adc = ADC(0)
		self.my_ssid = self.ap_if.config('essid')
		i = 0
		for n in self.my_ssid:
			i += ord(n)
		#i = len(self.my_ssid)
		#i = urandom.getrandbits(4)
		while i!=0:
			i = i-1
			channel = urandom.getrandbits(4)
		if channel > 11:
			channel =  16 - channel
		self.my_channel = channel

		self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)
		network.phy_mode(3)


	def _init_ap_if(self):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		await asyncio.sleep(1) 
		self.my_ssid = self.ap_if.config('essid')
		#self.my_ssid = 'MicroPython-06ab27'
		print(self.my_ssid)
		# channel = urandom.getrandbits(4)
		# if channel > 11:
		# 	channel =  16 - channel
		# self.my_channel = channel
		# print("my_channel_is" + self.my_channel)

		#print(self.my_ssid)
		#print(self.my_channel)

		self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)

		#print(self.my_ssid)
		#self.ap_if.config(channel=self.my_channel)
		network.phy_mode(3)


	def __await__(self, timeout, V_Writer):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		self._init_ap_if()
		await asyncio.sleep(1)
		print("voltages_is " + str(V_Writer.voltages))
		self.serverSocket.settimeout(timeout)
		print("my_channel_is " + str(self.my_channel))
		
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
					
			#V_Writer.voltages ={'MicroPython-06ab27': 'micropythoN', 'MicroPython-06ab0a': 'micropythoN'}
			#Prepare the response
			# response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
			# cl.send(response)
			# response = """<!DOCTYPE html><html><body>"""
			# cl.send(response)
			# if V_Writer.voltages == {}:
			# 	V_Writer.voltages[self.my_ssid] = self.sVin
			# for key in V_Writer.voltages.keys():
			# 	response = """<h3>%s=%s</h3>""" % (key, V_Writer.voltages[key])
			# 	cl.send(response)
			# response ="""</body></html>\n"""
			# cl.send(response)
			# cl.close()


			# response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
			# response += """<!DOCTYPE html>
			# <html>
			# <body>
			# <h3>Voltage on pin A0 =	dfsdfsdV </h3>
			# </body>
			# </html>\n"""
			# cl.send(response)
			# cl.close()



			cl.write(b'HTTP/1.0 200 OK\r\n'
				b'Content-type: text/html; charset=utf-8\r\n'
				b'\r\n')
			cl.write(b'<!DOCTYPE html><html><head><title>')

			clisock.write(b'<html><body><h3>Voltage on pin A0 =	dfsdfsdV </h3></body></html>}\r\n')
			cl.close()


		except:
			print("loop socket_EXCEPTION")
			#await asyncio.sleep(5)
				

	__iter__ = __await__ 