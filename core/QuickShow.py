from pyperclip import paste
from tkinter import Tk, Label
from core import Translation as tr

a = tr.Translation()


def showTop():
    top = Tk()
    top.title('翻译')
    top.geometry("150x80")
    top.attributes('-topmost', True)
    p = paste()
    try:
        res = a.tran(p)['trans_result'][0]['dst']
    except KeyError:
        res = "百度翻译配置错误！"
    Label(top, text=res).pack(expand=True)
    top.mainloop()


if __name__ == '__main__':
    showTop()
