# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import requests
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 572)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 490, 131, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.title = QtWidgets.QTextEdit(Form)
        self.title.setGeometry(QtCore.QRect(310, 60, 104, 41))
        self.title.setObjectName("title")
        self.coin1 = QtWidgets.QLabel(Form)
        self.coin1.setGeometry(QtCore.QRect(200, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.coin1.setFont(font)
        self.coin1.setObjectName("coin1")
        self.enab = QtWidgets.QTextEdit(Form)
        self.enab.setGeometry(QtCore.QRect(170, 10, 104, 31))
        self.enab.setObjectName("enab")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(10, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ab = QtWidgets.QTextEdit(Form)
        self.ab.setGeometry(QtCore.QRect(60, 60, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab.setFont(font)
        self.ab.setObjectName("ab")
        self.favorite = QtWidgets.QTextEdit(Form)
        self.favorite.setGeometry(QtCore.QRect(70, 330, 104, 31))
        self.favorite.setObjectName("favorite")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.like = QtWidgets.QTextEdit(Form)
        self.like.setGeometry(QtCore.QRect(70, 280, 104, 31))
        self.like.setObjectName("like")
        self.pic = QtWidgets.QTextEdit(Form)
        self.pic.setGeometry(QtCore.QRect(60, 120, 361, 41))
        self.pic.setObjectName("pic")
        self.OK = QtWidgets.QPushButton(Form)
        self.OK.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.OK.setObjectName("OK")
        self.coin = QtWidgets.QTextEdit(Form)
        self.coin.setGeometry(QtCore.QRect(260, 280, 104, 31))
        self.coin.setObjectName("coin")
        self.view = QtWidgets.QTextEdit(Form)
        self.view.setGeometry(QtCore.QRect(330, 230, 104, 31))
        self.view.setObjectName("view")
        self.owner = QtWidgets.QTextEdit(Form)
        self.owner.setGeometry(QtCore.QRect(70, 220, 211, 41))
        self.owner.setObjectName("owner")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 490, 131, 71))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(290, 230, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.desc = QtWidgets.QTextEdit(Form)
        self.desc.setGeometry(QtCore.QRect(70, 170, 351, 41))
        self.desc.setObjectName("desc")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(210, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.share = QtWidgets.QTextEdit(Form)
        self.share.setGeometry(QtCore.QRect(270, 330, 104, 31))
        self.share.setObjectName("share")
        self.ab.setReadOnly(True)
        self.title.setReadOnly(True)
        self.pic.setReadOnly(True)
        self.desc.setReadOnly(True)
        self.owner.setReadOnly(True)
        self.view.setReadOnly(True)
        self.like.setReadOnly(True)
        self.coin.setReadOnly(True)
        self.favorite.setReadOnly(True)
        self.share.setReadOnly(True)
        self.OK.clicked.connect(ui.ok)
        self.pushButton_2.clicked.connect(ui.up)
        self.pushButton.clicked.connect(ui.open)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bilibili API"))
        self.pushButton_2.setText(_translate("Form", "UP主頁"))
        self.label_7.setText(_translate("Form", "描述"))
        self.label_9.setText(_translate("Form", "點贊"))
        self.coin1.setText(_translate("Form", "投幣"))
        self.label_2.setText(_translate("Form", "AV/BV"))
        self.label_4.setText(_translate("Form", "封面"))
        self.label_3.setText(_translate("Form", "標題"))
        self.label.setText(_translate("Form", "AV編號或BVID"))
        self.label_11.setText(_translate("Form", "收藏"))
        self.label_6.setText(_translate("Form", "UP:"))
        self.OK.setText(_translate("Form", "OK"))
        self.pushButton.setText(_translate("Form", "打開這個視頻"))
        self.label_8.setText(_translate("Form", "觀看"))
        self.label_12.setText(_translate("From","分享"))
    
    def open(self):
        webbrowser.open(f"https://bilibili.com/video/av{avid}")
    
    def up(self):
        webbrowser.open(f"https://space.bilibili.com/{owner_mid}")

    def ok(self):
        global owner_mid
        global avid
        ab = ui.enab.toPlainText()
        if ab.startswith("AV") or ab.startswith("av"):
            bili = ab[2:]
            response = requests.get(f"https://api.bilibili.com/x/web-interface/view?aid={bili}")
        elif ab.startswith("BV") or ab.startswith("bv"):
            bili = ab
            response = requests.get(f"https://api.bilibili.com/x/web-interface/view?bvid={bili}")
        elif ab.isdigit():
            bili = ab
            response = requests.get(f"https://api.bilibili.com/x/web-interface/view?aid={bili}")
        else:
            QtWidgets.QMessageBox.critical(None,"ERROR","Bilibili视频ID应该是一串以'AV'或'BV'开头的字符，后面跟着数字。")
            return True

        data = response.json()
        root = data.get
        ###Data
        if root("code") != 0:
            QtWidgets.QMessageBox.critical(None,"ERROR",root("message"))
            exit()

        avid = root("data").get("aid")
        bvid = root("data").get("bvid")
        title = root("data").get("title")
        pic = root("data").get("pic")
        desc = root("data").get("desc")
        owner_face = root("data").get("owner").get("face")
        owner_name = root("data").get("owner").get("name")
        owner_mid = root("data").get("owner").get("mid")
        view = root("data").get("stat").get("view")
        like = root("data").get("stat").get("like")
        coin = root("data").get("stat").get("coin")
        favorite = root("data").get("stat").get("favorite")
        share = root("data").get("stat").get("share")

        ui.ab.setPlaceholderText(f"AV{avid}/{bvid}")
        ui.title.setPlaceholderText(title)
        ui.pic.setPlaceholderText(pic)
        ui.desc.setPlaceholderText(desc)
        ui.owner.setPlaceholderText(f"{owner_name}(uid:{owner_mid})")
        ui.view.setPlaceholderText(str(view))
        ui.like.setPlaceholderText(str(like))
        ui.coin.setPlaceholderText(str(coin))
        ui.favorite.setPlaceholderText(str(favorite))
        ui.share.setPlaceholderText(str(share))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())