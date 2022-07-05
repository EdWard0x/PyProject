import re
import time

# a = re.findall('(?<=s: ).*$', "STATUS_OK:Your Minima verification code is: 140975")
# print(a)



# t = 'ACCESS_NUMBER:49879451:5558979413'
# b = re.findall('(?<=ACCESS_NUMBER:).*$', t)
# print(b)
# c = str(b[0]).split(':')
# print(c)
# print(c[0])
# print(c[1])
# d = str(c[1])[0:1]
# print(d)
# e = str(c[1])[1:]
# print(e)
# arr = []
# arr.append(c[0])
# arr.append(d)
# print(arr)
# e = d[1:]
# print(e)
# with open('html.txt', 'r') as fr:
#     a = fr.read()
# print(a)
# print(str(a[6]).replace('<', '').replace('>', ''))
# pattern = re.compile(r'".*?"')
# b = re.findall(r'".*?"', a)[0]
# print(str(b).strip('"').split("=")[1])
# from fake_useragent import UserAgent
# ua = UserAgent()
# print(ua.random)
# start = time.time()
# time.sleep(5)
# print(start)
# if time.time() - start > 5:
#     print('ok')
# url = 'https://incentivecash.minima.global/account/registration-verify-email?token=05d937a0-73b8-48a8-87a4-a6ed83960bb9'
# b = url.split('=')[1]
# print(b)
import requests


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
    res = requests.get(url=url)
    # print(res.text)
    print(res.url)
    print(res.history)

# get_direct_url('http://tracking.minima.global/tracking/click?d=QMTKyK8_zTDbp8iAZrPdDAWqlMmA-4llYdkvR5dx5PlmUiwNRNNyleiFLBZP441C4jUra02KqLBD0EUTeIe0UEggjmgnZZHi12OiItX8hPngauYnX6tX9RUdSI5ib8VKIYKPVXS5tJ65WcErNG8DXm9p6CLCJcyvPAD2dQjJzjIJPlNB9QV1jeQvb1GyyTwvRgmZ6gyu3fMGuuBxN0qoj4YDPUj6gyXFglz6XXB7PGAMvdZkSnGmhF3Yb0tKSceB-g2')

with open('main_body.txt', 'r') as fr:
    tmp = fr.read()

a = tmp.replace('\n', '')
b = re.findall(r'<.*?>', a)
print(str(b[0]).replace('<', '').replace('>', ''))


