# -*- coding: utf-8 -*-
import yaml
def getYaml(failDir):
    resList = []
    #1.打开yaml文件
    fo = open(failDir,'r',encoding='utf-8')
    #2.使用第三方库去获取
    res = yaml.load_all(fo,Loader=yaml.Loader)
    # print(type(res))
    for i in res:
        for j in i:
            resList.append((j['data'],j['resp']))
            # print(j)
    return resList
if __name__ == '__main__':
    # getYaml('../data/RLS_API.yaml')
    print(getYaml('../data/RLS_API.yaml'))
    # getYaml('../configs/conf.yaml')

