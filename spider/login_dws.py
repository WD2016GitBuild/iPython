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
search_data = {'domain': '', 'bossOrderList': '', 'contractCode': '', 'productIds': '', 'addTimeStartStr': '', 'addTimeEndStr': '',
               'onlineStartTimeStr': '', 'onlineEndTimeStr': '', 'productInstCode': '', 'hqId': '', 'areaId': '', 'subId': '', 'empId': '', 'orderStatuss': '', 'businessTypes': ''}

status = ('设计中', '制作中', '质检待领取', '质检中', '待发布')

session = requests.Session()
def login():
    session.post(login_url, data=login_data, headers=login_header)

login()

def search(companyName, callback):
    search_data['companyName'] = companyName;
    f = session.post(search_url, headers=search_header, data=search_data)
    soup = BeautifulSoup(f.content, "html.parser")
    list = soup.select('.middle-align tr')

    for l in list:
        td = l.select('td')
        code = td[2].string  # 合同号
        name = td[3].string  # 客户名称
        type = td[5].string  # 产品名称
        status = td[7].string  # 订单状态
        print(code + '  ' + name + ' ' + type + ' ' + status)
        if(status == '待发布'):
            callback(code, name, type, status)


if __name__ == '__main__':
    search('成都秋叶原商贸有限公司')