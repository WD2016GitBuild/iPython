# pip install itchat

#coding=utf8
import itchat
import sys
from search import search
import win32api,win32con
import time
from _alert import show_result
from _qq import setText
from _qq import send_qq

def handle(code,name,type,status):
    if status == '制作中':
        result = '订单号:' + code + '\r\n客户名称:' + name + '\r\n质检被打回...'
        print(result)
        show_result(result)
        setText(result)
        send_qq('温州|李莉莉', result)
    elif status == '待发布':
        result = '订单号:' + code + '\r\n客户名称:' + name + '\r\n质检通过了!'
        print(result)
        show_result(result)
        setText(result)
        send_qq('温州|李莉莉', result)

if len(sys.argv) == 1:
	print("参数输入错误！")
else:
	companyName = sys.argv[1]
	if len(sys.argv) == 3:
	    orderNum = sys.argv[2]
	else:
	    orderNum = ""
	search(companyName, orderNum, handle)

