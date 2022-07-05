# -*- coding:utf-8 -*-
import os
import re
if __name__ == "__main__":
    rootdir = '.\port'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            # # 你想对文件的操作
            # print(path)
            name = re.findall(r'm.*?h', path)[0]
            # print(name)
            with open('./port/' + name, 'r') as fr:
                t = fr.read()
                # print(t)
                m = str(re.findall(r'c.*?\n', t)[2]).replace('\n', '')
                print(m)
