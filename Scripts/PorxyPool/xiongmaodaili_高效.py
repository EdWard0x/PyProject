import requests

ip_arr = []
port_arr = []
ip_port = []

'我的api:http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=bcdeb582d785c62aec7e4151bb6993eb&orderNo=GL201812171444364epf7o8k&count=1&isTxt=0&proxyType=1'

def get_proxy(api_url):
    url = api_url
    res = requests.get(url=url).json()
    obj = res['obj']
    for i in range(len(obj)):
        ip = obj[i]['ip']
        port = obj[i]['port']
        ip_arr.append(ip)
        port_arr.append(port)

def compose_ip_port():
    for i in range(len(ip_arr)):
        temp = str(ip_arr[i]) + ':' + str(port_arr[i])
        ip_port.append(temp)

def proxy_test():
    for i in ip_port:
        proxy = i #本地代理
        #proxy='username:password@123.58.10.36:8080'
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        try:
            response = requests.get('http://httpbin.org/get', proxies=proxies)
            print(response.json())
        except requests.exceptions.ConnectionError as e:
            print('错误:', e.args)



if __name__ == '__main__':
    get_proxy()
    compose_ip_port()
    proxy_test()