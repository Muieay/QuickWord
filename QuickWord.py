import gc
from tkinter import Tk, Menu
from keyboard import add_hotkey, wait
from core import Layout
from core import QuickShow
from threading import Thread


def startTran():
    """
    翻译主窗口
    :return:
    """
    root = Tk()
    root.title("QuickWord")
    bc = Layout.BaiduConfig()
    menubar = Menu(root)
    menubar.add_cascade(label='配置', command=bc.showConfig)
    root.config(menu=menubar)
    root.geometry("300x120")
    Layout.Layout(root)
    root.mainloop()


def quickStart():
    """
    键盘事件
    ctrl + b 快速翻译
    shift + esc 退出快速翻译
    :return:
    """
    add_hotkey('ctrl+b', QuickShow.showTop)
    # keyboard.record(until='esc')
    wait('shift+esc')


if __name__ == '__main__':
    try:
        start_thread = Thread(target=startTran)
        quick_thread = Thread(target=quickStart)
        start_thread.start()
        quick_thread.start()
    except:
        del start_thread
        del quick_thread
        gc.collect()
