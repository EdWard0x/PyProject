import requests

session = requests.session()

user_arr = []
lastPing_arr = []
dailyRewards_arr = []
previousRewards_arr = []


useruid_arr = []
nodeuid_arr = []

def login(user, password):
    url = 'https://incentivecash.minima.global/api/login'
    data = {
        'username': user,
        'password': password
    }
    res = session.post(url=url, data=data)
    if res.status_code == 200:
        return 1
    else:
        pass

def uid(user):
    url = 'https://incentivecash.minima.global/api/node-id'
    res = session.get(url=url)
    uid = res.text
    useruid_arr.append(user)
    nodeuid_arr.append(uid)

def rewards(user):
    url = 'https://incentivecash.minima.global/api/rewards'
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    res = session.get(url=url, headers=headers).json()
    lastPing = res['lastPing']
    dailyRewards = res['rewards']['dailyRewards']
    previousRewards = res['rewards']['previousRewards']
    user_arr.append(user)
    lastPing_arr.append(lastPing)
    dailyRewards_arr.append(dailyRewards)
    previousRewards_arr.append(previousRewards)

if __name__ == '__main__':
    file = open("result.txt", 'w').close()
    with open('account.txt', 'r') as fr:
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = login(user, password)
            if data:
                rewards(user)
                # uid(user)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')

    with open("result.txt", 'w', encoding='utf-8') as fw:
        for i in range(len(user_arr)):
            fw.write(user_arr[i] + '\n')
            fw.write('\t' + 'lastPing: ' + str(lastPing_arr[i]) + '\n')
            fw.write('\t' + 'dailyRewards: ' + str(dailyRewards_arr[i]) + '\n')
            fw.write('\t' + 'previousRewards: ' + str(previousRewards_arr[i]) + '\n')
        # for i in range(len(nodeuid_arr)):
        #     fw.write(useruid_arr[i] + '：' + nodeuid_arr[i] + '\n')