import re
import time
from lib import *


# 因为在data.py中replace函数会调用lib文件下b.py文件，所以咱们data.py中引入


# 这个方法是将自定义函数计算出来,eval函数可以用过字符的方法计算出结果内容，函数嵌套函数也是可以的
def repace(data):
    # 正则匹配出 data 中所有  中的变量，返回列表 不包含这些内容则返回空
    keys = re.findall(r'<(.*?)>', data)
    print(keys)
    # 返回是个list，采用替换的方法进行数据重组
    for r in keys:
        # 第一个参数是原来的值，第二个是参数是计算出来之后得到的值
        data = data.replace('<' + r + '>', eval(r))
    return data


if __name__ == '__main__':
    parmars = "{'phone': '<b.create_phone()>', 'type': '1'}"
    print(repace(parmars))
