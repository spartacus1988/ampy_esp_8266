import	network

class Connect:
	
	def __init__(self):
		self.sta_if = network.WLAN(network.STA_IF)
		self.ip = '0.0.0.0'


	def connect_to(self, SSID, password):
		if not self.sta_if.isconnected():
			self.sta_if.active(True)
			self.sta_if.connect(SSID, password)
			count_expected = 0
			while	not	self.sta_if.isconnected():
				count_expected += 1		
				for i in range(count_expected):
            				pass
				if count_expected > 100:
					print('Timeout connection was occured')
					break		
			print('network	config:',	self.sta_if.ifconfig())
			print('ip_sta_is:',	self.sta_if.ifconfig()[0])
			self.ip = self.sta_if.ifconfig()[0]
			return self.ip
		else:
			print('already connection was established')

