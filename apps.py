# -*- coding: utf-8 -*-
import subprocess, requests, time, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

style = open('style.txt' , 'r').read()

class Ui_Form(object):
    def setupUi(self, Form):
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(379, 304)
        Form.setStyleSheet(style)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-40, -10, 551, 331))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("background-image: url(:/For UI.png);")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 130, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.hwid)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.CheckTrial)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Check Trial")
        Form.setWindowIcon(QIcon(r':/For UI.png'))
        self.pushButton.setText(_translate("Form", "Login"))

    def CheckTrial(self):
        hwid1 = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        checkout = requests.get('https://pastebin.com/raw/NKC2ELzC')

        try:
            if hwid1 in checkout.text:
                QMessageBox.information(Form , 'Have Fun'  , 'Enjoy :)              ')
            else:
                QMessageBox.information(Form ,"Please Subscribe" , 'You are not a subscriber or the subscription period has expired')
                exit()
        except:
            exit()

import soo
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
