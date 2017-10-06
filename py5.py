# making web crawler

import requests
from bs4 import BeautifulSoup   #Beautiful Soup is a Python library for pulling data out of HTML and XML files

def web_crawler(max_pages):
	page=1
	title="abc"
	while page<= max_pages:
		url='http://www.biographyonline.net/people/famous-100.html' + str(page)
		source_code= requests.get(url)
		data=source_code.text
		soup=BeautifulSoup(data,'html.parser')
		
		div=soup.find('ul',{'class':'sub-menu'})
		sub_div=div.find_all('a')
		for link in sub_div:
			href=link.get('href')
			title= link.string
			if "http://www.biographyonline.net" not in href:
				href="http://www.biographyonline.net/writers.html"   #since link to this title is prsnt wrong on this pg inspect
			print(title)
			print(href)
			details_of_every_page(href)
		page = page+1

def details_of_every_page(url):
		source_code= requests.get(url)
	        data=source_code.text
        	soup=BeautifulSoup(data,'html.parser')
		div=soup.find('li',{'id':'menu-item-10536'})
		sub_div= div.find_all('a')
		for link in sub_div:
			title2 = link.string
			print(title2)


web_crawler(1)

