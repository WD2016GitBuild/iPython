import requests
from bs4 import BeautifulSoup
from common import get_html, download, get_soup

'''
	抓取AI音箱
	是否有货源
'''

request_type = "get"
base_url = 'https://item.mi.com'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'}
data = {}

def get_dy2018():
	url = 'https://item.mi.com/product/6334.html'
	print('开始抓取AI音箱...')
	soup = get_soup(get_html(url, 'utf-8'))
	# print(soup.prettify())
	a = soup.select('#J_buyBtnBox a')
	print(a)

# get_dy2018()

import threading
import time

def hello(name):
	print("hello %s\n" % name)
	global timer
	timer = threading.Timer(2.0, hello, ["Hawk"])
	timer.start()

if __name__ == "__main__":
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()