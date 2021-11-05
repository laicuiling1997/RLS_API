"""
@Time ： 2021/10/23 22:39
@Auth ： 小赖a
@File ：getExcel.py
@IDE ：PyCharm

"""


import xlrd
from xlutils.copy import copy
import json


def getExcel(sheetname,casename):
    resList = []
    #获取用例地址
    excelDir = '../data/RLS_API.xls'

    #打开excel对象，保持格式
    workBook = xlrd.open_workbook(filename=excelDir)

    #获取sheetname
    sheetName = workBook.sheet_by_name(sheetname)

    #获取行数，列数
    # rows = sheetName.nrows
    # cols = sheetName.ncols

    idx = 0
    #读取单元格--返回是字符串，cell(row,col),从0开始
    for one in sheetName.col_values(0): #返回由该列中所有单元格的数据组成的列表
        if casename in one:
            reqBodyData = sheetName.cell(idx,9).value
            respData = sheetName.cell(idx,11).value
            resList.append((json.loads(reqBodyData),json.loads(respData)))
        idx += 1
    return resList



def set_execelData():
    # 获取用例地址
    excelDir = '../data/RLS_API.xlsx'

    # 打开excel对象，保持格式
    workBook = xlrd.open_workbook(filename=excelDir)

    #复制workBook
    workBookNew = copy(workBook)
    workSheetNew = workBookNew.get_sheet(0)
    return workBookNew,workSheetNew




if __name__ == '__main__':
    # print(getExcel('login','Login'))
    for one in getExcel('depart','Depart'):
        print(one)
    # set_execelData()
















