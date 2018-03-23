import uasyncio as asyncio
from	machine	import	ADC
import	socket
import	network
import	time
import extract_credential
import connect
import run_socket
import client_socket
import vol_writer


async def fetch_ip(SSID, password):
	try:
		return await Connect.__await__(SSID, password) 
	except asyncio.TimeoutError:
		print('Got timeout fetch_ip')
	


async def wait_for_fetch_ip(ssid):
		while True:		
			return await asyncio.wait_for(fetch_ip(ssid, SSIDpass.credentials[ssid]), 10)
	

async def wrapper_wait_for_fetch_ip(SSIDpass):
	while True:
		for ssid in SSIDpass.SSID:
			pending_ip = await wait_for_fetch_ip(ssid)
			print('pending_ip is: ', str(pending_ip))
			request = await Cl_Socket.__await__()  
			text = V_Writer.__await__(request)
			print('text_is ' + str(text))
			await asyncio.sleep(1)


async def wait_for_run_server_socket():
		while True:
			await ServSocket.__await__() 
			await asyncio.sleep(1)


# async def wait_for_client_socket():
# 		while True:
# 			await Cl_Socket.__await__()  
# 			#yield from asyncio.sleep(1)
# 			await asyncio.sleep(1)






if __name__ == '__main__':

	#instance loop
	loop = asyncio.get_event_loop()

	#instanse class Connect
	Connect = connect.Connect()

	#instanse class ServSocket
	ServSocket = run_socket.serverSocketClass()

	#instanse class Cl_Socket
	Cl_Socket = client_socket.clientSocketClass()

	#instanse class voltageWriter
	V_Writer = vol_writer.voltageWriter()

	#instance class SSIDpass
	SSIDpass = extract_credential.SSIDpass()  
	SSIDpass.extract_credentials_data('/credentials.txt')



	loop.create_task(wait_for_run_server_socket())

	#loop.create_task(wait_for_client_socket())

	loop.create_task(wrapper_wait_for_fetch_ip(SSIDpass))

	loop.run_forever()


