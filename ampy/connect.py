import	network
import uasyncio as asyncio

class Connect:
	
	def __init__(self):
		self.sta_if = network.WLAN(network.STA_IF)
		self.ap_if = network.WLAN(network.AP_IF)
		self.ap_if.active(True)
		#await asyncio.sleep(1) 
		self.my_ssid = self.ap_if.config('essid')
		self.ip = '0.0.0.0'
		self.sta_if.active(True)
		self.ap_if.active(False)
		#await asyncio.sleep(1) 

	def __await__(self, SSID, password):
		if SSID == self.my_ssid:
			return '0.0.0.0'
		self.ap_if.active(False)
		self.sta_if.connect(SSID, password)
		while	not	self.sta_if.isconnected():
			print('SSID:' + SSID)
			await asyncio.sleep(1) 
		self.ip = self.sta_if.ifconfig()[0]
		return self.ip		
	

	__iter__ = __await__ 		
		




