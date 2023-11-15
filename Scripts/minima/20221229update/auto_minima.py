# -*- coding: utf-8 -*-
#author:xaver
#vx:15087438631

import requests

#配置好minimadocker后，先手动update一个账号，浏览器审查元素  看网络里面  发了个请求 后面的uid固定的
minima_server = "https://192.168.31.99:9004/cmd?uid=0xAD7656DD33DCDF20D99D2B178CAFA272F311B203808BB18BC5437C16554717C5"

#minima的那个ID
minima_uid = ["c4f64ec7-30e8-464c-bdf5-6a86bdc2c962", "89f88d34-35e5-4983-b57f-e6d3300f1070"]

#钉钉通知HOOK
ding_webhook = "https://oapi.dingtalk.com/robot/send?access_token=c40a700c85ca5d82e351d543685545c1de1a0c693dc39b42c0589ac2f4cd92ba"


#直接以文本playload传数据
headers = {"Content-Type": "text/plain"}

total_rewards = 0
#循环取出minimaid去发请求
for i in minima_uid:
    try:
        #incentivecash "uid:"
        data = f"incentivecash uid:{i}"
        print(f"执行uid:{i}")
        #verify关闭一下不然ssl证书报错
        res = requests.post(url=minima_server,headers=headers,data=data,verify=False).json()
        if res["status"] == True:
            previousRewards = res["response"]["details"]["rewards"]["previousRewards"]
            dailyRewards = res["response"]["details"]["rewards"]["dailyRewards"]
            communityRewards = res["response"]["details"]["rewards"]["communityRewards"]
            inviterRewards = res["response"]["details"]["rewards"]["inviterRewards"]
            total_rewards = int(total_rewards) + int(dailyRewards) + int(previousRewards)+int(communityRewards)+int(inviterRewards)

        print(f"总奖励：{total_rewards}")
    except Exception as error:
        requests.post(ding_webhook, json={"msgtype": "text", "text": {"content": f"Minima运行出错{error}"}})
        print(f"运行出错，已发送通知,{error}")

print("当前总奖励：" + str(total_rewards))

#弄完发送钉钉
requests.post(ding_webhook, json={"msgtype": "text", "text": {
    "content": "Minima今日运行完成！\n账号数量：" + str(len(minima_uid)) + "\n当前总奖励：" + str(total_rewards)}})

print("已发送钉钉通知")
