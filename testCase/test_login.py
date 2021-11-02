"""
@Time ： 2021/10/25 22:50
@Auth ： 小赖a
@File ：test_login.py
@IDE ：PyCharm

"""
import pytest
import os
from lib.apiLib.login import Login
from tools.getExcel import getExcel


#1.封装测试类

class TestLogin:
    @pytest.mark.parametrize('inData,respData',getExcel('login','Login'))
    def test_login(self,inData,respData):
        #调用封装模块
        res = Login().login(inData,getToken=False)
        #2.断言
        assert res['code'] == respData['code']


if __name__ == '__main__':
    pytest.main(['test_login.py','-s'])
    # pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    # os.system('allure serve ../report/tmp')
    # TestLogin().test_login()























