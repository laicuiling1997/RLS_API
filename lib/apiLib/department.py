"""
@Time ： 2021/10/26 20:42
@Auth ： 小赖a
@File ：department.py
@IDE ：PyCharm

"""
import requests
import pprint
from lib.apiLib.login import Login
from configs.config import HOST
from tools.apiDict import API

class departManage:
    def __init__(self,inToken):
        self.header = {'token':inToken}

    #查询部门列表
    def departList(self,inData):
        DEPART = API['depart']['departList']
        url = f'{HOST}{DEPART}'
        payload = inData
        resp = requests.get(url=url,headers=self.header,params=payload)
        return resp.json()['data']['list'][0]['depaId']
        # return resp.json()

    #添加部门
    def departAdd(self,inData):
        DEPARTADD = API['depart']['departAdd']
        url = f'{HOST}{DEPARTADD}'
        payload = inData
        resps = requests.post(url,data=payload,headers=self.header)
        return resps.json()

    # 编辑部门
    def departUpdate(self,inData,depaId,depaName):
        inData['depaId'] = depaId  #更新部门ID
        inData['depaName'] = depaName #更新部门名称
        DEPARTADD = API['depart']['departUpdate']
        url = f'{HOST}{DEPARTADD}'
        payload = inData
        resps = requests.post(url, data=payload, headers=self.header)
        return resps.json()


if __name__ == '__main__':
    data = {'membMobile': '13227676939', 'membPassword': '123456qw', 'mercUsed': 14}
    resp = Login().login(data)

    # res = departManage(resp).departList({'pageIndex': '1','pageSize': '20','depaName':None})
    # pprint.pprint(res)
    #
    # depAdd = departManage(resp).departAdd({'depaName':'新锐部09'})
    # pprint.pprint(depAdd)

    datas={"depaId":"","depaName":"","depaLinkman":"","depaLinkphone":"","depaFax":"","depaRemark":""}
    depupdate = departManage(resp).departUpdate(datas,'00dd9731a5d74de0bf895801b9e978ad','22')
    pprint.pprint(depupdate)




























