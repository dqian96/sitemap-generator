from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import lxml

class Parser(object):
	def __init__(self, html, current_url, domain):
		self.soup = BeautifulSoup(html, "lxml")
		self.list_of_links = []
		self.domain = domain
		self.current_url = current_url

	def find_all_unique_links_in_html(self):
		for link in self.soup.find_all('a'):
			url = link.get('href')
			if (url == None):
				continue
			#relative url
			if url[0:4].lower() != "http":
				#relative from root
				if (url[0] == "/"):
					url = self.domain + url[1:]
				#relative from current url
				else:		    						
					#adding / for link depth
					if self.current_url[-1] != "/":
						self.current_url += "/"
					url = self.current_url + url

			#frame reference is unecessary
			if (url.find("/#") != -1):
				url = url[:url.find("/#")]


			if url[-1] == "/":
				temp_url = url[:-1]
			else:
				temp_url = url+"/"

			if not(url in self.list_of_links or temp_url in self.list_of_links ):
				if (url[:len(self.domain)] == self.domain):
					self.list_of_links.append(url)
		return self.list_of_links
