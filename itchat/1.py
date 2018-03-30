# pip install itchat

#coding=utf8
import itchat

itchat.auto_login(hotReload=True)  
#获取通讯录信息
account=itchat.get_friends()
print(account[0])
# #获取自己的UserName
userName = account[0]['UserName']
print(userName)
#获取公众号信息
# mps = itchat.get_mps()
# print(mps)
lines = []
#读取txt文件

#循环发送文本内容
for i in range(2): 
    #UserName需要用上面获取的自己修改
    itchat.send("abc",toUserName=userName)  
print("Success")

