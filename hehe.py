# coding: utf-8

"""  笑话接口 """

import requests
import json

class Hehe(object):
    key = '*********************' # 需要自己申请key (japi.juhe.cn)
    api = 'http://japi.juhe.cn/joke/content/text.from?key='+key+'&pagesize=1&page=2'

    @staticmethod
    def fetch(num):
        try:
            r = requests.get(Hehe.api + str(num))
            tmp_dict = json.loads(r.text)
            payload = tmp_dict['result']['data'][0]['content']
        except:
            payload = u'小笑话被北京的沙尘暴吹走了，再请求一次吧（来自花树的小提示）'
        return payload

if __name__ == '__main__':
    print Hehe.fetch(2)