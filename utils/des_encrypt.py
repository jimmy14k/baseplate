import base64
from pyDes import *


'''
name=叶海涛&type=test&q=aaa ====>>> urgveus2G59mj2kRPnfwiGX6L+HdmK9JjKJ7AX/3Pek=
'''

KEY = '12345678'
IV = KEY


def Encrption(str):
    k = des(KEY, CBC, IV, padmode=PAD_PKCS5)
    return base64.b64encode(k.encrypt(str))


# 解密
def Deode(str):
    k = des(KEY, CBC, IV, padmode=PAD_PKCS5)
    return k.decrypt(base64.b64decode(str))


if __name__ == '__main__':
    data = "name=xx&identitycard=xx&phone=xx"
    d = Encrption(bytes(data,encoding='utf-8'))
    print("加密:",d)
    # print(Encrption("my name is").decode("utf-8"))

    print("解密:",Deode('oYPdvPaQ2GYe81S3BeuY1FfhQAbuvw/1kQ3fJFrexv4=').decode())
