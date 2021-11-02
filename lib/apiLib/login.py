# -*- coding: utf-8 -*-

import requests,hashlib
from configs.config import HOST
from tools.apiDict import API


def get_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    #获取加密内容
    return md5.hexdigest()

class Login:
    def login(self,inData,getToken=True):
        MEMBER = API['member']['login']
        url = f'{HOST}{MEMBER}'
        # inData['membPassword'] = get_md5(inData['membPassword'])
        payload = inData

        resp = requests.post(url=url, data=payload)

        if getToken == True:
            return resp.json()['data']['token']
        else:
            return resp.json()


if __name__ == '__main__':

    data = {'membMobile': '13227676939', 'membPassword': '123456qw', 'mercUsed': 14}
    # print(type(data))
    a = Login().login(data,getToken=False)
    print(a)
