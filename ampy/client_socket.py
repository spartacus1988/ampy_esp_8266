import urequests as requests
import uasyncio as asyncio
import network



class clientSocketClass:
	
	def __init__(self):
		self.addr = ('192.168.4.1', 8080)
		self.sta_if = network.WLAN(network.STA_IF)

	def __await__(self):
		print("client socket")
		if str(self.sta_if.ifconfig()[0]) != '0.0.0.0':
			try:
				r = requests.get("http://192.168.4.1:8080/")
				print(r.text)
				# if r.text == 'parameter location was not included in the GET request':
				# 	print('r.text is None')
				# 	r.close()
				# 	return None
				text = r.text
				r.close() 
				return text			
			except:
				print('request was failed')
		else:
			print('NO_IP')
			return None			
		await asyncio.sleep(1) 


	__iter__ = __await__ 