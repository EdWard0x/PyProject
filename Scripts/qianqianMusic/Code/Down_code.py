import requests
import encry

'''输入歌手名称获取歌曲id'''
def musicSinger_download(name):
    #计算requestid值
    # req_id = str(requestid.PyJs_anonymous_0_(7))
    # part = re.compile("'(.*)'")
    # arr_req = part.findall(req_id)[0]

    URL = 'https://music.taihe.com/v1/search?sign=' + str(encry.sign_code(name)) + '&word=' + name + '&timestamp=' + str(
        encry.Timestamp())
           # https://music.taihe.com/v1/search?sign=858521f01d523d4e83c9b4430b41d26b&word=周杰伦&timestamp=1602152132
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
    }
    res = requests.get(URL,headers=headers).json()
    songs_num = res['data']['typeTrack']
    # print(songs_num)
    for i in range(0,len(songs_num)):
        musci_id = songs_num[i]['TSID']
        musicId_downlaod(musci_id,name)


'''根据音乐id自动下载'''
def musicId_downlaod(music_id,name):
    web_url = 'https://music.taihe.com/v1/song/tracklink?sign=' + str(
        encry.sign_code(name)) + '&TSID=' + music_id + '&timestamp=' + str(encry.Timestamp())
    res = requests.get(web_url).json()
    '''正则匹配'''
    need_url = res['data']
    print(need_url)

    # with open(title + '.mp3', mode='wb') as f:
    #     f.write(res.content)

if __name__ == '__main__':
    musicSinger_download('十年')


