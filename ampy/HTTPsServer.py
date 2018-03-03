import uasyncio as asyncio
from	machine	import	ADC
import	socket
import	network
import	time
import extract_credential
import connect



async def fetch_ip(SSID, password):
    try:
    	#print(SSID)
    	#print(password)
    	await Connect.__await__(SSID, password) 
    	#await sta_if.connect(SSID, password)   
    except asyncio.TimeoutError:
        print('Got timeout')
	return Connect.ip	


async def wait_for_fetch_ip(ssid):
		while True:
			print("pending_1")
			#print(str(pending))  #error
			return await asyncio.wait_for(fetch_ip(ssid, SSIDpass.credentials[ssid]), 10)
			#return await asyncio.wait_for(fetch_ip(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]]), 10)
			#if pending:
    		#print("pending_2")
    		#await asyncio.sleep(2)
    		#print("pending_3")
    		#print(SSIDpass.credentials)
    		#print(SSIDpass.SSID)


async def wrapper_wait_for_fetch_ip(SSIDpass):
	for ssid in SSIDpass.SSID:
		pending = await wait_for_fetch_ip(ssid)
		print(str(pending))


#instance STA
#sta_if = network.WLAN(network.STA_IF)


#instance loop
loop = asyncio.get_event_loop()

#instanse class Connect
Connect = connect.Connect()


#Connect.ip = Connect.__await__(SSIDpass.SSID[0], SSIDpass.credentials[SSIDpass.SSID[0]])
#print('ip_sta_now_is:', Connect.ip)
 

#instance class SSIDpass
SSIDpass = extract_credential.SSIDpass()  
SSIDpass.extract_credentials_data('/credentials.txt')
#print(SSIDpass.credentials)
#print(SSIDpass.SSID)
#print(SSIDpass.credentials[SSIDpass.SSID[0]])


#init ADC	
LSB = 3.3/1024	
adc = ADC(0)	
	



#init socket
#print("socket DONE")

#for ssid in SSIDpass.SSID:
#	print(ssid)


#loop forever
#loop.create_task(wait_for_fetch_ip(SSIDpass))

loop.create_task(wrapper_wait_for_fetch_ip(SSIDpass))




#loop.create_task(bar())

loop.run_forever()
