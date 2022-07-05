import requests
import hashlib
import json
import socket
import socks
import time
from urllib import request

socks.set_default_proxy(socks.SOCKS5, "8.218.90.98", 2333, username='1111', password='1111')
socket.socket = socks.socksocket

session = requests.session()
addr = []
def getlogindata(user,password):
    'MD5'
    signaturemd5 = hashlib.md5()
    signaturemd5.update(password.encode())
    pwd = signaturemd5.hexdigest()

    url = 'https://mobile.herocat.io/vcbank-api/auth/login'
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'
    }
    data = {
        "email": user,
        "password": pwd,
        "actionToken": ""
    }
    # res = session.post(url=url, headers=headers, data=json.dumps(data))
    req = request.Request(url=url,data=json.dumps(data).encode('utf-8'),headers=headers,method='POST')
    res = request.urlopen(req)
    print(res.read())

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

def getassets_HCT(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/assets/accounts/info'
    headers = {
        'apitoken': lgdata['login_token'],
        'content - type': 'application/json; charset=UTF-8',
        'origin': 'https://mobile.herocat.io',
        'pragma': 'no - cache',
        'referer': 'https://mobile.herocat.io/myHPET',
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    res = session.post(url=url, headers=headers)
    print(res)
    print(res.status_code)
    print('getassets_HCT')
    res = res.json()
    # print(res)
    HCT = res['data'][5]['availableAmount']
    return HCT

def getAddrId(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/assets/usercurrencyaddress/withdraw'
    headers = {
        'apitoken': lgdata['login_token'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid'],
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'

    }
    res = session.post(url=url, headers=headers)
    print(res)
    print(res.status_code)
    print('getAddrId')
    res = res.json()
    userCurrencyAddressId = res['data'][0]['userCurrencyAddressId']
    return userCurrencyAddressId

def withdrow(user, hct_account, AddressId):
    url = 'https://mobile.herocat.io/vcbank-api/assets/withdraw/apply'
    headers = {
        'apitoken': lgdata['login_token'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid'],
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'
    }
    data = {
        "userCurrencyAddressId": AddressId,
        "amount": hct_account,
        "currencyCode": "HCT",
        "isChangeFromUSD": 'false',
        "password": '7ae6dc96d7ee59bc7202899281ca5821'
    }
    if int(hct_account) >= 100:
        res = session.post(url=url, headers=headers, data=json.dumps(data)).json()
        if res['code'] == 200:
            print(user + ': ' + str(hct_account))
            addr.append(user + ': ' + str(hct_account))
        else:
            print(user + ': ' + '提取失败')
            addr.append(user + ': ' + '提取失败')
    else:
        print(user + '：数量<100')
        addr.append(user + '：数量<100')


if __name__ == '__main__':
    file = open("withdrow_Hct.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        # txtcount = len(open("account.txt", 'rU').readlines())
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            lgdata = getlogindata(user, password)
            if lgdata:
                HCT_Account = getassets_HCT(lgdata)
                AddressId = getAddrId(lgdata)
                withdrow(user, HCT_Account, AddressId)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
        time.sleep(5)
    with open("withdrow_Hct.txt", 'a') as fw:
        for i in range(len(addr)):
            fw.write(addr[i])