import uasyncio as asyncio
import ure as re


class voltageWriter:
	
	def __init__(self):
		self.addr = ('192.168.4.1', 8080)
	

	def ure_text(self, html):
		p = re.compile(r'<h3>(.*)</h3>')

		##p = re.compile(r'<\/?!?(h3)[^>]*>')

		#p = p.search(html)
		#html = p.group(0)

		#print(str(html))
		

		#p = re.compile(r'<.*?>')

		p = p.search(html)
		p = p.group(1)
		return p
		#return p

	def __await__(self, html):
		print("voltage writer")
		text = self.ure_text(html)
		print(str(text))
		return text

		


	__iter__ = __await__ 