import hashlib
import json
import requests


BEP20 = []
HECO = []
TRC20 = []
ERC20 = []


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

def getaddr(user, lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/assets/usercurrencyaddress/deposit'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json; charset=UTF-8',
        'apitoken': lgdata['login_token'],
        # 'cookie': '_ga=GA1.1.84466953.1634989737; _ga_23QMW81014=GS1.1.' + str(int(t)) + '.1.1.' + str(int(t)) + '.0',
        # 'cookie': lgdata['cookie'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }
    data = {"currencyCode": "USDT"}
    res = session.post(url=url, headers=headers, data=json.dumps(data)).json()
    # print(res)
    # bep20_addr = res['data'][0]['address']

    # HECO_addr = res['data'][1]['address']

    TRC20_addr = res['data'][2]['address']

    # ERC20_addr = res['data'][3]['address']

    # BEP20.append('BEP20: ' + user + ' : ' + bep20_addr + '\n')
    # HECO.append('HECO: ' + user + ' : ' + HECO_addr + '\n')
    TRC20.append('TRC20: ' + user + ' : ' + TRC20_addr + '\n')
    # ERC20.append('ERC20: ' + user + ' : ' + ERC20_addr + '\n')

    print('ok')

    # print(BEP20)
    # print(HECO)
    # print(TRC20)
    # print(ERC20)

if __name__ == '__main__':
    file = open("address.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        # txtcount = len(open("account.txt", 'rU').readlines())
        # print(txtcount)
        # print(fr.readlines())
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = getlogindata(user, password)
            if data:
                getaddr(user, data)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
    with open("address.txt", 'a') as fw:
        for i in range(len(TRC20)):
            fw.write(TRC20[i])
