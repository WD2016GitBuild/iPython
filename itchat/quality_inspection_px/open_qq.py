import os
import glob
import win32api

shortcuts = glob.glob("qq_links\*.lnk")

def open_sc(_name):
    for sc in shortcuts:
        print(isinstance(sc, str))
        print(sc)
        name = sc.split('\\')
        name = name[1].split(".")[0]
        if name == _name:
            win32api.ShellExecute(0,None,sc,None,None,True)
            break    
