import paramiko

res = []


def conn_ssh(ip, passwd, cmd):
    # 建立连接
    trans = paramiko.Transport((ip, 22))
    trans.connect(username="root", password=passwd)

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans

    # 剩下的就和上面一样了
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    res.append(ip + ':' + ssh_stdout.read().decode() + '\n')
    # 关闭连接
    trans.close()


if __name__ == '__main__':
    # conn_ssh('137.184.32.156', '0519..', 'docker stop masa && docker rm -f masa && docker image prune -af')

    with open('ip.txt', 'r') as fr:
        # txtcount = len(open("account.txt", 'rU').readlines())
        for line in fr.readlines():
            # user = line.split("----")[0]
            # password = line.split("----")[1].replace('\n', '')
            ip = line.replace('\n', '')
            try:
                # if ip == '143.110.238.227':
                #     continue
                conn_ssh(ip, '0519..', 'docker stop masa && docker rm -f masa && docker image prune -af')   #清除原masa信息
                conn_ssh(ip, '0519..', "git clone https://github.com/masa-finance/masa-node-v1.0 && cd masa-node-v1.0 && sed -i '0,/vol1/{s/vol1/\/data\/vol1/}' docker-compose.yml && PRIVATE_CONFIG=ignore docker-compose up -d")   #走官方masa
                conn_ssh(ip, '0519..', 'sudo docker exec -it masa-node-v10_masa-node_1 geth attach /qdata/dd/geth.ipc --exec admin.nodeInfo.enode')   #获取enodeId
            except:
                print(ip + '异常')
    with open("res.txt", 'w') as fw:
    # with open("enodeId.txt", 'w') as fw:
        for i in range(0, len(res)):
            fw.write(res[i])
