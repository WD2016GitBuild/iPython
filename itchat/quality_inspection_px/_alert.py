from tkinter import *

def show_result(result):
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.title("质检结果")
    _width = len(result*12)
    _height = 200
    root.geometry(str(_width) + 'x' + str(_height))
    l = Label(root, text=result, font=("微软雅黑", 12), width=_width, height=_height)
    l.pack(side=LEFT)
    root.mainloop()