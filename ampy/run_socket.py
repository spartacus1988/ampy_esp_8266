
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
		i = 0
		for n in self.my_ssid:
			i += ord(n)
		while i!=0:
			i = i-1
			channel = urandom.getrandbits(4)
		if channel > 11:
			channel =  16 - channel
		self.my_channel = channel
		self.ap_if.config(essid=self.my_ssid, channel=self.my_channel)
		network.phy_mode(3)


	def __await__(self, timeout, V_Writer):
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		self._init_ap_if()
		await asyncio.sleep(1)
		print("voltages_is " + str(V_Writer.voltages))
		self.serverSocket.settimeout(timeout)
		print("my_channel_is " + str(self.my_channel))
		print("my_channel_is " + str(type(self.my_channel)))
		
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
					

			cl.write(b'HTTP/1.0 200 OK\r\n'
				b'Content-type: text/html; charset=utf-8\r\n'
				b'\r\n')
			cl.write(b'<!DOCTYPE html><body>\r\n')

			if V_Writer.voltages == {}:
				V_Writer.voltages[self.my_ssid] = self.sVin
			if self.my_ssid not in V_Writer.voltages.keys():
				V_Writer.voltages[self.my_ssid] = self.sVin
			for key in V_Writer.voltages.keys():
				if key == self.my_ssid:
					V_Writer.voltages[self.my_ssid] = self.sVin
				cl.write(b'<h3>%s=%s</h3>\r\n' % (key, V_Writer.voltages[key]))

			cl.write(b'</body></html>\r\n')
			cl.close()


		except:
			print("loop socket_EXCEPTION")
			#await asyncio.sleep(5)
				

	__iter__ = __await__ 