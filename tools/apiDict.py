"""
@Time ： 2021/10/26 21:39
@Auth ： 小赖a
@File ：apiDict.py
@IDE ：PyCharm

"""

API = {
    #登录注册
    'member' : {
        'login' : '/communal/user/rlsAcLogin'
    },
    
    #部门url
    'depart' : {
        'departList' : '/rls/rlsSys/department/queryPage',
        'departAdd' : '/rls/rlsSys/department/add',
        'departUpdate':'/rls/rlsSys/department/update'
    }


}



