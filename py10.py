import requests
from bs4 import BeautifulSoup
import operator

def start(url):
	word_list=[]
	source_code=requests.get(url).text
	soup= BeautifulSoup(source_code,'html.parser')
	for post_text in soup.find('ul',{'class':'sub-menu'}):
		content = post_text.string
		words = content.lower().split()
		for each_word in words:
			print(each_word)
			word_list.append(each_word)
			clean_up_list(word_list)


def clean_up_list(word_list):    # this function is to clean the symbols like ,.@#%&*, etc from the words
	clean_word_list=[]
	for word in word_list:
		symbols="!~`@#$%^&*()_-+=[]{}\|{[:;'<>?/.,\""
		for i in range(0, len(symbols)):
			word=word.replace(symbols[i],"")
		if len(word)>0:
			clean_word_list.append(word)
	create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):  # to count the number of times a particular word occurs in the page
	word_count= {}
	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word]=1
	for key, value in sorted(word_count.items(), key=operator.itemgetter(0)): # itemgetter(0) means it is sorting by alphabetic order and itemgetter(1) means it is sorting by number of occurences in ascending order.
		print(key, value)

start('http://www.biographyonline.net/people/famous-100.html')

