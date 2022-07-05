import requests
import re
import json
import time
import random
# from fake_useragent import UserAgent

# ua = UserAgent()
# api_key = '72B1287e2e92168ff6e176d6d6e994d5'
# country = ['0', '1', '7', '43']
country = ['0']
service = 'ot'
class sms:

    api_key = ''

    '''
    询问余额
    '''
    def get_balance(self, api_key):
        url = 'https://api.sms-activate.org/stubs/handler_api.php?api_key=$' + api_key + '&action=getBalance'
        res = requests.get(url=url)
        # print(res.text)
        return res.text


    '''
    获取订单
    '''
    def order_number(self, api_key):
        arr_id_num = []
        # url = 'https://api.sms-activate.org/stubs/handler_api.php?api_key=' + api_key + '&action=getNumber&service=' + service + '&country=' + country[random.randint(0, len(country) - 1)]
        url = 'https://api.sms-activate.org/stubs/handler_api.php?api_key=' + api_key + '&action=getNumber&service=' + service + '&country=' + country[0]
        res = requests.get(url=url)
        print(res.text)
        b = re.findall('(?<=ACCESS_NUMBER:).*$', res.text)  # ACCESS_NUMBER:$id:$number
        c = str(b[0]).split(':')
        d = str(c[1])[0:1]
        e = str(c[1])[1:]
        '''
        俄罗斯专用
        '''
        arr_id_num.append(c[0])     # 号码id
        arr_id_num.append(c[1])     # 号码(带区号)
        arr_id_num.append(d)        # 区号
        arr_id_num.append(e)        # 号码(不带区号)
        print(arr_id_num)
        return arr_id_num


    '''
    激活状态修改
    
    1	通知关于号码的准备状态 （短信被发送）
    3	再次询问密码（免费）
    6	完全激活*
    8	通知关于使用号码而取消激活
    
    $api_key - API密码
    $id - 号码id激活
    $forward * - 要重定向到的电话号码
    * 仅当使用getNumber传递参数forward = 1时才必须。
    $status - 激活状态
    '''
    def active_state_modify(self, order_number, status, api_key):
        url = 'https://api.sms-activate.org/stubs/handler_api.php?api_key=' + api_key + '&action=setStatus&status=' + str(status) + '&id=' + order_number[0]
        res = requests.get(url=url)
        # print(res.text)

    '''
    激活状态查询
    '''
    def active_state_inquire(self, order_number, api_key):
        url = 'https://api.sms-activate.org/stubs/handler_api.php?api_key=' + api_key + '&action=getStatus&id=' + order_number[0]
        res = requests.get(url=url)
        print(res.text)
        if 'STATUS_OK' in res.text:
            reg_code = re.findall('(?<=s: ).*$', res.text)
            # active_state_full(arr_id_num)
            return reg_code
        else:
            return 0