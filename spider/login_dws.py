import requests
from bs4 import BeautifulSoup
from common import get_html, download, get_soup
import urllib

'''
	每天抓取站酷前20条网页资讯
'''

request_type = "post"
base_url = 'http://dws.300.cn'
login_url = 'http://dws.300.cn/security/doLogin'
search_url = 'http://dws.300.cn/order/orderSearch'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
           'Referer': 'http://dws.300.cn/security/login'}
headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
           'Referer': 'http://dws.300.cn/userManage/toMain'}
data = {'loginName': 'cdwudong@300.cn',
        'password': '4da7629abc2a7610b35684b3eb96fa73'}
data2 = {'companyName': '成都秋叶原商贸有限公司', 'domain': '', 'bossOrderList': '', 'contractCode': '', 'productIds': '', 'addTimeStartStr': '', 'addTimeEndStr': '',
         'onlineStartTimeStr': '', 'onlineEndTimeStr': '', 'productInstCode': '', 'hqId': '', 'areaId': '', 'subId': '', 'empId': '', 'orderStatuss': '', 'businessTypes': ''}
print(data2)
v2ex_session = requests.Session()
v2ex_session.post(login_url, data=data, headers=headers)

f = v2ex_session.post(search_url,headers=headers, data=data2)
soup = BeautifulSoup(f.content,"html.parser")
list = soup.select('.middle-align tr')
def create_full_string(s):
	num = len(s)
	total = 20
	for x in range(total-num):
		s = s + '  '
	return s

for l in list:
	td = l.select('td')
	code = td[2].string #合同号
	name = td[3].string #客户名称
	type = td[5].string #产品名称
	status = td[7].string #订单状态
	print(create_full_string(name) + ' ' + create_full_string(type) + ' ' + create_full_string(status))
	print('')
	