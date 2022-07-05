import wangyi_para
import requests
import time
import json

rtid = wangyi_para.get_tid()
t_temp = time.time()
t = (int(round(t_temp * 1000)))
session = requests.session()


# print(tid)

'''网易'''
def get_tk(mail_account):
    url = 'https://dl.reg.163.com/dl/gt?un=' + mail_account + '&pkid=CvViHzl&pd=mail163&channel=0&topURL=https%3A%2F%2Fmail.163.com%2F&rtid=' + rtid + '&nocache=' + str(t)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'utid=JQ5w8s6ZrG9doxXdddPTQanlJCR2kTBQ; _9755xjdesxxd_=32; YD00000710348764:WM_NI=kW7cRymw9jxduE5jm8VtQBtHYs1R+EZ5r6eukzYye9v9tBWhZM1GYvN1ipcIqFS7sLv8G1Yld+0UoI5VbzXPavD8luewtb8cMeu0pozKhKz3cmVEzVPJU1PZSnSC8xdsTkM=; YD00000710348764:WM_NIKE=9ca17ae2e6ffcda170e2e6eeccc63f9ab19f92cc43f2a88ab3c84b968a9e85b565b29e8989ec3bbaf1e1d9ce2af0fea7c3b92aa989f984d173afa9f78bfb70b79bfb8bf03496ac9fa3f7449badffb3aa4f9aebbed7e87fa9a6979ae833b6e7bca3d6649a93ffa8dc7e8eefa791e243b39a9dd8f248b6e889d2dc68a8f500b6ee43f78aae9bdb5ca3aa8cd9ef7fa7a9bc83bb698fbbbbd1f365ba95a8acf939a1b39aa6f95e94969bd2d35291b29da4bb74a8ad9c8cd037e2a3; YD00000710348764:WM_TID=w9f0+4FxWyZEFUBQUUZvt7BHknwm6/4e; gdxidpyhxdE=RkwBW8tuWvdmlLOrET4CCDU8xJi/zwhPB5gufOG/apDcMGapnGOEZ9VaQuiSBI4r0rNCkIIWrk1EMZm9obI+1dgfrkK2QEZEg0NtaTicLnzOoG8nXGlnplmb+62Ojj92dUpYqi/1Cs\alBL0TLI5/HlTHZJp3yZPB8l6Uf6uYLwzmR6G:1639632138032; NTES_WEB_FP=9a4be280842f13fbd1e063128c9659f9; NTES_P_UTID=JQ5w8s6ZrG9doxXdddPTQanlJCR2kTBQ|1645419054; THE_LAST_LOGIN=avein521@163.com; nts_mail_user=avein521@163.com:-1:1; _ntes_nnid=a719ec3c6bfc04ae5ac1f97675b26b39,1645419061266; _ntes_nuid=a719ec3c6bfc04ae5ac1f97675b26b39; l_s_mail163CvViHzl=2BDA1093FDDA9283AD02B57FFFEC7E0EA0DE0F870A54A4EC1D7C739BA355DD0A26FE1439240F98E748A483839B4246F491A9FA58AFD1DFE7FA98221593011893C88416F311E20C760E7E5D1AC8F681DD9BBEFDD2793C094FBBFB40671B1AF04D94BC54E66F7C1AA1AC4E91CA614581CB',
        'Host': 'dl.reg.163.com',
        'Pragma': 'no-cache',
        'Referer': 'https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2021%2F%2Fcss%2F&cf=urs.163.4b996708.css&MGID=1636938723986.326&wdaId=&pkid=CvViHzl&product=mail163',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    # res = session.get(url=url, headers=headers)
    # print(res.status_code)
    # print(res)
    res = session.get(url=url, headers=headers).json()
    if res['ret'] == 201:
        # print('get_tk_status:' + str(res))
        # print(res.text)
        return res['tk']
    else:
        print(res)
def get_login(mail_account, password, tk):
    url = 'https://dl.reg.163.com/dl/l'
    pwd = wangyi_para.get_pwd(password)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '421',
        'Content-Type': 'application/json',
        'Cookie': 'utid=rnDmqUGN8i1rfPyviJQrkezhkKMLcfBA; NTES_WEB_FP=b631263f422d2325c9ac6164f5dd0237; l_s_mail163CvViHzl=2BDA1093FDDA9283AD02B57FFFEC7E0EC8337A965B1C629FB6608FFD6F32B977CF3CD7CD8391749086EA18AD5DBE96D1C109E6DD6A2A7EF9265A343BCD316227E214E1DC4741B0DA4AB0C0621116626DCE8B44CB884CA0E6A3DC8457F2989C96748C5CE0C69985D0217B4708C58BB6D4',
        'Host': 'dl.reg.163.com',
        'Origin': 'https://dl.reg.163.com',
        'Pragma': 'no-cache',
        'Referer': 'https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2021%2F%2Fcss%2F&cf=urs.163.4b996708.css&MGID=1636938090486.2627&wdaId=&pkid=CvViHzl&product=mail163',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    data = {
        "un": mail_account,
        "pw": pwd,
        "pd": "mail163",
        "l": 0,
        "d": 10,
        "t": t,
        "pkid": "CvViHzl",
        "domains": "163.com",
        "tk": tk,
        "pwdKeyUp": 1,
        "channel": 0,
        "topURL": "https://smart.mail.163.com/login.htm",
        "rtid": rtid
    }
    res = session.post(url=url, headers=headers, data=json.dumps(data))
    print(res.text)
    # print(res.status_code)
    # print(res.text)
def getUnRead():
    url = 'https://mail.163.com/js6/s?sid=ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX&func=mbox:listMessages'
    headers = {
        'accept': 'text/javascript',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '746',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'starttime=; NTES_P_UTID=WaXCE1u3aOFECTzfh3K4ZnfYUg5HNgD9|1636938765; NTES_SESS=GtuWgki7VVL.yU3K4iBy8TizC1iaV1SAzZYZbnS4UJXpMmy6MT5QSOv5.C8fhW70mgL8rJ7I40XOziH8cwpS6Thd7vBWQ_u_D3dGG800mI6MYGl2.akzO19LVAEQGA8TSVwSyM717jRIqJpIrDR_d5WplK3QKVQh5d.N6N9tWpXqvM5RAKm4lipOQie5x74JczNxTJMv7d_wO; S_INFO=1636938765|0|3&80##|avein521; P_INFO=avein521@163.com|1636938765|0|mail163|00&99|shd&1636938106&mail163#shd&370100#10#0#0|&0|mail163|avein521@163.com; nts_mail_user=avein521@163.com:-1:1; df=mail163_letter; mail_upx=t5hz.mail.163.com|t6hz.mail.163.com|t10hz.mail.163.com|t11hz.mail.163.com|t12hz.mail.163.com|t13hz.mail.163.com|c2bj.mail.163.com|c3bj.mail.163.com|c4bj.mail.163.com|c5bj.mail.163.com|c6bj.mail.163.com|c7bj.mail.163.com|c1bj.mail.163.com; mail_upx_nf=; mail_idc=""; Coremail=fb8cb049f68a1%ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX%g1a135.mail.163.com; MAIL_ENTRY_INFO=1|0|mail163|mail163_letter|39.64.220.142|9cf70abbcf8688642e5f3f5d876b624d_v1|; MAIL_ENTRY_CS=0a097217982d1b75f877ec2e5fe217e6; cm_last_info=dT1hdmVpbjUyMSU0MDE2My5jb20mZD1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEQURCaG1WUlJVc2RMaXRCWVVJUlJ6ZEpEUXhSTk5qWlgmcz1BREJobVZSUlVzZExpdEJZVUlSUnpkSkRReFJOTmpaWCZoPWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RBREJobVZSUlVzZExpdEJZVUlSUnpkSkRReFJOTmpaWCZ3PWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJmw9LTEmdD0tMSZhcz10cnVl; MAIL_SESS=GtuWgki7VVL.yU3K4iBy8TizC1iaV1SAzZYZbnS4UJXpMmy6MT5QSOv5.C8fhW70mgL8rJ7I40XOziH8cwpS6Thd7vBWQ_u_D3dGG800mI6MYGl2.akzO19LVAEQGA8TSVwSyM717jRIqJpIrDR_d5WplK3QKVQh5d.N6N9tWpXqvM5RAKm4lipOQie5x74JczNxTJMv7d_wO; MAIL_SINFO=1636938765|0|3&80##|avein521; MAIL_PINFO=avein521@163.com|1636938765|0|mail163|00&99|shd&1636938106&mail163#shd&370100#10#0#0|&0|mail163|avein521@163.com; secu_info=1; mail_entry_sess=44c37ac9d34c7eb68b03794902ef3a76a58b9b1cb52ecf92e216f522829bf370841f0fd8a6484da6302469ba3bb3fdf020696d7a01a9f94e1e65abe198654031cd9d3503d1ffc13b1fdd08192c37ff282800621ba0de23af1cc359bdbe25e834102857e3016cb6f16256a82ff051ed2f87e401c9e3988c315233e80831cfdc625757f90f6710f6e5f9a1d7bb2bf553cd7c7daacbb4134f9ddf5f15661ab0150f47749901823592ad437a8c2cbb3327f3de43b8ac4c61f25bdd41d1b27eebb005; JSESSIONID=E51B6008A2DDE48B9957C1B8D7C6ECD2; locale=; face=js6; Coremail.sid=ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX; mail_style=js6; mail_uid=avein521@163.com; mail_host=mail.163.com',
        'origin': 'https://mail.163.com',
        'pragma': 'no-cache',
        'referer': 'https://mail.163.com/js6/main.jsp?sid=ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX&df=mail163_letter',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    data = {
        'var': '<?xml version="1.0"?><object><array name="fids"><int>1</int></array><object name="filter"><object name="flags"><boolean name="read">false</boolean></object></object><string name="order">date</string><boolean name="desc">true</boolean><int name="limit">20</int><int name="start">0</int><boolean name="skipLockedFolders">false</boolean><boolean name="returnTag">true</boolean><boolean name="returnTotal">true</boolean><string name="mrcid">9cf70abbcf8688642e5f3f5d876b624d_v1</string></object>'
    }
    res = session.post(url=url, headers=headers, data=data).text
    print(res)
    # last_mid_top = res.index('id') + 5
    # last_mid_tail = res.index('fid') - 4
    # return res[last_mid_top: last_mid_tail]
def getMain(unreadmid):
    # total = unread['total']
    # subject = unread['var'][0]['subject']
    # last_unread_mid = unread['var'][0]['id']
    # print(type(unreadmid))
    print(unreadmid)
    data = {}
    t = '+'
    new = []
    while True:
        for i in unreadmid:
            if i == '+':
                i = ' '
                new.append(i)
            else:
                new.append(i)
        break
    k = ''.join(new)

    url = 'https://mail.163.com/js6/read/readhtml.jsp?mid=' + unreadmid + '&userType=ud&font=15&color=4D677D'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'starttime=; NTES_P_UTID=WaXCE1u3aOFECTzfh3K4ZnfYUg5HNgD9|1636938765; NTES_SESS=GtuWgki7VVL.yU3K4iBy8TizC1iaV1SAzZYZbnS4UJXpMmy6MT5QSOv5.C8fhW70mgL8rJ7I40XOziH8cwpS6Thd7vBWQ_u_D3dGG800mI6MYGl2.akzO19LVAEQGA8TSVwSyM717jRIqJpIrDR_d5WplK3QKVQh5d.N6N9tWpXqvM5RAKm4lipOQie5x74JczNxTJMv7d_wO; S_INFO=1636938765|0|3&80##|avein521; P_INFO=avein521@163.com|1636938765|0|mail163|00&99|shd&1636938106&mail163#shd&370100#10#0#0|&0|mail163|avein521@163.com; nts_mail_user=avein521@163.com:-1:1; df=mail163_letter; mail_upx=t5hz.mail.163.com|t6hz.mail.163.com|t10hz.mail.163.com|t11hz.mail.163.com|t12hz.mail.163.com|t13hz.mail.163.com|c2bj.mail.163.com|c3bj.mail.163.com|c4bj.mail.163.com|c5bj.mail.163.com|c6bj.mail.163.com|c7bj.mail.163.com|c1bj.mail.163.com; mail_upx_nf=; mail_idc=""; Coremail=fb8cb049f68a1%ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX%g1a135.mail.163.com; MAIL_ENTRY_INFO=1|0|mail163|mail163_letter|39.64.220.142|9cf70abbcf8688642e5f3f5d876b624d_v1|; MAIL_ENTRY_CS=0a097217982d1b75f877ec2e5fe217e6; cm_last_info=dT1hdmVpbjUyMSU0MDE2My5jb20mZD1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEQURCaG1WUlJVc2RMaXRCWVVJUlJ6ZEpEUXhSTk5qWlgmcz1BREJobVZSUlVzZExpdEJZVUlSUnpkSkRReFJOTmpaWCZoPWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RBREJobVZSUlVzZExpdEJZVUlSUnpkSkRReFJOTmpaWCZ3PWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJmw9LTEmdD0tMSZhcz10cnVl; MAIL_SESS=GtuWgki7VVL.yU3K4iBy8TizC1iaV1SAzZYZbnS4UJXpMmy6MT5QSOv5.C8fhW70mgL8rJ7I40XOziH8cwpS6Thd7vBWQ_u_D3dGG800mI6MYGl2.akzO19LVAEQGA8TSVwSyM717jRIqJpIrDR_d5WplK3QKVQh5d.N6N9tWpXqvM5RAKm4lipOQie5x74JczNxTJMv7d_wO; MAIL_SINFO=1636938765|0|3&80##|avein521; MAIL_PINFO=avein521@163.com|1636938765|0|mail163|00&99|shd&1636938106&mail163#shd&370100#10#0#0|&0|mail163|avein521@163.com; secu_info=1; mail_entry_sess=44c37ac9d34c7eb68b03794902ef3a76a58b9b1cb52ecf92e216f522829bf370841f0fd8a6484da6302469ba3bb3fdf020696d7a01a9f94e1e65abe198654031cd9d3503d1ffc13b1fdd08192c37ff282800621ba0de23af1cc359bdbe25e834102857e3016cb6f16256a82ff051ed2f87e401c9e3988c315233e80831cfdc625757f90f6710f6e5f9a1d7bb2bf553cd7c7daacbb4134f9ddf5f15661ab0150f47749901823592ad437a8c2cbb3327f3de43b8ac4c61f25bdd41d1b27eebb005; JSESSIONID=E51B6008A2DDE48B9957C1B8D7C6ECD2; locale=; face=js6; Coremail.sid=ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX; mail_style=js6; mail_uid=avein521@163.com; mail_host=mail.163.com',
        'pragma': 'no-cache',
        'referer': 'https://mail.163.com/js6/main.jsp?sid=ADBhmVRRUsdLitBYUIRRzdJDQxRNNjZX&df=mail163_letter',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    if t in unreadmid:
        data = {
            'mid': k,
            'userType': 'ud',
            'font': '15',
            'color': '4D677D'
        }
    else:
        data = {
            'mid': unreadmid,
            'userType': 'ud',
            'font': '15',
            'color': '4D677D'
        }
    res = session.get(url=url, headers=headers, data=data)
    print('读取最新一封邮件状态：' + res)


if __name__ == '__main__':
    tk = get_tk("avein521@163.com")
    # get_login("avein521@163.com", "czhZDY0519", tk)
    # unreadmid = getUnRead()
    # getMain(unreadmid)
    # tk = get_tk("zx7619392911@163.com")
    # get_login("zx7619392911@163.com", "Zx761939291", tk)
    # unreadmid = getUnRead()
    # getMain(unreadmid)