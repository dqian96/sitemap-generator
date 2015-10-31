import link_parser
import urllib2
import sitemap_xml_generator
import hashlib
#class for dfs of site
class Spider(object):
	def __init__(self):
		#final set of links to output
		self.list_of_links = []
		self.not_found = False;
		#hashtable for all considered links, 0-1000 possible indices
		#future implementation to adjust size of table for estimated number of links expected
		self.table_of_links = [[]*1]*1001
	#dfs of every link, adding to list_of_links
	def crawl_home_page(self, url, domain=""):	
		print "Crawling: "+url
		#domain/home address is the first inputting link
		if self.list_of_links == []:
			domain = url
			last_slash = domain.rfind("/")
			if not(last_slash == 6 or last_slash == 7):
				last_period = domain.rfind(".")

				if last_slash < last_period:
					domain = domain[:last_slash]

			if domain[-1] != "/":
				domain += "/"
		#retrieve html at link
		try:
			response = urllib2.urlopen(url)
			html = response.read()
			self.list_of_links.append(url)
			#md5 hash or url, and then reducing it to the appropriate range
			hash_url = int(hashlib.md5(url).hexdigest(), 16)
			while (hash_url > 1000):
				hash_url = hash_url / 1000
			self.table_of_links[hash_url].append(url)
		#404 error
		except:
			self.not_found = True
			return

		parser = link_parser.Parser(html, url, domain)
		links_in_url = parser.find_all_unique_links_in_html()

		#recursion for each unique link on html page
		for link in links_in_url:
			if link[-1] == "/":
				temp_link = link[:-1]
			else:
				temp_link = link+"/"

			#hashes for links on page
			hash_link = int(hashlib.md5(link).hexdigest(), 16)
			hash_temp_link =  int(hashlib.md5(temp_link).hexdigest(), 16)

			while (hash_link > 1000):
				hash_link = hash_link / 1000
			while (hash_temp_link > 1000):
				hash_temp_link = hash_temp_link / 1000	
			#if unique links
			if not(link in self.table_of_links[hash_link] or temp_link in self.table_of_links[hash_temp_link]):
				self.crawl_home_page(link, domain) 

	#generate sitemap
	def generate_sitemap(self):
		xml = sitemap_xml_generator.XML_Generator(self.list_of_links)
		xml.generate_xml_sitemap_file()
		print 
		xml.generate_xml_sitemap_standard_output()
		print
		if (self.not_found):
			print "Errors were found on this site. They are not included in the sitemap."
		print "A list of "+str(len(self.list_of_links))+" url(s) were generated."

#example usage
#root_of_site_to_crawl = Spider();
#root_of_site_to_crawl.crawl_home_page("http://wordchoice.ca/")
#root_of_site_to_crawl.generate_sitemap()


##################################################################################
#previous code
'''
import link_parser
import urllib2
import sitemap_xml_generator
#class for dfs of site
class Spider(object):
	def __init__(self):
		self.list_of_links = []
		self.not_found = False;
	#dfs of every link, adding to list_of_links
	def crawl_home_page(self, url, domain=""):	
		print "Crawling: "+url
		#domain/home address is the first inputting link
		if self.list_of_links == []:
			domain = url
			last_slash = domain.rfind("/")
			if not(last_slash == 6 or last_slash == 7):
				last_period = domain.rfind(".")

				if last_slash < last_period:
					domain = domain[:last_slash]
	
			if domain[-1] != "/":
				domain += "/"
		#retrieve html at link
		try:
			response = urllib2.urlopen(url)
			html = response.read()
			self.list_of_links.append(url)
		#404 error
		except:
			self.not_found = True
			return

		parser = link_parser.Parser(html, url, domain)
		links_in_url = parser.find_all_unique_links_in_html()

		#recursion for each unique link on html page
		for link in links_in_url:
			if link[-1] == "/":
				temp_link = link[:-1]
			else:
				temp_link = link+"/"

			#hashing
			
			if not(link in self.list_of_links or temp_link in self.list_of_links):
				self.crawl_home_page(link, domain) 

	#generate sitemap
	def generate_sitemap(self):
		xml = sitemap_xml_generator.XML_Generator(self.list_of_links)
		xml.generate_xml_sitemap_file()
		print 
		xml.generate_xml_sitemap_standard_output()
		print
		if (self.not_found):
			print "Errors were found on this site. They are not included in the sitemap."
		print "A list of "+str(len(self.list_of_links))+" url(s) were generated."

#example usage
#root_of_site_to_crawl = Spider();
#root_of_site_to_crawl.crawl_home_page("http://wordchoice.ca/")
#root_of_site_to_crawl.generate_sitemap()
'''