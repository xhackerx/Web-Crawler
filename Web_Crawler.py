import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	url='http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_4/page+' + str(page)
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findall('a',{'class':'item.name}):
		href='http://www.imdb.com" + link.get('href')
		title=link.string
		print(href)
		print(title)
		get_single_item_date(href)
	page+=1

def get_single_item_date(item_url):
	source_code=requests.get(item_url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for item_name in soup.findAll('div',{'class':'i-name'}):
		print(item_name.string)
	for link in soup.findall('a')
		href="http://www.imdb.com" + link.get('href)
		print(href)
trade_spider(3)
