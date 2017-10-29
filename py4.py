# downloading .csv files form internet

from urllib import request

def download_page(url):
	response=request.urlopen(url)
	url_str= str(response.read())
	lines=url_str.split("\\n")
	dest_url=r'py4.txt'
	fx=open(dest_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()

download_page('https://finance.yahoo.com/quote/GOOG/key-statistics?p=GOOG.csv')
