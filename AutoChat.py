import itchat
from itchat.content import TEXT
import urllib.request,urllib.parse
import json

TulingUrl = "http://www.tuling123.com/openapi/api"##请求地址
TulingApiKey = "43b6758215124481aba6299578d1b89a"##图灵机器人的apikey
global status
status = 1##默认为开启模式
@itchat.msg_register(TEXT)
def simple_reply(msg):
    global status
    if(msg['ToUserName'] == "filehelper"):
        if msg["Content"] == "关闭":
            status = 0
            itchat.send("聊天机器人以关闭", 'filehelper')
        else:
            status = 1
            itchat.send("聊天机器人以开启", 'filehelper')
    if status == 1:
        print(msg["Content"])
        values = {'key': TulingApiKey, "info":msg["Content"]}
        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(TulingUrl + '?' + data)
        response = urllib.request.urlopen(req)
        the_page = response.read().decode('UTF8')
        data = json.loads(the_page)
        if data["code"] > 99999:
            print("回复成功")
            return data["text"]+"【机器自动回复】"
        else:
            return "机器人出错主人正在修复[捂脸]"
itchat.auto_login(hotReload=True)
itchat.run()


