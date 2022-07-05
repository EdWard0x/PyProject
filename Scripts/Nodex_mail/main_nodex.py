import time

import requests
import bs4
import random



session = requests.session()

def get_index():
    url = 'https://mm.nodex.run/admin'
    headers = {
        'Connection': 'close',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '50',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://mm.nodex.run',
        'pragma': 'no-cache',
        'referer': 'https://mm.nodex.run/admin/ui/login?next=ui.index',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    data = {
        'email': 'avein@aveinmail521.com',
        'pw': '222www',
        'submit': 'Sign in'
    }
    res = session.post(url=url, headers=headers, data=data, verify=False)
    print(res)
    print(res.text)

def get_csrftoken():
    url = 'https://mm.nodex.run/admin/ui/user/settings'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'session=RpTA6B2EeQTpHb3f1ydoWQSxollcw3TNIizqpAD7hlaQYZ39PA',
        'pragma': 'no-cache',
        'referer': 'https://mm.nodex.run/admin/ui/login?next=ui.index',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    res = session.get(url=url, headers=headers)
    # with open('html.html', 'w') as fw:
    #     fw.write(res.text)
    # print(res.text)

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    VIEWSTATE = soup.find('input', id='csrf_token')["value"]

    # VIEWSTATEGENERATOR = soup.find('input', id='__VIEWSTATEGENERATOR')["value"]
    #
    # VEVENTVALIDATION = soup.find('input', id='__EVENTVALIDATION')["value"]
    return VIEWSTATE

def add_mail(csrftoken, random_m, random_p):
    url = 'https://mm.nodex.run/admin/ui/user/create/nodex.run'
    headers = {
        'Connection': 'close',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '285',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'session=RpTA6B2EeQTpHb3f1ydoWQGYrJPM21UvFYUZ8vi_V7uwYZ4Fkw',
        'origin': 'https://mm.nodex.run',
        'pragma': 'no-cache',
        'referer': 'https://mm.nodex.run/admin/ui/user/create/nodex.run',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    data = {
        'csrf_token': csrftoken,
        'localpart': random_m,
        'pw': random_p,
        'pw2': random_p,
        'displayed_name': random_m,
        'comment': random_m,
        'enabled': 'y',
        'quota_bytes': '1000000000',
        'enable_imap': 'y',
        'enable_pop': 'y',
        'submit': 'Save'
    }
    res = session.post(url=url, headers=headers, data=data, verify=False)
    fw.write(random_m + '----' + random_p + '\n')
    print('ok')
    # print(res.status_code)
    # print(res.text)



if __name__ == '__main__':
    mail_num = input('输入创建的邮箱数量：')
    time.sleep(5)
    with open('words.txt', 'r') as fr:
        words = fr.read().split(',')
    get_index()
    csrftoken = get_csrftoken()
    with open("account.txt", 'w', encoding='utf-8') as fw:
        for i in range(int(mail_num)):
            words_index1 = random.randint(0, len(words) - 1)
            words_index2 = random.randint(0, len(words) - 1)
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 99)
            random_m = str(words[words_index1]) + str(words[words_index2]) + str(num1) + str(num2)
            random_p = '1111qqqq'
            add_mail(csrftoken, random_m, random_p)