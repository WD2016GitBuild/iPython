import requests
from bs4 import BeautifulSoup

'''
	公共方法
'''

request_type = "get"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'}
data = {}

def get_html(url, encoding='utf-8'):
	if request_type == "get":
		response = requests.get(url, headers=headers)
	else:
		response = requests.post(url, headers=headers)
	response.encoding = encoding
	return response.text


def download(src, name):
	r = requests.get(src, stream=True)
	f = open(name + '.jpg', 'wb')
	for chunk in r.iter_content(chunk_size=512):
		if chunk:
			f.write(chunk)


def get_soup(html_text):
	soup = BeautifulSoup(html_text, 'html.parser')
	return soup
