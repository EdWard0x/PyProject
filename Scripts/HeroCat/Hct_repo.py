import hashlib
import json
import requests
import socket
import socks
import time

socks.set_default_proxy(socks.SOCKS5, "43.128.19.77", 1081, username='1102s', password='1102s')
socket.socket = socks.socksocket



session = requests.session()
tmp = []

def getlogindata(user, password):
    'MD5'
    signaturemd5 = hashlib.md5()
    signaturemd5.update(password.encode())
    pwd = signaturemd5.hexdigest()

    url = 'https://mobile.herocat.io/vcbank-api/auth/login'
    headers = {
        # 'Connection': 'close',
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

def get_ExInfo(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/exchange/currencyexchangeinfo/getExchangeInfo'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'apitoken': lgdata['login_token'],
        'cache-control': 'no-cache',
        'content-length': '26',
        'content-type': 'application/json; charset=UTF-8',
        'language': 'en',
        'origin': 'https://mobile.herocat.io',
        'pragma': 'no-cache',
        'referer': 'https://mobile.herocat.io/buyback',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': "Android",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid'],
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        "from": "HCT",
        "to": "USDT"
    }
    res = session.post(url=url, headers=headers, data=json.dumps(data)).json()
    print(res)
    Hct_amount = res['data']['allowaxExchangeAmount']
    return int(Hct_amount)

def getInfo_Hct(lgdata):
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
    # USDT = res['data'][8]['availableAmount']
    print('可用Hct余额：' + str(HCT))
    return int(HCT)

def Exchange(Hct_balance, hctamount, lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/exchange/currencyexchangeinfo/exchange'
    headers = {
        # 'Connection': 'close',
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        # 'origin': 'https://mobile.herocat.io',
        # 'pragma': 'no - cache',
        # 'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    data = {"amount":hctamount,"from":"HCT","to":"USDT"}
    if Hct_balance >= hctamount:
        res = session.post(url=url, headers=headers, data=json.dumps(data))
        if res.status_code == 200:
            print(user + ': 回购成功')
            tmp.append(user + '回购成功' + '\t' + '数量：' + str(hctamount) + ' ' + str(hctamount*0.2) + 'U' + '\n')
        else:
            print(user + ': 回购失败')
            tmp.append(user + '回购失败' + '\n')
            # print(tmp)
    else:
        print(user + ': Hct余额不足')
        tmp.append(user + 'Hct余额不足' + '\n')

if __name__ == '__main__':
    # ip = input('请输入代理地址：')
    file = open("Hctrepo_res.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        # count = len(fr.readlines())

        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = getlogindata(user, password)
            if data:
                hctamount = get_ExInfo(data)
                Hct_balance = getInfo_Hct(data)
                Exchange(Hct_balance, hctamount, data)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
        time.sleep(5)
    with open("Hctrepo_res.txt", 'a') as fw:
        for i in range(len(tmp)):
            fw.write(tmp[i])