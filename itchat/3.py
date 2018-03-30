# pip install itchat

#coding=utf8
import itchat
import sys
from search import search

itchat.auto_login(hotReload=True)  
#获取通讯录信息
account=itchat.get_friends()
# print(account[0])
# #获取自己的UserName
mySelf = account[0]['UserName']
# print(userName)
# Design群
rooms = itchat.get_chatrooms(update=True)
# rooms = itchat.search_chatrooms('Design')[0]['UserName']
rooms = itchat.search_chatrooms('Design')[0]['UserName']

companyName = sys.argv[1]
toWho = sys.argv[2]

def listCount(name):
    account = itchat.get_friends()
    for x in account:
        # print(x['NickName'])
        # print(x['RemarkName'])
        if(x['RemarkName'] == name):
            return x['UserName']
            break

def listRoom():
    rooms = itchat.get_chatrooms(update=True)
    rooms = itchat.search_chatrooms('幸福一家人')
    print(len(rooms))
    for x in rooms:
        print(x['NickName'])

print(companyName)
print('开始质检...')
print('质检结果后将结果发送给微信-' + toWho)
room = listCount(toWho)
print('查找到UserName：' + room)

def handle(code,name,type,status):
    if status == '制作中':
        print('订单号：' + code + '，客户名称：' + name + '，质检被打回...')
        itchat.send('订单号：' + code + '，客户名称：' + name + '，质检被打回...',toUserName=mySelf)
        itchat.send('订单号：' + code + '，客户名称：' + name + '，质检被打回...',toUserName=rooms)
    elif status == '待发布':
        print('订单号：' + code + '，客户名称：' + name + '，质检通过了!')
        itchat.send('订单号：' + code + '，客户名称：' + name + '，质检通过了!',toUserName=mySelf)
        itchat.send('订单号：' + code + '，客户名称：' + name + '，质检通过了!',toUserName=rooms)
        
search(companyName, handle)
# itchat.send('哈哈',toUserName=rooms)




def main():
    listRoom()
    listCount()


if __name__ == '__main__':
	# main()
	pass