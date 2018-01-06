import os


class SSIDpass:
 
	def __init__(self):
        	self.SSID = []
        	self.credentials = {}


	def extract_credentials_data(self, pathfile):
		self.SSID = []
		self.credentials = {}
		with open(pathfile, 'r') as f:
        		for line in f:
                		ssid, pwd = line.strip().split(':')
                		self.credentials[ssid] = pwd
				self.SSID.append(ssid)
                		break
            		
