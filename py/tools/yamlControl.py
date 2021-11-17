
import yaml
def get_yaml_data(fileDir):          #fileDir 打开文件路径
    #1- 读取文件操作-----从磁盘读取到内存里
    fo = open(fileDir,'r',encoding="utf-8")     #r=read读取    编码格式=encoding fo= file-Object 文件对象
    #2 - 使用yaml方法获取数据
    res = yaml.load(fo,Loader=yaml.FullLoader)
    return res

if __name__ == '__main__':
    res=get_yaml_data('../data/loginCase.yaml')      #相对路径  ../上层目录
    print(res)



