"""
@Time ： 2021/10/26 22:30
@Auth ： 小赖a
@File ：test_depart.py
@IDE ：PyCharm

"""
import os

import pytest
from lib.apiLib.login import Login
from tools.getExcel import getExcel
from lib.apiLib.department import departManage


class TestDepart:


    #新增部门
    @pytest.mark.departadd
    @pytest.mark.parametrize('inData,respData',getExcel('depart','Depart'))
    def test_depart_add(self,inData,respData):
        token = Login().login({'membMobile': '13227676939', 'membPassword': '123456qw', 'mercUsed': 14}, getToken=True)
        res = departManage(token).departAdd(inData)
        assert res['code'] == respData['code']

    #编辑部门
    @pytest.mark.parametrize('inData,respData',getExcel('depart','Update'))
    def test_depart_updata(self,inData,respData,departId):
        res = departManage(departId[0]).departUpdate(inData,departId[1],'1112')
        assert res['code'] == respData['code']





if __name__ == '__main__':
    #删除pytest在../report/tmp生成的数据
    # for i in os.listdir('../report/tmp'):
    #     if 'json' in i:
    #         os.remove(f'../report/tmp/{i}')
    pytest.main(['-s','-m','departadd', 'test_depart.py'])
    # data = {'depaId': '', 'depaName': '新锐三部', 'depaLinkman': '', 'depaLinkphone': '', 'depaFax': '', 'depaRemark': ''}







