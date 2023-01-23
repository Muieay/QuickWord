from tkinter import Tk, Label, Button, Entry, END, Toplevel, Menu
import json
from core import Translation as tr

a = tr.Translation()


class Layout:

    def __init__(self, root):
        Label(root, text="请输入翻译内容：").grid(row=0)
        Label(root, text="翻译结果：").grid(row=1)
        self.e1 = Entry(root)
        self.e2 = Entry(root)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)
        self.bt1 = Button(root, text="翻译", width=10, command=self.tran)
        self.bt2 = Button(root, text="清空", width=10, command=self.clear)
        self.bt1.place(x=50, y=70)
        self.bt2.place(x=150, y=70)

    # 清理信息框
    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    # 展示翻译结果
    def tran(self):
        self.e2.delete(0, END)
        word = self.e1.get()
        try:
            val = a.tran(word)['trans_result'][0]['dst']
        except KeyError:
            val = "百度翻译配置错误！"
        self.e2.insert(0, val)


# 百度翻译配置
class BaiduConfig:
    def __init__(self):
        self.configData = None
        self.bt1 = None
        self.e2 = None
        self.e1 = None
        self.top = None

    # 配置设置
    def showConfig(self):
        self.top = Toplevel()
        self.top.title('配置')
        self.top.attributes('-topmost', True)
        Label(self.top, text="appid:").grid(row=0)
        Label(self.top, text="key:：").grid(row=1)
        self.e1 = Entry(self.top)
        self.e2 = Entry(self.top)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)
        self.top.geometry("210x100")
        self.bt1 = Button(self.top, text="确定", width=10, command=self.createapi)
        self.bt1.place(x=70, y=65)

    def createapi(self):
        with open("api.json", "w", encoding="UTF-8") as file:
            if self.e1.get() != '' and self.e2.get() != '':
                self.configData = {
                    "appid": self.e1.get(),
                    "key": self.e2.get(),
                }
                self.configData = json.dumps(self.configData)
                file.write(self.configData)
            self.top.destroy()


if __name__ == '__main__':
    b = BaiduConfig()

    root1 = Tk()

    menubar = Menu(root1)
    menubar.add_cascade(label='配置', command=b.showConfig)
    root1.config(menu=menubar)

    root1.geometry("300x120")
    app = Layout(root1)
    root1.mainloop()
