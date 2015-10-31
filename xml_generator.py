class XML_Generator(object):
	def __init__(self, links):
		self.xml_sitemap = "<!-- Service provided by David Qian --> \n"
		self.xml_sitemap += '<?xml version="1.0" encoding="UTF-8"?> \n'
		self.xml_sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"> \n'
		for link in links:
			self.xml_sitemap += '\t<url>\n'
			self.xml_sitemap += '\t\t<loc>'+link+'</loc>\n'
			self.xml_sitemap += '\t</url>\n'
		self.xml_sitemap += '</urlset>'

	def generate_xml_sitemap_file(self):
		outputFile =  open('sitemap.xml', 'w')
		outputFile.write(self.xml_sitemap)
		outputFile.close()
	def generate_xml_sitemap_standard_output(self):
		print self.xml_sitemap



