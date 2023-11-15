import json
import time

import requests


# session = requests.session()

def getlogindata(user, password):
    url = 'https://payout.minima.global/api/login'
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'
    }
    data = {
        "username": user,
        "password": password
    }
    res = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
    res = res.json()
    try:
        re_data = {}
        re_data["login_token"] = res['accessToken']
        # print(re_data)
        return re_data
    except Exception as e:
        print('登录失败！', e)


def Claim(login_token, user):
    print(login_token['login_token'])
    url = 'https://payout.minima.global/api/user/enroll'
    headers = {
        'Content-Type': 'application/json',
        'authorization': 'Bearer ' + login_token['login_token'],
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'
    }
    data = {
        'address': 'MxG084QHASQ9706YRFY2HRUVDHZ1F3UHD5MPWU4TM0Q08JT2BFDDHFZN617Q398',
        'nodeVersion': "1.0.21"
    }
    try:
        res = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
        print(res.text)
    except Exception as e:
        print('提取失败！', e, user)


if __name__ == '__main__':
    with open('account.txt', 'r') as fr:
        for address in fr.readlines():
            tmp = address.split('----')
            user = tmp[0]
            password = tmp[1].replace('\n', '')
            login_token = getlogindata(user, password)
            Claim(login_token, user)
            time.sleep(30)
