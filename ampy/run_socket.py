
import	socket
from	machine	import	ADC
import uasyncio as asyncio
import network
import urandom

class serverSocketClass:
	
	def __init__(self):
		self._init_ap_if()
		# self.ap_if = network.WLAN(network.AP_IF)
		# self.ap_if.active(True)
		self.addr = ('192.168.4.1', 8080)
		self.serverSocket = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)
		self.serverSocket.settimeout(1)
		self.serverSocket.bind(self.addr)
		self.serverSocket.listen(5)
		#init ADC	
		self.LSB = 3.3/1024	
		self.Dn = None
		self.vin = None
		self.sVin = None
		self.adc = ADC(0)

	def _init_ap_if(self):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		await asyncio.sleep(1) 
		self.my_ssid = self.ap_if.config('essid')
		#self.my_ssid = 'MicroPython-06ab27'
		print(self.my_ssid)
		channel = urandom.getrandbits(4)
		if channel > 11:
			channel =  16 - channel
		self.my_channel = channel

		#print(self.my_ssid)
		#print(self.my_channel)

		self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)

		#print(self.my_ssid)
		#self.ap_if.config(channel=self.my_channel)
		network.phy_mode(3)







	def __await__(self, timeout, V_Writer):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		await asyncio.sleep(1)
		print("voltages_is " + str(V_Writer.voltages))
		self.serverSocket.settimeout(timeout)
		
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
			#print(self.my_ssid)
			#d = "dsdsdsdsadsda"
			#d = self.my_ssid
				

			#Prepare the response
			response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
			response += """<!DOCTYPE html>
			<html>
			<body>
			<h3>Voltage on pin A0 =	%sV </h3>
			</body>
			</html>\n""" % self.sVin



			# #Prepare the response
			# response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
			# response += """<!DOCTYPE html>
			# <html>
			# <body>
			# <h3>Voltage on pin A0 =	dfsdfsdV </h3>
			# </body>
			# </html>\n"""

			# print("voltages_is " + str(V_Writer.voltages))
			# #V_Writer.voltages = {'dict': 1, 'dictionary': 2}

			# print("self.my_ssid_is " + str(self.my_ssid))

			# for key in V_Writer.voltages.keys():
			# 	if key == self.my_ssid:
			# 		V_Writer.voltages[key] = self.sVin 
			# if V_Writer.voltages == {}:
			# 	V_Writer.voltages[self.my_ssid] = self.sVin 
			
			# for key in V_Writer.voltages.keys():
			# 	pass
			# 	#response += """<h3>%s=%s</h3>""" % (key, V_Writer.voltages[key])

			#response +="""</body></html>\n"""



			#response = sVin
			cl.send(response)
			cl.close()
		except:
			await asyncio.sleep(5)
				

	__iter__ = __await__ 