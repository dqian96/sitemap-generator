import link_parser
import urllib2
import xml_generator
#class for dfs of site
class Spider(object):
	def __init__(self):
		self.list_of_links = []

	#dfs of every link, adding to list_of_links
	def crawl_home_page(self, url, domain=""):	

		#domain/home address is the first inputting link
		if self.list_of_links == []:
			domain = url

		if domain[-1] != "/":
			domain += "/"

		#retrieve html at link
		try:
			response = urllib2.urlopen(url)
			html = response.read()
			self.list_of_links.append(url)
		#404 error
		except:
			return

		parser = link_parser.Parser(html, url, domain)
		links_in_url = parser.find_all_unique_links_in_html()

		#recursion for each unique link on html page
		for link in links_in_url:
			if link[-1] == "/":
				temp_link = link[:-1]
			else:
				temp_link = link+"/"
			if not(link in self.list_of_links or temp_link in self.list_of_links):
				self.crawl_home_page(link, domain) 

	#generate sitemap
	def generate_sitemap(self):
		xml = xml_generator.XML_Generator(self.list_of_links)
		xml.generate_xml_sitemap_file()
		xml.generate_xml_sitemap_standard_output()

#example usage
root_of_site_to_crawl = Spider();
root_of_site_to_crawl.crawl_home_page("https://www.student.cs.uwaterloo.ca/~se212/")
root_of_site_to_crawl.generate_sitemap()

