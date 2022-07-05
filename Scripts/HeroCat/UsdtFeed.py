import hashlib
import json
import requests
import socket
import socks
import time

socks.set_default_proxy(socks.SOCKS5, "43.128.19.77", 1081, username='1102s', password='1102s')
socket.socket = socks.socksocket


# class sessions(requests.Session):
#     def request(self, *args, **kwargs):
#         kwargs.setdefault('timeout', 10)
#         return super(sessions, self).request(*args, **kwargs)



session = requests.session()
# session = sessions()
tmp = []

def getlogindata(user, password):
    'MD5'
    signaturemd5 = hashlib.md5()
    signaturemd5.update(password.encode())
    pwd = signaturemd5.hexdigest()

    # url = 'https://mobile.herocat.io/vcbank-api/auth/login'
    url = 'https://www.herocat.io/vcbank-api/auth/login'
    headers = {
        # 'Connection' : 'close',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    data = {
        "email": user,
        "password": pwd,
        "actionToken": ""
    }
    res = session.post(url=url, headers=headers, data=json.dumps(data), timeout=30).json()
    # print(res)
    try:
        if res['code'] == 200:
            print(user + ':' + '登录状态：成功')
            re_data = {}
            re_data["login_uid"] = res['data']['uid']
            re_data["login_token"] = res['data']['token']
            # re_data['cookie'] = session.cookies.get_dict()
            # print(session.cookies.get_dict())
            return re_data
    except Exception as e:
        print('登录失败！', e)

def getInfo_Usdt(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/assets/accounts/info'
    headers = {
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        # 'origin': 'https://mobile.herocat.io',
        # 'pragma': 'no - cache',
        # 'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    res = session.post(url=url, headers=headers, json=data, verify=False, timeout=30).json()
    # print(res)
    # HCT = res['data'][5]['availableAmount']
    USDT = res['data'][8]['availableAmount']
    print('可用USDT余额：' + str(USDT))
    return int(USDT)

def feed(user, Usdt, lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/hero_cat/userfeedcat/feed'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'apitoken': lgdata['login_token'],
        'cache-control': 'no-cache',
        'content-length': '116',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.704469853.1636901408; _ga_23QMW81014=GS1.1.1636905494.21.1.1636905510.0',
        'language': 'en',
        'origin': 'https://mobile.herocat.io',
        'pragma': 'no-cache',
        'referer': 'https://mobile.herocat.io/myHPET',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': "Android",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid'],
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    if Usdt >= 1:
        data = {
            "catFoodId":1,
            "foodAmount":Usdt,
            "items":[
                {"amount":0,"currencyCode":"HCT"},
                {"amount":Usdt,"currencyCode":"USDT"}
            ]
        }
        res = session.post(url=url, headers=headers, data=json.dumps(data), verify=False, timeout=30)
        if res.status_code == 200:
            print(user + ': 喂养成功')

        else:
            print(user + ': 喂养失败')
            tmp.append(user + '喂养失败' + '\n')
            # print(tmp)
    else:
        print(user + ': 余额<1')
        tmp.append(user + '余额<1' + '\n')
        # print(tmp)

if __name__ == '__main__':
    # ip = input('请输入代理地址：')
    file = open("UsdtFeed_res.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        # count = len(fr.readlines())

        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = getlogindata(user, password)
            if data:
                Usdt = getInfo_Usdt(data)
                feed(user, Usdt, data)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
        time.sleep(5)
    with open("UsdtFeed_res.txt", 'a') as fw:
        for i in range(len(tmp)):
            fw.write(tmp[i])