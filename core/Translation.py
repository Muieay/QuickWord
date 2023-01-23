import random
from urllib import request
from urllib import parse
import hashlib
import json


# 获取配置
def readConfig():
    """
    获取api接口信息
    :return:
    """
    try:
        with open("api.json", "r", encoding="UTF-8") as file:
            baiduConfig = file.read()
            return json.loads(baiduConfig)
    except FileNotFoundError:
        with open("api.json", "w", encoding="UTF-8") as file:
            configData = {
                "appid": '',
                "key": ''
            }
            configData = json.dumps(configData)
            file.write(configData)
        return None


# 翻译
class Translation:
    lan1 = 'en'
    lan2 = 'zh'

    def __init__(self):
        self.__word = None
        if readConfig() is not None:
            self.__appid = readConfig()['appid']
            self.__key = readConfig()['key']

    def tran(self, world='hello'):
        try:
            self.__word = world
            self.checkLan()
            url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
            f_data = {
                "from": self.lan1,
                "to": self.lan2,
                "appid": self.__appid,
                "key": self.__key,
                "q": self.__word,
                "salt": str(random.randint(99999, 99999999))
            }
            m = f_data['appid'] + f_data['q'] + f_data['salt'] + f_data['key']
            sign = hashlib.md5(m.encode('UTF-8'))
            f_data['sign'] = sign.hexdigest()
            data = parse.urlencode(f_data).encode('UTF-8')
            rep = request.urlopen(url, data)
            # print(rep)
            html = rep.read().decode('UTF-8')
            tr = json.loads(html)
            return tr
        except AttributeError:
            pass

    def checkLan(self):
        if '\u4e00' <= self.__word <= '\u9fff':
            self.lan1 = 'zh'
            self.lan2 = 'en'
        else:
            self.lan1 = 'en'
            self.lan2 = 'zh'


if __name__ == '__main__':
    w = input('请输入:')
    a = Translation()
    print(a.tran(w))
