docker_fmt = 'docker run -it --cpus=0.1 --name minima_9{idx:0>2d}1 -p 9{idx:0>2d}1:9{idx:0>2d}1 -p 9{idx:0>2d}2:9{idx:0>2d}2 -e "PORT=9{idx:0>2d}1" -e "RPC=9{idx:0>2d}2" -e "{uuid}" -v ~/minima/data_9{idx:0>2d}1:/minima/data -d qsobad/minima:nighty'
cron_fmt = '{} {} * * * /root/minima/incent.sh minima_9{:0>2d}1 9{:0>2d}2 {}'

def create_crontab(idx, uuid):
    hour = int(idx / 6)
    min = (idx % 6) * 10
    cron1 = cron_fmt.format(min, hour, idx, idx, uuid)
    cron2 = cron_fmt.format(min, hour + 8, idx, idx, uuid)
    cron3 = cron_fmt.format(min, hour + 16, idx, idx, uuid)
    print(cron1)
    print(cron2)
    print(cron3)

def create_shells(idx, uuid):
    docker_sh = docker_fmt.format(idx=idx, uuid=uuid)
    print(docker_sh)

uuids = '''
00073d4f-16c6-4cd6-b7aa-94f04295e4af
300ad179-2c08-4ea9-a98d-4f398e4cb92c
5db19683-0cd0-4f0c-9eed-9df16d2f2e70
1a3a970c-c802-46db-b100-57272a9899c3
d6033240-b356-40fd-be73-d6cc2cd0bb03
0249fff2-cdad-4d62-85d6-2d850af7432d
2d5b836a-f630-452c-9462-9031d4fd483d
9f906d0b-0283-4bd8-9c24-2acb5480b09f
7510f22a-cf28-406a-a42e-ee3d6109558c
79ff95f7-1af7-444c-bf51-e034ab424f53
9257310c-8c26-413f-b162-17e1f925634c
21b22d9f-6023-4c57-a7ac-10e7446f6e06
8be0e901-7615-47dc-a457-059b4d740f80
eba01d43-2acd-4db1-8f60-085ab62cb603
f2cfdefa-5874-4814-9132-4851aef59e60
813db02a-9a99-41ea-ac26-714822413d16
21b22d9f-6023-4c57-a7ac-10e7446f6e06
8be0e901-7615-47dc-a457-059b4d740f80
eba01d43-2acd-4db1-8f60-085ab62cb603
f2cfdefa-5874-4814-9132-4851aef59e60
813db02a-9a99-41ea-ac26-714822413d16
cf4184aa-571e-4555-9226-046379f771af
'''


uuids_list =uuids.split("\n")

idx = 0
for uuid in uuids_list:
    create_shells(idx, uuid)
    idx += 1

idx = 0
for uuid in uuids_list:
    create_crontab(idx, uuid)
    idx += 1