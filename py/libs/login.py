
from configs.config import HOST   #环境参数导入
import requests
# import hashlib               #hashlib（自带库 不需要导入）
# def  get_md5(a):
#     # 实例化一个md5 对象
#      md5= hashlib.md5()
#     # 调用加密的方法直接加密
#     md5.updata(a.encode(''))
#       return md5.hexdigest()             返回一个加密的结果



# 封装登录的一个类
class Login:
    def login(self,inData,mode=True):             #登录方法
        #url 地址
        url= f'{HOST}/index.html#/odc/login'        #f=传参的方法
        # 传递参数
        payload=inData
        # 请求
        resp = requests.post(url,json=payload)     #resp=覆盖请求对象
        if mode:     #获取token
            return resp.json() ["token"]     #返回是字典形式
        else:     #获取相应数据
            return resp.json()          #返回是字典形式
import pprint          #引入完美打印模块

        # 查看响应
        # return resp.text()

if __name__ == '__main__':
    res=Login().login({"username":"caishu","password":"CCcc@@88"})
    print(res)
    pprint.pprint(res)



