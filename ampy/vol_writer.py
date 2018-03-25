import uasyncio as asyncio
import ure as re


class voltageWriter:
	
	def __init__(self):
		self.voltages = {}
	

	def ure_text(self, html):
		try:
			p = re.compile(r'<h3>(.*)</h3>')
			p = p.search(html)
			html_str = p.group(0)
			html_str = html_str.replace('<h3>', ':')
			html_str = html_str.replace('</h3>', ':')
			#print(html_str)
			html_list = html_str.split(':')
			#print(html_list)
			#print(type(html_list))
			for line in html_list:
				if "=" in line:
					ssid, voltage = line.strip().split('=')
					self.voltages[ssid] = voltage

			print(self.voltages)
			#print(type(self.voltages))
			#line = html.split('\n')
			return self.voltages
			#return p
		except:
			return None

	def __await__(self, html):
		#print("voltage writer")
		if html is not None:
			self.voltages = self.ure_text(html)
			#print(str(text))
			#text = text.split('=')
			#print(str(text[1]))
		return self.voltages

		


	__iter__ = __await__ 