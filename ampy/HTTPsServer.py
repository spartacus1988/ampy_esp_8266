from	machine	import	ADC
import	socket
import	network
import	time
import extract_credential

#instanse class
SSIDpass = extract_credential.SSIDpass()  
SSIDpass.extract_credentials_data('/credentials.txt')
print(SSIDpass.credentials)
print(SSIDpass.SSID)
print(SSIDpass.credentials[SSIDpass.SSID[0]])



#init Wi-Fi
sta_if	= network.WLAN(network.STA_IF)
ap_if	= network.WLAN(network.AP_IF)
#ap_if.active(False)
ap_if.active(True)
print("DEBUG PRINT")
print(ap_if.isconnected())
if not sta_if.isconnected():
	sta_if.active(True)
	sta_if.connect(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]])
	while	not	sta_if.isconnected():
		pass
	print('network	config:',	sta_if.ifconfig())
	print('ip_sta_is:',	sta_if.ifconfig()[0])

#compulsory pause	
time.sleep(2)
	
	
LSB = 3.3/1024	
adc = ADC(0)	
	
#addr = ('192.168.8.105', 8082)
#addr = (sta_if.ifconfig()[0], 8082)
addr = ('192.168.4.1', 8082)
serverSocket = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)
serverSocket.bind(addr)
serverSocket.listen(3)




print("socket DONE")

#while False:
while True:
	print("loop")
	cl, addr = serverSocket.accept()
	cl_file	= cl.makefile('rwb', 0)
	while	True:
		line = cl_file.readline()
		if not line or line == b'\r\n':
			break
	Dn = adc.read()
	vin = LSB * Dn
	sVin = "{:.3f}".format(vin)

	
	response = sVin
	cl.send(response)
	cl.close()

	

