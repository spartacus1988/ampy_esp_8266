import uasyncio as asyncio
from	machine	import	ADC
import	socket
import	network
import	time
import extract_credential
import connect
from machine import UART



async def sender():
    swriter = asyncio.StreamWriter(uart, {})
    while True:
        await swriter.awrite('Hello uart\n')
        await asyncio.sleep(5)

async def receiver():
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.readline()
        print('Recieved', res)
        await asyncio.sleep(5)



async def bar():
    count = 0
    while True:
        count += 1
        print(count)
        await asyncio.sleep(1)  




async def fetch_ip(SSID, password):
    try:
    	await Connect.__await__(SSID, password) 
    	#await sta_if.connect(SSID, password)   
    except asyncio.TimeoutError:
        print('Got timeout')

	return Connect.ip	


async def wait_for_fetch_ip(SSID, password):
	while True:
		await asyncio.wait_for(fetch_ip(SSID, password), 10)
    	await asyncio.sleep(5)
    	print(SSIDpass.credentials)
    	print(SSIDpass.SSID)



#instanse UART
uart = UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

#instanse STA
sta_if = network.WLAN(network.STA_IF)

#instanse loop
loop = asyncio.get_event_loop()

#instanse class SSIDpass
SSIDpass = extract_credential.SSIDpass()  
SSIDpass.extract_credentials_data('/credentials.txt')
print(SSIDpass.credentials)
print(SSIDpass.SSID)
print(SSIDpass.credentials[SSIDpass.SSID[0]])

#instanse class Connect
Connect = connect.Connect()
Connect.ip = Connect.connect_to(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]])
print('ip_sta_now_is:', Connect.ip)
 

#init Wi-Fi




#sta_if	= network.WLAN(network.STA_IF)
#ap_if	= network.WLAN(network.AP_IF)
#ap_if.active(False)
#ap_if.active(True)
#print("DEBUG PRINT")
#print(ap_if.isconnected())
#if not sta_if.isconnected():
#	sta_if.active(True)
#	sta_if.connect(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]])
#	while	not	sta_if.isconnected():
#		pass
#	print('network	config:',	sta_if.ifconfig())
#	print('ip_sta_is:',	sta_if.ifconfig()[0])


#compulsory pause	
time.sleep(2)
	


#init ADC	
LSB = 3.3/1024	
adc = ADC(0)	
	

#create socket addr
#addr = ('192.168.8.105', 8082)
#addr = (sta_if.ifconfig()[0], 8082)
addr = ('192.168.4.1', 8082)


#init socket
#serverSocket = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)
#serverSocket.bind(addr)
#serverSocket.listen(3)
print("socket DONE")




#loop forever
loop.create_task(wait_for_fetch_ip(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]])) # Schedule ASAP
#loop.create_task(wait_for_fetch_ip(SSIDpass.SSID[1], SSIDpass.credentials[SSIDpass.SSID[1]])) 

#loop.run_until_complete(wait_for_fetch_ip(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]]))

#loop.create_task(bar())
loop.create_task(sender())
loop.create_task(receiver())
loop.run_forever()












while True:
	#print("loop")
	cl, addr = serverSocket.accept()
	cl_file	= cl.makefile('rwb', 0)
	while	True:
		line = cl_file.readline()
		if not line or line == b'\r\n':
			break
	Dn = adc.read()
	vin = LSB * Dn
	sVin = "{:.3f}".format(vin)

	

	#Prepare the response
	response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
	response += """<!DOCTYPE html>
	<html>
	<body>
	<h3>Voltage on pin A0 =	%sV </h3>
	</body>
	</html>\n""" % sVin


	#response = sVin
	cl.send(response)
	cl.close()





	

