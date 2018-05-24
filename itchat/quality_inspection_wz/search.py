import requests
from bs4 import BeautifulSoup
import datetime
import sys
import time

sys.setrecursionlimit(1000000)

login_url = 'http://dws.300.cn/security/doLogin'
search_url = 'http://dws.300.cn/order/orderSearch'

login_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
                'Referer': 'http://dws.300.cn/security/login'}
search_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3343.4 Safari/537.36',
                 'Referer': 'http://dws.300.cn/userManage/toMain'}
login_data = {'loginName': 'wzfuxiaoping@300.cn',
              'password': 'f057a419496bda4bdad4862a4b6173b9'}
search_data = {'domain': '', 'bossOrderList': '', 'contractCode': '', 'productIds': '', 'addTimeStartStr': '', 'addTimeEndStr': '',
               'onlineStartTimeStr': '', 'onlineEndTimeStr': '', 'productInstCode': '', 'hqId': '', 'areaId': '', 'subId': '', 'empId': '', 'orderStatuss': '', 'businessTypes': ''}

status = ('设计中', '制作中', '质检待领取', '质检中', '待发布')

session = requests.Session()
def login():
    session.post(login_url, data=login_data, headers=login_header)

login()
search_end = False
currentStatus = ""

def search(companyName, orderNum, callback):
    global search_end
    global currentStatus
    search_data['companyName'] = companyName;
    f = session.post(search_url, headers=search_header, data=search_data)
    soup = BeautifulSoup(f.content, "html.parser")
    list = soup.select('.middle-align tr')
    num = 0
    for l in list:
        td = l.select('td')
        code = td[2].string  # 合同号
        if orderNum != "":
            if code != orderNum:
                continue
        name = td[3].string  # 客户名称
        type = td[5].string  # 产品名称
        yw = td[6].string # 业务类型
        status = td[7].string  # 订单状态
        # print(type)
        if yw == '另购':
            continue
        if currentStatus != status and status != '制作中':
        	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + code + ' ' + name + ' ' + type + ' ' + status)
        	currentStatus = status
        if status == '质检中' or status == '质检待领取':
            # print(code + ' ' + name + ' ' + type + ' ' + status)
            # print('.', sep=' ', end=" ", file=sys.stdout, flush=True)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + name + ' ' + status)
            num = num + 1
        if status == '待发布' or status == '制作中':
            search_end = True
            callback(code, name, type, status)
    if not search_end and num > 0:
        time.sleep(60)
        search(companyName, orderNum, callback)
    else:
        print('没有质检的订单')


if __name__ == '__main__':
    def p(code, name, type, status):
        print(code + '  ' + name + ' ' + type + ' ' + status)
    search('成都秋叶原商贸有限公司',p)