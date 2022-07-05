import requests
import socket
import socks

# socks.set_default_proxy(socks.SOCKS5, "119.28.44.140", 808)
# socket.socket = socks.socksocket

proxies = {
            'http': 'http://' + '119.28.44.140:808',
            'https': 'https://' + '119.28.44.140:808'
        }
url = 'http://httpbin.org/get'
# url = 'https://www.baidu.com/'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Host": "httpbin.org",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-61ca86d5-4f2d1dcb24f81a022ece2c3f"
}
res = requests.get(url=url, headers=headers, proxies=proxies)
# res = requests.get(url=url, headers=headers)
print(res)
print(res.text)