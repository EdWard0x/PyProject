import requests
import time
import datetime
import hashlib
import os
import threading

session = requests.session()

def getlogindata(user,password):
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
    res = session.post(url=url, headers=headers, json=data).json()
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


def getusertokens(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/assets/usertokengains/info'
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'apitoken': lgdata['login_token'],
        # 'cookie': '_ga=GA1.1.84466953.1634989737; _ga_23QMW81014=GS1.1.' + str(int(t)) + '.1.1.' + str(int(t)) + '.0',
        # 'cookie': lgdata['cookie'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    data = {"currencyCode": "HCT"}
    res = session.post(url=url, headers=headers, json=data).json()
    usertokens = int(res['data']['myAmount'])
    # print(usertokens)
    return usertokens
def extokens(lgdata,tokens):
    url = 'https://mobile.herocat.io/vcbank-api/exchange/currencyexchangeinfo/exchange'
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'apitoken': lgdata['login_token'],
        # 'cookie': '_ga=GA1.1.84466953.1634989737; _ga_23QMW81014=GS1.1.' + str(int(t)) + '.1.1.' + str(int(t)) + '.0',
        # 'cookie': lgdata['cookie'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    data = {"amount": tokens,"from": "HCT","to": "USDT"}
    res = session.post(url=url, headers=headers, json=data).json()
    try:
        if res['code'] == 200:
            print(user + ' : ' + '额度兑换 ' + 'ok')
    except Exception as e:
        print('兑换失败！', e)
def usdtassets(lgdata):
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
    res = session.post(url=url, headers=headers, json=data).json()
    # print(res)
    usdtaccount = int(res['data'][5]['availableAmount'])
    return usdtaccount
def feed(lgdata,uaccount):
    t = time.time()
    url = 'https://mobile.herocat.io/vcbank-api/hero_cat/userfeedcat/feed'
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'apitoken': lgdata['login_token'],
        # 'cookie': '_ga=GA1.1.84466953.1634989737; _ga_23QMW81014=GS1.1.' + str(int(t)) + '.1.1.' + str(int(t)) + '.0',
        # 'cookie': lgdata['cookie'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }

    data = {
        "catFoodId": 1,
        "foodAmount": uaccount,
        "items": [{"amount": 0, "currencyCode": "HCT"}, {"amount": uaccount, "currencyCode": "USDT"}]}
    res = session.post(url=url, headers=headers, json=data).json()
    try:
        if res['code'] == 200:
            print(user + ' : ' + '额度喂养 ' + 'ok')
    except Exception as e:
        print('兑换失败！', e)

if __name__ == '__main__':
    # file = open("result.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        # txtcount = len(open("account.txt", 'rU').readlines())
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = getlogindata(user, password)
            if data:
                tokens = getusertokens(data)
                extokens(data, tokens)
                uaccount = usdtassets(data)
                feed(data, uaccount)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
