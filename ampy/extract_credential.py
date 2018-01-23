import os

class SSIDpass:

    def __init__(self):
    	self.SSID = []
        self.credentials = {}


    def extract_credentials_data(self, pathfile):
        pass
        self.SSID = []
        self.credentials = {}
        
        with open(pathfile, 'r') as f:
            for line in f:
                ssid, pwd = line.strip().split(':')
                #self.SSID.append(ssid)
                self.credentials[ssid] = pwd

        for key in self.credentials.keys():
            self.SSID.append(key)
        pass        