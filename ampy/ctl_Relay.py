import network
from	machine	import	ADC
from machine import Pin


class control_Relay:
	
	def __init__(self):
		self.ap_if = network.WLAN(network.AP_IF)
		self.my_ssid = self.ap_if.config('essid')
		self.voltages = {}
		self.values_voltages = []
		#init ADC
		####3.5 = +40kOhm ### 3.6 = +47kOhm #### 3.2 = default (100k+220k on the board)	
		self.LSB = 3.52/1024	
		self.Dn = None
		self.vin = None
		self.sVin = None
		self.adc = ADC(0)
		self.summ = 0
		self.average = 0
		#measure the voltage
		self.Dn = self.adc.read()
		self.vin = self.LSB * self.Dn
		self.sVin = "{:.3f}".format(self.vin)
		#init Relay
		self.relay = Pin(5, Pin.OUT)
		self.state_relay = "OFF"
	

	def check_self_state(self, voltages):

		#measure the voltage
		self.Dn = self.adc.read()
		self.vin = self.LSB * self.Dn
		self.sVin = "{:.3f}".format(self.vin)

		#getting voltages
		self.voltages = voltages


		# ############DEBUG#################
		# self.voltages = {'MicroPython-06ab27': '3.45', 'MicroPython-06ab0a': '3.3'}
		# self.vin = 3.45
		# self.sVin = "3.45"
		# ###########DEBUG#################



		#add self.sVin
		if self.my_ssid not in self.voltages.keys():
			self.voltages[self.my_ssid] = self.sVin

		#update self.voltages
		for key in self.voltages.keys():
			if key == self.my_ssid:
				self.voltages[self.my_ssid] = self.sVin

		#extract values in list
		for value in self.voltages.values():
			self.values_voltages.insert(0, value)
			#print("value_is "+ str(value))
			#print("type_of_value_is "+ str(type(value)))
			#print("type_of_self.sVin_is "+ str(type(self.sVin)))
			#print("type_of_self.sVin_is "+ str(type(self.vin)))

		#check if more then max
		if self.vin > 3.55:
			self.relay.on()
			self.state_relay = "ON"
			print("relay was ON by self.vin > 3.55")
			return self.state_relay	

		#calc self.summ
		self.summ = 0
		for value in self.values_voltages:
			self.summ += float(value)

		#calc self.average
		self.average = self.summ / len(self.values_voltages)
		print("self.average_is " + str(self.average))

		#check if batteries unbalanced
		if self.vin > self.average + 0.05 and self.vin > 3.10:
			self.relay.on()
			self.state_relay = "ON"
			print("relay was ON by self.vin > self.average + 0.05 and self.vin > 3.10")
			return self.state_relay

		#check if batteries balanced
		if self.vin < self.average + 0.03: #and self.vin < 3.50:
			self.relay.off()
			self.state_relay = "OFF"
			print("relay was OFF by self.vin < self.average + 0.03")
			return self.state_relay

		#this if must be latest
		#check if less then 3.00
		if self.vin < 3.00:
			self.relay.off()
			self.state_relay = "OFF"
			print("relay was OFF by self.vin < 3.00")
			return self.state_relay
		return self.state_relay





