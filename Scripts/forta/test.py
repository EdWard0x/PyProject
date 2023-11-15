import requests



URL = 'https://api.forta.network/stats/sla/scanner/'


def Score(address, ip):
    try:
        res = requests.get(URL + address).json()
        avg = res['statistics']['avg']
        batch_count = res['lowestScores'][0]['inputs']['batch_count']
        # print('add:{0},avg:{1},batch:{2},ip:{3}'.format(address, avg, batch_count, ip))
        print('add:{0},avg:{1},ip:{2}'.format(address, avg, ip))
    except:
        print('获取失败')


if __name__ == '__main__':
    with open('address.txt', 'r') as fr:
        for address in fr.readlines():
            tmp = address.split(' ')
            add = tmp[0]
            ip = tmp[1].replace('\n', '')
            Score(add, ip)
