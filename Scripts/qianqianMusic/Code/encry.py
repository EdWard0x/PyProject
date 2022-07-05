import time
from hashlib import md5
import js2py
from urllib.parse import quote


def useragent_code():
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    code = md5(useragent.encode()).hexdigest()
    return code

def Timestamp():
    t = int(time.time())
    # print(t)
    return t

def sign_code(name):
    t = int(time.time())
    secret = "0b50b02fd0d73a9c4c8c3a781c30845f"
    sign = 'timestamp=' + str(t) + '&word=' + name + secret
    code = md5(sign.encode()).hexdigest()
    return code