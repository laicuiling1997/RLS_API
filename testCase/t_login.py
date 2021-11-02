"""
@Time ： 2021/10/24 17:13
@Auth ： 小赖a
@File ：t_login.py
@IDE ：PyCharm

"""


import json
#1.读取数据
from tools.getExcel import getExcel,set_execelData
dataList = getExcel('login','Login')
#2.关联请求
from lib.apiLib.login import Login
workBookNew,workSheetNew = set_execelData() #元组


#元组 -- （请求body,响应数据）
for one in dataList:
 #字符串转字典（login中的data需要传dict）
    # print(type(loginData))
    res = Login().login(one[0],False)  #实际响应结果
    #预期与实际的响应数据进行比较
    if res['code'] == one[1]['code']:
        print('====pass===')
        workSheetNew.write(dataList.index(one),12,'pass')  #(行号，列号，字符串内容)
    else:
        print('===fail===')
        workSheetNew.write(dataList.index(one), 12,'fail')
workBookNew.save('../data/RLS_API_NEW.xls')