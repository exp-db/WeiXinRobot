# coding: utf-8
import itchat
import requests


from hehe import Hehe

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    global num
    payload = Hehe.fetch(num)
    num += 1
    return payload

if __name__ == '__main__':


    # 笑话编号
    num = 1

    itchat.auto_login(enableCmdQR=-1)
    itchat.run()