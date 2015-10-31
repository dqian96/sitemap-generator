import web_crawler

#main program
print
print "Hey! Welcome to Web Crawler/Sitemap Generator by David Qian."
print "This product is licensed under the MIT license."
print "No warranty is provided of any kind nor gurantee of proper function."
print "Please use this product for non-evil purposes."
print "Some sites will deny to be crawled because of their robots.txt document. Please respect their wishes!"
print

root_URL = raw_input("Enter the EXACT, ROOT URL of the site you wish to crawl (0 to exit): ")
while (root_URL != "0"):
	print
	crawler = web_crawler.Spider();
	crawler.crawl_home_page(root_URL)
	crawler.generate_sitemap()
	print
	root_URL = raw_input("Enter the EXACT, ROOT URL of the site you wish to crawl (0 to exit): ")


