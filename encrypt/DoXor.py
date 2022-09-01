# python 异或加密算法, 使用^来计算明文与密文的解译
import random

#input_str = input('请输入1、进行加密，2、进行解密：')

keys = "aaaaaaaaaa"
# 加密
def XorEncode(str_1,keys):
    # 秘钥的种子, random.seed() 默认参数为系统时间
    random.seed(keys)
    str_2 = ''
    for item in str_1:
        str_2 += str(ord(item) ^ random.randint(0, 255)) + ','
    # 去除收尾,逗号
    str_2 = str_2.strip(',')
    #print(str_2)
    return str_2


# 解密
def XorDecode(str_3,keys):
    # 秘钥的种子, random.seed() 默认参数为系统时间
    random.seed(keys)
    str_3 = str_3.split(',')
    str_4 = ''
    for item in str_3:
        item = int(item)
        str_4 += chr(item ^ random.randint(0, 255))
    #print(str_4)
    return str_4

# if input_str == '1':
#     print('您选择加密!')
#     str_1 = input('请输入准备加密的明文：')
#     keys = "aaaaaaaaaa"
#     XorEncode(str_1, keys)
# elif input_str == '2':
#     print('您选择解密：')
#     str_3 = input('请输入准备解密的密文：')
#     keys = input('请输入秘钥：')
#     keys ="aaaaaaaaaa"
#     XorDecode(str_3, keys)
# else:
#     print('请按照规则进行输入！')