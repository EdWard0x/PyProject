import hashlib
import json
import requests
import socket
import socks
import time

socks.set_default_proxy(socks.SOCKS5, "43.128.19.77", 1081, username='1102s', password='1102s')
socket.socket = socks.socksocket


session = requests.session()
power_dayHct = []


def getlogindata(user, password, ip):
    'MD5'
    signaturemd5 = hashlib.md5()
    signaturemd5.update(password.encode())
    pwd = signaturemd5.hexdigest()

    url = 'https://mobile.herocat.io/vcbank-api/auth/login'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "email": user,
        "password": pwd,
        "actionToken": ""
    }
    # proxies = {
    #     'http': '185.200.36.86:8080',
    #     'https': '185.200.36.86:8080'
    # }
    proxies = {
        'http': ip,
        'https': ip
    }
    try:
        res = session.post(url=url, headers=headers, proxies=proxies, data=json.dumps(data), verify=False).json()
        try:
            if res['code'] == 200:
                # print(user + ':' + '登录状态：成功')
                re_data = {}
                re_data["login_uid"] = res['data']['uid']
                re_data["login_token"] = res['data']['token']
                # re_data['cookie'] = session.cookies.get_dict()
                # print(session.cookies.get_dict())
                return re_data
        except Exception as e:
            print('登录失败！', e)
    except requests.exceptions.ConnectionError as e:
        print('代理不可用:', e.args)
        getlogindata(user, password, ip)
def getlogindata(user, password):
    'MD5'
    signaturemd5 = hashlib.md5()
    signaturemd5.update(password.encode())
    pwd = signaturemd5.hexdigest()

    url = 'https://mobile.herocat.io/vcbank-api/auth/login'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    data = {
        "email": user,
        "password": pwd,
        "actionToken": ""
    }
    res = session.post(url=url, headers=headers, data=json.dumps(data)).json()
    # print(res)
    try:
        if res['code'] == 200:
            # print(user + ':' + '登录状态：成功')
            re_data = {}
            re_data["login_uid"] = res['data']['uid']
            re_data["login_token"] = res['data']['token']
            # re_data['cookie'] = session.cookies.get_dict()
            # print(session.cookies.get_dict())
            return re_data
    except Exception as e:
        print('登录失败！', e)

def getpower_dayHct(lgdata, ip):
    url = 'https://mobile.herocat.io/vcbank-api/hero_cat/userherocat/get'
    headers = {
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        # 'origin': 'https://mobile.herocat.io',
        # 'pragma': 'no - cache',
        # 'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    proxies = {
        'http': ip,
        'https': ip
        # 'http': '185.200.36.86:8080',
        # 'https': '185.200.36.86:8080'
    }
    try:
        res = session.post(url=url, headers=headers, json=data, proxies=proxies, verify=False).json()
        powerAmount = res['data']['powerAmount']
        myDayDCatAmount = res['data']['myDayDCatAmount']
        power_dayHct.append(user + 'pet算力：' + str(powerAmount) + '\t' + '今日产出：' + str(myDayDCatAmount) + '\n')
    except requests.exceptions.ConnectionError as e:
        print('代理不可用:', e.args)
        getpower_dayHct(lgdata, ip)
def getpower_dayHct(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/hero_cat/userherocat/get'
    headers = {
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        # 'origin': 'https://mobile.herocat.io',
        # 'pragma': 'no - cache',
        # 'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    res = session.post(url=url, headers=headers, json=data).json()
    powerAmount = res['data']['powerAmount']
    myDayDCatAmount = res['data']['myDayDCatAmount']
    power_dayHct.append(user + 'pet算力：' + str(powerAmount) + '\t' + '今日产出：' + str(myDayDCatAmount) + '\n')

def getRate(lgdata, ip):
    url = 'https://mobile.herocat.io/vcbank-api/index/herocat/top'
    headers = {
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        # 'origin': 'https://mobile.herocat.io',
        # 'pragma': 'no - cache',
        # 'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    proxies = {
        'http': ip,
        'https': ip
        # 'http': '185.200.36.86:8080',
        # 'https': '185.200.36.86:8080'
    }
    try:
        res = session.get(url=url, headers=headers, proxies=proxies, verify=False).json()
        rate = res['data']['hctToUSDTExchangeRealRate']
        # print(rate)
        return rate
    except requests.exceptions.ConnectionError as e:
        print('代理不可用:', e.args)
        getRate(lgdata, ip)
def getRate(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/index/herocat/top'
    headers = {
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        # 'origin': 'https://mobile.herocat.io',
        # 'pragma': 'no - cache',
        # 'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }

    res = session.get(url=url, headers=headers).json()
    rate = res['data']['hctToUSDTExchangeRealRate']
    # print(rate)
    return rate

def get_totalHct(lgdata, ip):
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
    proxies = {
        'http': ip,
        'https': ip
        # 'http': '185.200.36.86:8080',
        # 'https': '185.200.36.86:8080'
    }
    try:
        res = session.post(url=url, headers=headers, json=data, proxies=proxies, verify=False).json()
        # print(res)
        HCT = res['data'][3]['availableAmount']
        # print(HCT)
        return HCT
    except requests.exceptions.ConnectionError as e:
        print('代理不可用:', e.args)
        get_totalHct(lgdata, ip)
def get_totalHct(lgdata):
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
    res = session.post(url=url, headers=headers, json=data).json()
    # print(res)
    HCT = res['data'][5]['availableAmount']
    # print(HCT)
    return HCT

def feed(rate, totalhct, lgdata, ip):
    # a = int(rate * totalhct)
    # b = round(int(rate * totalhct) / rate, 8)
    all = int(totalhct / 10) * 10
    singal = int(all / 5)
    url = 'https://mobile.herocat.io/vcbank-api/hero_cat/userfeedcat/feed'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'apitoken': lgdata['login_token'],
        'cache-control': 'no-cache',
        'content-length': '127',
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
    proxies = {
        'http': ip,
        'https': ip
        # 'http': '185.200.36.86:8080',
        # 'https': '185.200.36.86:8080'
    }
    if totalhct >= 10:
        data = {"catFoodId":1,"foodAmount":singal,"items":[{"amount":all,"currencyCode":"HCT"},{"amount":"0.0000","currencyCode":"USDT"}]}
        try:
            res = session.post(url=url, headers=headers, data=json.dumps(data), proxies=proxies, verify=False)
            if res.status_code == 200:
                print(user + ': 喂养成功')
            else:
                print(user + ': 喂养失败')
        except requests.exceptions.ConnectionError as e:
            print('代理不可用:', e.args)
            feed(rate, totalhct, lgdata, ip)
    else:
        print(user + ': 余额<10')
def feed(rate, totalhct, lgdata):
    # a = int(rate * totalhct)
    # b = round(int(rate * totalhct) / rate, 8)
    all = int(totalhct / 10) * 10
    singal = int(all / 5)
    url = 'https://mobile.herocat.io/vcbank-api/hero_cat/userfeedcat/feed'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'apitoken': lgdata['login_token'],
        'cache-control': 'no-cache',
        'content-length': '127',
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
    if totalhct >= 10:
        data = {"catFoodId":1,"foodAmount":singal,"items":[{"amount":all,"currencyCode":"HCT"},{"amount":"0.0000","currencyCode":"USDT"}]}
        res = session.post(url=url, headers=headers, data=json.dumps(data))
        if res.status_code == 200:
            print(user + ': 喂养成功')
        else:
            print(user + ': 喂养失败')
    else:
        print(user + ': 余额<10')

if __name__ == '__main__':
    # ip = input('请输入代理地址：')
    file = open("hctFeed_power_tolHct.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        count = len(fr.readlines())

        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = getlogindata(user, password)
            if data:
                getpower_dayHct(data)
                rate = getRate(data)
                totalhct = get_totalHct(data)
                feed(rate, totalhct, data)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
        time.sleep(5)
    with open("hctFeed_power_tolHct.txt", 'a') as fw:
        for i in range(len(power_dayHct)):
            fw.write(power_dayHct[i])