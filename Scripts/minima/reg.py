import re
import time
import json
import requests
# from fake_useragent import UserAgent
from msg import sms
from Scripts.Nodex_mail import take_test
from porxies import xiongmaodaili_高效 as porxie

# ua = UserAgent()

'''
发送验证码
'''
def send_code(order_number):
    url = 'https://verify-9776-kiovbv.twil.io/start-verify'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '17',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://incentivecash.minima.global',
        'pragma': 'no-cache',
        'referer': 'https://incentivecash.minima.global/',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

    }
    data = {
        'to': '+' + order_number[1]
    }

    # proxy = ip()
    # proxies = {
    #     'http': 'http://' + proxy,
    #     'https': 'https://' + proxy
    # }
    res = requests.post(url=url, headers=headers, data=data)
    if res.status_code == 200:
        print(str(order_number[1]) + '短信发送成功')
        return 1
    else:
        print(str(order_number[1]) + '短信发送失败')
        return 0

'''
提交注册信息
'''
def sub_reg(account, password, order_number, reg_code):
    url = 'https://incentivecash.minima.global/api/user/registration'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '181',
        'Content-Type': 'application/json',
        'Host': 'incentivecash.minima.global',
        'Origin': 'https://incentivecash.minima.global',
        'Pragma': 'no-cache',
        'Referer': 'https://incentivecash.minima.global/account/register',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

    }
    data = {
        "email": account,
        "password": password,
        "confirmPassword": password,
        "phoneNumber": order_number[3],
        "phonePrefix": order_number[2],
        "phoneVerifyCode": reg_code[0]
    }
    res = requests.post(url=url, headers=headers, data=json.dumps(data))
    if res.status_code == 200:
        return 1
    else:
        return 0

'''
引入邮箱登录
'''
def get_mail(user, pwd, server):
    IMAP = take_test.IMAP
    IMAP = IMAP(user, pwd, server)
    conn = IMAP.login()
    IMAP.front(conn)
    IMAP.get_content(conn)
    IMAP.loginout(conn)

'''
完善注册
'''
def get_direct_url(link):
    arr = []
    url = link
    # url = 'http://tracking.minima.global/tracking/click?d=QMTKyK8_zTDbp8iAZrPdDAWqlMmA-4llYdkvR5dx5PlmUiwNRNNyleiFLBZP441C4jUra02KqLBD0EUTeIe0UEggjmgnZZHi12OiItX8hPngauYnX6tX9RUdSI5ib8VKIYKPVXS5tJ65WcErNG8DXm9p6CLCJcyvPAD2dQjJzjIJPlNB9QV1jeQvb1GyyTwvRgmZ6gyu3fMGuuBxN0qoj4YDPUj6gyXFglz6XXB7PGAMvdZkSnGmhF3Yb0tKSceB-g2'
    headers = {
        'Host': 'tracking.minima.global',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Accept': 'image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    res = requests.session().get(url=url, headers=headers)
    # print(res.text)
    # print(res.url)
    # print(res.history)
    token = res.url.split('=')[1]
    # print(token)
    arr.append(res.url)
    arr.append(token)
    # print(arr)
    return arr
def first_reg(arr_url):
    url = arr_url[0]
    headers = {
        'Host': 'incentivecash.minima.global',
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-User': '?1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    res = requests.get(url=url, headers=headers)
    # print(res.text)
    # print(res.url)
    # print(res.history)
def last_reg(arr_token):
    url = 'https://incentivecash.minima.global/api/user/registration/' + str(arr_token[1])
    headers = {
        'Host': 'incentivecash.minima.global',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'sec-ch-ua-platform': "Windows",
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://incentivecash.minima.global',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://incentivecash.minima.global/account/registration-verify-email?token=' + arr_token[1],
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    res = requests.post(url=url, headers=headers)
    # if res.status_code == 200:
    #     print('全部步骤完成')
    print(res.status_code)
    # print(res.text)
    # print(res.url)
    # print(res.history)

def ip():
    porxie.get_proxy()
    porxie.compose_ip_port()
    for i in porxie.ip_port:
        return i

if __name__ == '__main__':
    sms = sms()
    sms.api_key = input('请输入api_key:')
    server = input('请输入邮箱域名服务器：')
    with open('account_needreg.txt', 'r') as fr:
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            while True:
                balance_tmp = sms.get_balance()
                balance = re.findall('(?<=:).*$', str(balance_tmp))
                if float(balance[0]) > 20:
                    order_number = sms.order_number()
                    if send_code(order_number):
                        sms.active_state_modify(order_number, 1)
                        start = time.time()
                        while True:
                            if sms.active_state_inquire(order_number):
                                modify = False
                                break
                            else:
                                if time.time() - start > 180:
                                    sms.active_state_modify(order_number, 8)
                                    modify = True
                                    break
                                else:
                                    pass
                        if modify:
                            pass
                        else:
                            reg_code = sms.active_state_inquire(order_number)
                            if sub_reg(user, password, order_number, reg_code):
                                sms.active_state_modify(order_number, 6)
                                break
                            else:
                                print('提交注册信息失败,请手动提交' + order_number[1] + reg_code)
                                break
                    else:
                        print('重新检查ua或者ip')
                        exit(0)
                else:
                    print('余额不足')
                    exit(0)

    # 打开写入的邮件正文
    time.sleep(60)
    with open('mailaccount.txt', 'r') as f:
        for line in f.readlines():
            user = line.split("----")[0]
            pwd = line.split("----")[1].replace('\n', '')

            get_mail(user, pwd, server)
            with open('main_body.txt', 'r') as fr:
                tmp = fr.read()
                if 'Program' in tmp.replace('\n', ''):
                    # 完善注册
                    a = tmp.replace('\n', '')
                    b = re.findall(r'<.*?>', a)
                    link = str(b[0]).replace('<', '').replace('>', '')
                    arr = get_direct_url(link)
                    first_reg(arr)
                    last_reg(arr)
                else:
                    pass