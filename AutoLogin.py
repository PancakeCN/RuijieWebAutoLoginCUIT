import requests
import time
import random
import urllib

header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '955',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 一定不要带Cookie，不然短时间重复访问会导致需要验证码
    # 'Cookie': '',
    'Host': '10.254.241.19',
    'Origin': 'http://10.254.241.19',
    # 从请求头中获取
    'Referer': '',
    # 一般无需修改
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

dataLogin = {
    # 填写post请求中的账号
    'userId': '',
    # 填写post请求中加密过的密码
    'password': '',
    # 选择网络接入方式，在post请求中有
    'service': '',
    # 从post请求中复制过来即可
    'queryString': '',
    # 不用填
    'operatorPwd': '',
    # 不用填
    'operatorUserId': '',
    # 不用填
    'validcode': '',
    # 不用修改
    'passwordEncrypt': 'true',
    # 填写post请求中的对应字段
    'userIndex': ''
}

dataCheck = {
    # 填写post请求中的对应字段，同上
    'userIndex': ''
}

# 登录地址
login = 'http://10.254.241.19/eportal/InterFace.do?method=login'
# 验证地址
checkStatus = 'http://10.254.241.19/eportal/InterFace.do?method=getOnlineUserInfo'

timeFormat = "%Y-%m-%d %H:%M:%S"


def work():
    res1 = requests.post(url=checkStatus, headers=header, data=dataCheck)
    res1.encoding = 'utf-8'
    content = str(res1.text.encode().decode(
        "unicode_escape").encode('raw_unicode_escape').decode())
    i = content.find('"result":"')
    # print(content)
    if content[i + 10:i + 14] == 'wait':
        print("\033[0;32;40m" + time.strftime(timeFormat, time.localtime()) + " [INFO] 账号" + dataLogin['userId'] + "当前处于在线状态。\033[0m")
    else:
        print("\033[0;33;40m" + time.strftime(timeFormat, time.localtime()) + " [WARN] 账号" + dataLogin['userId'] + "当前已经下线，正在尝试登录！\033[0m")
        res2 = requests.post(url=login, headers=header, data=dataLogin)
        res2.encoding = 'utf-8'
        content2 = str(res2.text.encode().decode(
            "unicode_escape").encode('raw_unicode_escape').decode())
        j = content2.find('"result":"')
        # print(content2)
        if content2[j + 10:j + 17] == 'success':
            print("\033[0;32;40m" + time.strftime(timeFormat, time.localtime()) + " [INFO] 账号" + dataLogin['userId'] + "登录成功！接入方式：" + urllib.parse.unquote(dataLogin['service']) + "\033[0m")


while (True):
    try:
        work()
    except:
        print("\033[0;31;40m" + time.strftime(timeFormat, time.localtime()), " [ERROR] 监测出错，请检查网络是否连通。\033[0m")
        time.sleep(1)
        continue
    # 这里间隔20~40秒查询一次状态，切莫太频繁
    time.sleep(random.randint(20, 40))