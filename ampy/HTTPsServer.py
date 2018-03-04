import uasyncio as asyncio
from	machine	import	ADC
import	socket
import	network
import	time
import extract_credential
import connect
import run_socket
import client_socket



async def fetch_ip(SSID, password):
    try:
    	#print(SSID)
    	#print(password)
    	return await Connect.__await__(SSID, password) 
    	#await sta_if.connect(SSID, password)   
    except asyncio.TimeoutError:
        print('Got timeout fetch_ip')
	


async def wait_for_fetch_ip(ssid):
		while True:
			#print("pending_1")
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
	while True:
		for ssid in SSIDpass.SSID:
			pending_ip = await wait_for_fetch_ip(ssid)
			print('pending_ip is: ', str(pending_ip))
			
			await Cl_Socket.__await__() 




async def wait_for_run_server_socket():
		while True:
			await ServSocket.__await__() 






if __name__ == '__main__':

	#instance STA
	#sta_if = network.WLAN(network.STA_IF)


	#instance loop
	loop = asyncio.get_event_loop()

	#instanse class Connect
	Connect = connect.Connect()

	#instanse class ServSocket
	ServSocket = run_socket.serverSocketClass()

	#instanse class Cl_Socket
	Cl_Socket = client_socket.clientSocketClass()


	 

	#instance class SSIDpass
	SSIDpass = extract_credential.SSIDpass()  
	SSIDpass.extract_credentials_data('/credentials.txt')
	#print(SSIDpass.credentials)
	#print(SSIDpass.SSID)
	#print(SSIDpass.credentials[SSIDpass.SSID[0]])


		
		



	#print("socket DONE")





	loop.create_task(wait_for_run_server_socket())

	loop.create_task(wrapper_wait_for_fetch_ip(SSIDpass))




	#loop.create_task(bar())

	loop.run_forever()


