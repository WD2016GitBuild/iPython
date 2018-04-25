# pip install itchat

#coding=utf8
import itchat
import sys
from search import search
import win32api,win32con
import time

def alert(msg, title):
    win32api.MessageBox(0, msg, title, win32con.MB_OK) 


def handle(code,name,type,status):
    if status == '制作中':
        print('订单号：' + code + '，客户名称：' + name + '\r\n质检被打回...')
        alert('订单号：' + code + '\r\n客户名称：' + name + '\r\n质检被打回...','质检结果')
    elif status == '待发布':
        print('订单号：' + code + '\r\n客户名称：' + name + '\r\n质检通过了!')
        alert('订单号：' + code + '\r\n客户名称：' + name + '\r\n质检通过了!', '质检结果')

if len(sys.argv) == 1:
	print("参数输入错误！")
else:
	companyName = sys.argv[1]
	if len(sys.argv) == 3:
	    orderNum = sys.argv[2]
	else:
	    orderNum = ""
	search(companyName, orderNum, handle)
