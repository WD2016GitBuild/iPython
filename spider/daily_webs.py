import requests
from bs4 import BeautifulSoup

'''
	抓取dy2018最新电影
'''

request_type = "get"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'}
data = {}

def get_html(url):
	if request_type == "get":
		response = requests.get(url, headers=headers)
	else:
		response = requests.post(url, headers=headers)
	response.encoding = 'utf-8'
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


def get_dy2018():
	url = 'http://www.zcool.com.cn/discover/607!0!0!0!0!!!!-1!0!1'
	print('开始抓取zcool...')
	soup = get_soup(get_html(url))
	# print(soup.prettify())
	card_box = soup.select('.card-box')
	print("共搜索到" + str(len(card_box)) + "条记录")
	for i in range(10):
		card = card_box[i]
		card_img = card.select('.card-img')[0]
		card_a = card_img.select('a')[0]
		card_img = card_a.select('img')[0]
		card_a_href = card_a['href']
		card_img_src = card_img['src']
		print(card_a_href)
		print(card_img_src)
		print("")

def get_iiiimg():
	url = 'https://www.iiiimg.com/'
	print('开始抓取iiiimg...')
	soup = get_soup(get_html(url))
	# print(soup.prettify())
	card_box = soup.select('.picdiv')
	print("共搜索到" + str(len(card_box)) + "条记录")
	for i in range(10):
		card = card_box[i]
		card_img = card.select('.imgbox')[0]
		card_a = card_img.select('a')[0]
		card_img = card_a.select('img')[0]
		card_a_href = card_a['href']
		card_img_src = card_img['src']
		print(card_a_href)
		print(card_img_src)
		print("")

def get_68design():
	url = 'http://www.68design.net/work/?c=11&s=0&d=0&r=7&u=0&k=&g=&z='
	base_url = 'http://www.68design.net'
	print('开始抓取68design...')
	soup = get_soup(get_html(url))
	# print(soup.prettify())
	card_box = soup.select('.works-info ul li')
	print("共搜索到" + str(len(card_box)) + "条记录")
	for i in range(10):
		card = card_box[i]
		card_a = card.select('a')[0]
		card_img = card_a.select('img')[0]
		card_a_href = base_url + card_a['href']
		card_img_src = card_img['src']
		print(card_a_href)
		print(card_img_src)
		print("")

get_zcool()
get_iiiimg()
get_68design()
