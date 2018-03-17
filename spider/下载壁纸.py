import requests
from bs4 import BeautifulSoup 

def get_html(url, headers):
	response = requests.post(url, headers=headers)
	response.encoding = 'utf-8'
	return response.text

url = 'http://desk.zol.com.cn/bizhi/7257_89799_2.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36'}
data = {'loginName':'cdwudong@300.cn', 'password':'4da7629abc2a7610b35684b3eb96fa73'}

def download(src, name):
	r = requests.get(src, stream=True)
	f = open(name + '.jpg', 'wb')
	for chunk in r.iter_content(chunk_size=512):
		if chunk:
			f.write(chunk)

soup = BeautifulSoup(get_html(url, headers), 'html.parser')
a = soup.select('.photo-list-box li a')
print("共查找到" + str(len(a)) + "图片")
for x in a:
	soup = BeautifulSoup(get_html("http://desk.zol.com.cn" + x['href'], headers), 'html.parser')
	img = soup.select("#bigImg")
	src = img[0]['src'];
	print(src)
	download(src, src[-12:])
	
print(str(len(a)) + "张图片已经全部下载完成~~")