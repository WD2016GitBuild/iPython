import requests
from bs4 import BeautifulSoup
from common import get_html, download, get_soup

'''
	每天抓取站酷前20条网页资讯
'''

request_type = "get"
base_url = 'https://www.dy2018.com'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'}
data = {}

def get_dy2018():
	url = 'https://www.dy2018.com/'
	print('开始抓取dy2018...')
	soup = get_soup(get_html(url, 'gb2312'))
	# print(soup.prettify())
	list = soup.select('.co_content222 li')
	print("共搜索到" + str(len(list)) + "条记录")
	for i in list:
		one = i
		a = one.select('a')[0]
		a_href = a['href']
		a_title = a['title']
		print(base_url + a_href)
		print(a_title)
		print("")

get_dy2018()
