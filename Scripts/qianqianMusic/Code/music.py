# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtWidgets
import requests
import encry
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 109)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.musicSinger_download)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "千千音乐下载器"))
        self.pushButton.setText(_translate("MainWindow", "下载"))

    '''输入歌手名称获取歌曲id'''
    def musicSinger_download(self):
        name = self.lineEdit.text()
        #计算requestid值
        # req_id = str(requestid.PyJs_anonymous_0_(7))
        # part = re.compile("'(.*)'")
        # arr_req = part.findall(req_id)[0]

        URL = 'https://music.taihe.com/v1/search?sign=' + str(
            encry.sign_code(name)) + '&word=' + name + '&timestamp=' + str(encry.Timestamp())
               # https://music.taihe.com/v1/search?sign=858521f01d523d4e83c9b4430b41d26b&word=周杰伦&timestamp=1602152132
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
        }
        res = requests.get(URL,headers=headers).json()
        songs_num = res['data']['typeTrack']
        # print(songs_num)
        for i in range(0,len(songs_num)):
            musci_id = songs_num[i]['TSID']
            self.musicId_downlaod(musci_id,name)


    '''根据音乐id自动下载'''
    def musicId_downlaod(self,music_id,name):
        web_url = 'https://music.taihe.com/v1/song/tracklink?sign=' + str(
            encry.sign_code(name)) + '&TSID=' + music_id + '&timestamp=' + str(encry.Timestamp())
        res = requests.get(web_url).json()['data']
        '''正则匹配'''
        res_str = str(res)
        # print(res_str)
        a = re.compile(r"'path': '(.*?)'")
        Last_url = re.findall(a,res_str)[0]
        # print(Last_url)
        music = requests.get(Last_url).content
        with open('./Music/' + music_id + '.mp3', mode='wb') as f:
            f.write(music)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication