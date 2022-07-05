import hashlib
import mail163_selenium
import requests
import re

session = requests.session()
mail_url = 'https://mail.163.com/'

def get_logindata(user,password):
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
            print(user + ':' + '登录状态：成功')
            re_data = {}
            re_data["login_uid"] = res['data']['uid']
            re_data["login_token"] = res['data']['token']
            # re_data['cookie'] = session.cookies.get_dict()
            # print(session.cookies.get_dict())
            return re_data
    except Exception as e:
        print('登录失败！', e)

def get_mailcode(lgdata):
    url = 'https://mobile.herocat.io/vcbank-api/auth/sendVerifyCode'
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'apitoken': lgdata['login_token'],
        # 'cookie': '_ga=GA1.1.84466953.1634989737; _ga_23QMW81014=GS1.1.' + str(int(t)) + '.1.1.' + str(int(t)) + '.0',
        # 'cookie': lgdata['cookie'],
        'token': lgdata['login_token'],
        'uid': lgdata['login_uid']
    }

if __name__ == '__main__':
    with open('mail.txt', 'r') as fr:
        mail_info = fr.readlines()
    # print(mail_info)
    # print(type(mail_info[0]))
    # print(mail_info[0])
    # print(re.split('-', mail_info[0])[4].replace('\n', ''))
    # print(re.split('-', mail_info[0])[0])
    with open('hero_account.txt', 'r') as fr:
        # txtcount = len(open("account.txt", 'rU').readlines())
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            lgdata = get_logindata(user, password)
            get_mailcode(lgdata)
            for i in range(len(mail_info)):
                mail_info_account = re.split('-', mail_info[i])[0]
                if user == mail_info_account:
                    mail_info_pwd = re.split('-', mail_info[i])[4].replace('\n', '')
                    mail163_selenium.auto_pc(mail_url, mail_info_account, mail_info_pwd)