import requests
import bs4
import requests
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "43.128.19.77", 1081, username='1102s', password='1102s')
socket.socket = socks.socksocket

def get():
    url = 'http://www.66ip.cn/nmtq.php?getnum=50&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=2&proxytype=2&api=66ip'
    res = requests.get(url=url)
    # print(res.text)
    with open('tmp.txt', 'w', encoding='utf-8') as fw:
        fw.write(res.text)
    ip_tmp = []
    with open('tmp.txt') as fr:
        keyword = ['<br />']
        for line in fr:
            for key in keyword:
                if key in line:
                    # print(line)
                    ip_tmp.append(line)
                    break
    # print(type(ip_tmp))
    A = str(ip_tmp).replace('<br />', '')
    B = A.replace(r'\t', '')
    C = B.replace(' ', '')
    D = C.replace('[', '')
    E = D.replace("'", '')
    F = E.replace(']', '')
    ip_str = F.replace(r'\n', '')
    # print(ip)
    ip_list = ip_str.split(',')
    # print(type(ip_list))
    print(ip_list)
    # for i in range(len(ip_list)):
    #     print(ip_list[i])
    return ip_list

def proxy_test(ip_port):
    for i in ip_port:
        proxy = i #本地代理
        #proxy='username:password@123.58.10.36:8080'
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        try:
            # response = requests.get('http://httpbin.org/get', proxies=proxies)
            response = requests.get('http://httpbin.org/get', proxies='http://54.39.48.130')
            print(response.json())
        except requests.exceptions.ConnectionError as e:
            print('错误:', e.args)

def proxy_test_test():
    #proxy='username:password@123.58.10.36:8080'
    proxies = {
        # 'http': '119.28.44.140:808',
        # 'https': '119.28.44.140:808'
        'http': '185.200.36.86:8080',
        'https': '185.200.36.86:8080'
    }
    try:
        # requests.packages.urllib3.disable_warnings()
        # response = requests.get('http://httpbin.org/get', proxies=proxies, verify=False)
        # response = requests.get('https://www.baidu.com/', proxies=proxies, verify=False)
        # response = requests.get('https://www.baidu.com/', verify=False)
        response = requests.get('http://httpbin.org/get', verify=False)
        print(response.text)
        print('可用')
    except requests.exceptions.ConnectionError as e:
        print('错误:', e.args)

if __name__ == '__main__':
    # ip_port = get()
    # print(ip_port)
    # proxy_test(ip_port)
    proxy_test_test()
