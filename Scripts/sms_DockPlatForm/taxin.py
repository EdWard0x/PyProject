import requests
import re
import json
import time
import random


# from fake_useragent import UserAgent


class taxin:
    '''
    登录
    '''

    def Login(self, username, password):
        url = 'http://api.my531.com/Login/?username=' + username + '&password=' + password
        res = requests.get(url=url)
        # print(res.text)
        token = res.text.split('|')[1]
        balance = res.text.split('|')[2]
        commission = res.text.split('|')[3]
        info = []
        info.append(token)
        info.append(balance)
        info.append(commission)
        return info

    '''
    参数名	位置	    必填	    示例值											说明
    token	query	是		2173719145b8355c8db5fd4ee5040286a1815bb8		登录返回的token
    id		query	是		25061											项目ID
    loop	query	否		1												0:排除我加黑过的号码，1:排除我用过加黑过、他人用过的号码，2:不排除任何号码。(默认1)
    isp		query	否		0												筛选运营商，0:不限，1:移动，2:联通，3:电信。(默认0)
    card	query	否		0												筛选号段类型，0:不限，1:虚拟号段，2:正常号段。(默认0)
    area	query	否		山东											    筛选省或市，只需传一个。(UTF-8)
    phone	query	否		13666666666										指定号码
    type	query	否		json											type=json 设置返回json数据 （不传入此参数则为文本数据）
    '''

    def GetPhone(self, token, id, **args):
        url = 'http://api.my531.com/GetPhone/?token=' + token + '&id=' + id + '&type=' + str(args['type'])
        try:
            res = requests.get(url=url)
        except Exception as e:
            print(e)
        else:
            data = res.json()['data']
            if data:
                return data
            else:
                return '无可用号码'
        # print(url)



    '''
    参数名	位置	    必填	    示例值											说明
    token	query	是		2173719145b8355c8db5fd4ee5040286a1815bb8		登录返回的token
    id		query	是		25061											项目ID
    phone	query	否		13666666666										获取验证码的手机号
    dev	    query	否	    taxin888                                        开发者用户名
    type	query	否		json											type=json 设置返回json数据 （不传入此参数则为文本数据）
    '''
    def GetMsg(self,token, id, phone,dev,type):
        url = 'http://api.my531.com/GetMsg/?token=' + token + '&id=' + id + '&phone=' + phone+ '&dev=' + dev+ '&type=' + type
        while True:
            time.sleep(5)
            try:
                res = requests.get(url=url)
            except Exception as e:
                print(e)
            else:
                stat = res.json()['stat']
                if stat:
                    data = res.json()['data']
                    return str(re.findall(r'：.*', data)[0])[1:]
                else:
                    print(res.json()['message'])

