import requests


def get_pic():
    url= 'http://www.zgcxtcw.cn/index.php/login/verify'
    res = requests.get(url=url)
    picData = res.content
    with open('code.png', 'wb') as fw:
        fw.write(picData)


if __name__ == '__main__':
    get_pic()