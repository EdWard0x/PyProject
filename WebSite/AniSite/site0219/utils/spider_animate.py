import re

import requests
from bs4 import BeautifulSoup

'''获取新番时间'''


def new_ani_time(before='6', after='6'):
    tmp_list = []
    url = 'https://api.bilibili.com/pgc/web/timeline?types=1&before=' + before + '&after=' + after
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        # 'cookie': "buvid3=AFA45CD7-0A4D-C966-C6A4-CBD2E40AE3FF61831infoc; i-wanna-go-back=-1; _uuid=89459E107-522B-107BD-DEFC-CF316E26DE10E62179infoc; buvid4=943E5178-920A-486A-5EF4-685875EE770565203-022021009-7T/Hv0hvMbwUrnV2XWkZ1A%3D%3D; sid=k89cvgph; fingerprint=2e2cfeb2bf5be8e8505fb25dfc31d7a3; buvid_fp_plain=undefined; DedeUserID=6488012; DedeUserID__ckMd5=7da907c751e1d1a2; SESSDATA=538bebbe%2C1660007485%2Ce553d*21; bili_jct=9c5598a50081db2b39750679ac1f527d; b_ut=5; buvid_fp=0776b48af6654831f2876c8e5bbc911e; CURRENT_BLACKGAP=0; blackside_state=1; rpdid=|(Ylm||umJu0J'uYRRRllYuk; bp_video_offset_6488012=627151257712005200; PVID=1; b_lsid=B9BB29B4_17F062926FC; bsource=search_baidu; CURRENT_FNVAL=80; LIVE_BUVID=AUTO1416450758422090; innersign=0",
        'origin': 'https://www.bilibili.com',
        'pragma': 'no-cache',
        'referer': 'https://www.bilibili.com/',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    res = requests.get(url=url, headers=headers).json()

    for obj_dict in res['result']:
        tmp_dict = {}
        for k, v in obj_dict.items():
            tmp_dict['date'] = obj_dict['date']
            tmp_dict['day_of_week'] = obj_dict['day_of_week']
            if k == 'episodes':
                for oo_dict in obj_dict['episodes']:
                    tmp_dict['cover'] = oo_dict['cover']
                    tmp_dict['ep_cover'] = oo_dict['ep_cover']
                    tmp_dict['pub_index'] = oo_dict['pub_index']
                    tmp_dict['pub_time'] = oo_dict['pub_time']
                    tmp_dict['season_id'] = oo_dict['season_id']
                    tmp_dict['square_cover'] = oo_dict['square_cover']
                    tmp_dict['episode_id'] = oo_dict['episode_id']
                    tmp_dict['vedio_addr'] = 'www.bilibili.com/bangumi/play/ss' + str(
                        oo_dict['season_id']) + '?from_spmid=666.13.0.0'
                    tmp_dict['title'] = oo_dict['title']
        tmp_list.append(tmp_dict)

    return tmp_list


'''番剧排行榜'''


def ani_ranking():
    url = 'https://www.bilibili.com/v/popular/rank/bangumi'
    headers = {
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers)

    addr = []
    title = []
    viewers = []
    likers = []
    soup = BeautifulSoup(res.text, 'lxml')
    obj1 = soup.find_all('div', class_='info')
    for i in obj1:
        title.append(i.a.text)
        addr.append(str(i.a['href']).replace('//', ''))
    obj2 = soup.find_all('div', class_='detail-state')
    tmp = []
    for i in obj2:
        for child in i.children:
            if child.name == "span":
                res = str(child.text).replace('\n', '').replace(' ', '')
                tmp.append(res)
    for i in range(0, len(tmp), 2):
        viewers.append(tmp[i])
    for i in range(1, len(tmp), 2):
        likers.append(tmp[i])

    tt_list = []
    tt_list.append(title)
    tt_list.append(viewers)
    tt_list.append(likers)
    tt_list.append(addr)

    tmp_list = []
    for i, j, k, p in zip(tt_list[0], tt_list[1], tt_list[2], tt_list[3]):
        dic = {
            'title': i,
            'viewers': j,
            'likers': k,
            'addr': p
        }
        tmp_list.append(dic)



    return tmp_list


if __name__ == '__main__':
    # result = new_ani_time()
    # print(result)
    # result = ani_ranking()
    # open('text.txt', 'w').close()
    # with open('text.txt', 'w') as f:
    #     f.write(str(result))

    rank = ani_ranking()
    print(rank)
