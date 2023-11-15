import requests

session = requests.session()

lastPing_arr = []
dailyRewards_arr = []
previousRewards_arr = []


useruid_arr = []
nodeuid_arr = []

def login(user, password):
    url = 'https://incentive.minima.global/api/login'
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
    url = 'https://incentive.minima.global/api/node-id'
    res = session.get(url=url)
    uid = res.text
    useruid_arr.append(user)
    nodeuid_arr.append(uid)

def rewards():
    url = 'https://incentive.minima.global/api/rewards'
    res = session.get(url=url).json()
    lastPing = res['lastPing'] + '\t'
    dailyRewards = res['rewards']['dailyRewards']
    previousRewards = res['rewards']['previousRewards']
    lastPing_arr.append(lastPing)
    dailyRewards_arr.append(dailyRewards)
    previousRewards_arr.append(previousRewards)

if __name__ == '__main__':
    file = open("result_uid.txt", 'w').close()

    with open('uid_account.txt', 'r') as fr:
        for line in fr.readlines():
            user = line.split("----")[0]
            password = line.split("----")[1].replace('\n', '')
            data = login(user, password)
            if data:
                # rewards()
                uid(user)
            else:
                print(user + ' : ' + '该账号信息错误，跳过该账号')
    with open("result_uid.txt", 'a') as fw:
        # for i in range(len(lastPing_arr)):
        #     fw.write(user + '\n' + '\t' + 'lastPing: ' + lastPing_arr[i] + '\n')
        #     fw.write('\t' + 'dailyRewards: ' + str(dailyRewards_arr[i]) + '\n')
        #     fw.write('\t' + 'previousRewards: ' + str(previousRewards_arr[i]) + '\n')
        for i in range(len(nodeuid_arr)):
            fw.write(useruid_arr[i] + '：' + nodeuid_arr[i] + '\n')