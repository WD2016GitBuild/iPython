# pip install itchat

#coding=utf8
import itchat
from search import search

itchat.auto_login(hotReload=True)  
#获取通讯录信息
account=itchat.get_friends()
print(account[0])
# #获取自己的UserName
userName = account[0]['UserName']
print(userName)

companyName = '成都龙源新材料科技有限公司'


def handle(code,name,type,status):
    if status == '制作中':
        itchat.send('订单号：' + code + '，客户名称：' + name + '，质检被打回...',toUserName=userName)
    elif status == '待发布':
        itchat.send('订单号：' + code + '，客户名称：' + name + '，质检通过了!',toUserName=userName)
        
search(companyName, handle)
