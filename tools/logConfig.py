# # -*- coding: utf-8 -*-
# """
# @Time ： 2021/11/7 2:44 下午
# @Auth ： 小赖a
# @File ：logConfig.py
#
# """
# import logging
# import datetime
#
# def logInfo():
#     logging.basicConfig(
#         #输出指定的格式，还有很多其他信息可以选择
#         format="%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s",
#         #设置指定文件名
#         filename = f'../logs/{datetime.datetime.now().strftime("%y_%m_%d_%H.%M.%S")}.txt',
#         level = logging.INFO,
#         filemode='a'
#
#     )
#
#     return logging
#
# if __name__ == '__main__':
#     log = logInfo()
#     log.debug("---info---")
#
#
#
#
import logging
import datetime
def logInfo(name=__name__):
    #1- 日志的名称：  路径+名字(进程/日期)+后缀名
    logname = f"../logs/{datetime.datetime.now().strftime('%Y%m%d%H%M')}.log"
    #2- 创建日志对象
    loggerObject = logging.getLogger(name)#
    #3- 日志级别
    loggerObject.setLevel(logging.INFO)
    #4- 日志文件的属性
    rHandler = logging.FileHandler(logname,mode='a',encoding="utf-8")
    #5- 日志内容的格式
    #2021-01-20 17:29:44,688 INFO o.a.j.u.JMeterUtils: Setting Locale
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]: %(message)s ")
    rHandler.setFormatter(formatter)
    loggerObject.addHandler(rHandler)
    return loggerObject#返回日志对象

if __name__ == '__main__':
    # log = logger()
    pass