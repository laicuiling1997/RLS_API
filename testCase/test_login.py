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
from tools.getYamlData import getYaml
from tools.logConfig import logInfo
log = logInfo()

#1.封装测试类

class TestLogin:
    # @pytest.mark.parametrize('inData,respData',getExcel('login','Login'))
    @pytest.mark.parametrize('inData,respData',getYaml('../data/RLS_API.yaml'))
    def test_login(self,inData,respData):
        #调用封装模块
        res = Login().login(inData,getToken=False)
        log.info("############llll##########")
        #2.断言
        try:
            assert res['code'] == respData['code']
        except Exception as err:
            print('------1----')
            log.error(err)
            raise err

if __name__ == '__main__':
    pytest.main(['test_login.py','-s'])
    # pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    # os.system('allure serve ../report/tmp')
    # TestLogin().test_login()























