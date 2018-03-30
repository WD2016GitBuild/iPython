#coding=utf8
import datetime  
import time
  
def doSth():  
    print("acb")

# 一般网站都是1:00点更新数据，所以每天凌晨一点启动  
def main(h=1,m=0): 
    while True:  
        now = datetime.datetime.now()
        print(now.hour)
        print(now.minute)
        # print(now.hour, now.minute)  
        if now.hour == h and now.minute == m:  
            doSth()
        # 每隔60秒检测一次  
        time.sleep(60)
  
if __name__ == "__main__":
    main()