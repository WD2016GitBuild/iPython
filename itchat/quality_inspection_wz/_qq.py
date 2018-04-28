import win32gui
import win32con
import win32clipboard as w
import time
from open_qq import open_sc

def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def main():
    qqs = []
    qqs.append(['王園紅','嘉兴|王园红 159-5738-2291'])
    # qqs.append(['赵浩宇', '赵浩宇-65028581'])
    qqs.append(['何安东', '浦西|何安东'])

    for qq in qqs:
        print(qq[0])
        open_sc(qq[0])
        time.sleep(0.5)
        send_qq(qq[1], "测试")

def _MyCallback(hwnd, extra):  
    windows = extra  
    temp=[]  
    temp.append(hex(hwnd))  
    temp.append(win32gui.GetClassName(hwnd))  
    temp.append(win32gui.GetWindowText(hwnd))  
    windows[hwnd] = temp  
    
def TestEnumWindows():  
    windows = {}  
    win32gui.EnumWindows(_MyCallback, windows)  
    print("Enumerated a total of  windows with %d classes" ,(len(windows)))
    print('------------------------------')
    #print classes  
    print('-------------------------------')
    for item in windows :  
        print(windows[item])

if __name__ == '__main__':
    # main()
    # print("Enumerating all windows...")
    # h=win32gui.FindWindow(None,'qq')  
    # print(hex(h))
    # TestEnumWindows()  
    # print("All tests done!")

    # qq = win32gui.FindWindow(None, "QQWifiQQPluginMsgWnd")
    # # 投递剪贴板消息到QQ窗体
    # win32gui.SendMessage(qq, 258, 22, 2080193)
    # win32gui.SendMessage(qq, 770, 0, 0)
    # # 模拟按下回车键
    # win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    # win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    # main()

    send_qq('温州|李莉莉', "abc")



# a()