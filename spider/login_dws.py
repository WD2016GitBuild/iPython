import requests
from bs4 import BeautifulSoup

login_url = 'http://dws.300.cn/security/doLogin'
search_url = 'http://dws.300.cn/order/orderSearch'

login_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
                'Referer': 'http://dws.300.cn/security/login'}
search_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
                 'Referer': 'http://dws.300.cn/userManage/toMain'}
login_data = {'loginName': 'cdwudong@300.cn',
              'password': '4da7629abc2a7610b35684b3eb96fa73'}
search_data = {'companyName': '成都秋叶原商贸有限公司', 'domain': '', 'bossOrderList': '', 'contractCode': '', 'productIds': '', 'addTimeStartStr': '', 'addTimeEndStr': '',
               'onlineStartTimeStr': '', 'onlineEndTimeStr': '', 'productInstCode': '', 'hqId': '', 'areaId': '', 'subId': '', 'empId': '', 'orderStatuss': '', 'businessTypes': ''}

session = requests.Session()
session.post(login_url, data=login_data, headers=login_header)

f = session.post(search_url, headers=search_header, data=search_data)
soup = BeautifulSoup(f.content, "html.parser")
list = soup.select('.middle-align tr')

def create_full_string(s):
    num = len(s)
    # print(s)
    total = 25
    for x in range(total-num):
        s = s + '  '
    return s

# print(create_full_string('合同号') + '  ' + create_full_string('客户名称') + ' ' +
        #   create_full_string('产品名称') + ' ' + create_full_string('订单状态'))

for l in list:
    td = l.select('td')
    code = td[2].string  # 合同号
    name = td[3].string  # 客户名称
    type = td[5].string  # 产品名称
    status = td[7].string  # 订单状态
    print(create_full_string(code) + '  ' + create_full_string(name) + ' ' +
          create_full_string(type) + ' ' + create_full_string(status))
    print('')
