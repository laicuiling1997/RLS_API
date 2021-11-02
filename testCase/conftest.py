# -*- coding: utf-8 -*-
from sqlite3 import connect

import pytest

from lib.apiLib.department import departManage
from lib.apiLib.login import Login


@pytest.fixture(scope='class',autouse=True)
def setup(request):
    print('----开始执行测试用例----')




    def fin():
        print('----测试用例执行完成----')
    #相比yield,request.addfinalizer 会更好
    #当测试用例出现问题时，yield后面的teardown将不会被执行，而addfinalizer的teardown会被执行
    request.addfinalizer(fin)

#获取部门id
@pytest.fixture(scope='function')
def departId():
    token = Login().login({'membMobile': '13227676939', 'membPassword': '123456qw', 'mercUsed': 14}, getToken=True)
    res = departManage(token).departList({'pageIndex': '1','pageSize': '20','depaName':None})
    depAdd = departManage(token).departAdd({'depaName': '新锐部2323'})
    return token,res,depAdd





