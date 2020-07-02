#1、一行代码实现1--100之和
sums = sum(range(1,101))
print(sums)
#2、如何在一个函数内部修改全局变量
def f():
    global a
#    a = 2
    b = 3
    return a+b

a = 3
c = f()
print(str(c))

#3、列出5个python标准库
import os
import sys
import datetime
import re
import math
#4、字典如何删除键和合并两个字典
dicts = {1:'白',2:'玉'}
dicts_0 ={3:'孙',4:'华'}

dicts.update(dicts_0)
print(dicts)
del dicts[4]
print(dicts)
#5、谈下python的GIL

#6、python实现列表去重的方法
mm = [1,1,2,3,5,5,3,1,2,6]
print(list(set(mm)))
print(list(dict.fromkeys(mm).keys()))
mms = []
for i in mm:
    if i not in mms:
        mms.append(i)
print(mms)
#7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
#8、python2和python3的range(100)的区别
#9、一句话解释什么样的语言能够用装饰器?
#10、python内建数据类型有哪些
int #整型
str #字符串
dict #字典
list #列表
bool #布尔
tuple #元组
#11、简述面向对象中__new__和__init__区别
#12、简述with方法打开处理文件帮我我们做了什么？
f_object = open('/usr/local/sln-pro/my-world-git/requierments.txt','r')
try:
    c = f_object.readlines()
except Exception as e:
    print(e)
else:
    print(c)
finally:
    f_object.close()


#13、列表[1,2,3,4,5]，请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]？
list_map = list(map(lambda x:x*x,range(1,6)))
list_map_0 = [i for i in list_map if i >= 10]
print(list_map)
print(list_map_0)

#14、python中生成随机整数、随机小数、0--1之间小数方法
import random
ran_int = random.randint(0,9999999)
ran_int_float = random.uniform(1,100)
ran_float = random.random()
print(ran_int)
print(ran_int_float)
print(ran_float)
#15、避免转义给字符串加哪个字母表示原始字符串？
# 避免转移字符：r
re_values = re.compile(r'[a-zA-Z0-9]')
vaues = '514616您好IOw'

str_re =re_values.findall(vaues)
re_vlues_0 = [i for i in vaues if i not in str_re]
print(''.join(re_vlues_0))

re_vlues_1 = re.sub(re_values,'',vaues)
print(''.join(re_vlues_1).strip())

#16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的。
values = '<div class="nam">中国</div>'
re_tags = re.findall(r'<div class=".*">(.*?)</div>', values)
re_tags_0 = re.search(r'<div class=".*">(.*?)</div>', values)
re_tags_1 = re.split(r'<div class=".*">(.*?)</div>', values)
print(re_tags)
print(re_tags_0.group(1))
print(''.join(re_tags_1).strip())
#17、python中断言方法举例
#assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错。
# a = 2
# assert a == 2, 'Fail a <> 2'
# assert a == 1, 'Fail a <> 1'
# #18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# import cx_Oracle
# dsn = cx_Oracle.makedsn()
# conect = cx_Oracle.connect()
# cursor = conect.cursor()
# sql = 'select distinct name from student'
# cursor.excute(sql)
# cursor.close()
# conect.close()
#19、10个Linux常用命令
#ls,vi,cd,cat,rm,mkdir,mv,more,less,head,pwd,grep,echo,cp
#20、python2和python3区别？列举5个
#21、列出python中可变数据类型和不可变数据类型，并简述原理
a1 = 100
a2 = 100
a3 = 101
a4 = [100, 101,102]
print(id(a4))
a5 = [100, 101,102]
print(id(a5))
a5[0]=99
print(id(a5))
a5.append(103)
print(id(a5))
#22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = 'ajldjlajfdljfddd'
s0 = list(set(s))
s0.sort(reverse=False)
print(''.join(s0))
#23、用lambda函数实现两个数相乘
sum = lambda x,y:x*y
print(sum(2,3))
#24、字典根据键从小到大排序
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
lis = sorted(dic.items(),key = lambda i:i[0], reverse=False)
lis_dict = dict(lis)
print(lis)
print(lis_dict)

dic_0 = {}
for key in sorted(dic.keys(),reverse=False):
    dic_0[key]=dic[key]
print(dic_0)

#25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
counts = Counter("kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h")
print(counts)

#26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
res = re.compile(r'[a-zA-Z0-9]')
a = "not 404 found 张三 99 深圳"
a0 = res.sub('',a)
print(a0.strip())

#27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def ff(n):
    return n%2 == 1
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a0 = filter(ff,a)
a1 = [i for i in a0]
print(a1)

#28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a0 = [i for i in a if i % 2 == 1]
print(a0)

#29、正则re.complie作用
#re.compile是将正则表达式编译成一个对象，加快速度，并重复使用。

#30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
#tuple int str
#31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
a = [1,5,7,9]
b = [2,2,6,8]
a.extend(b)
a.sort(reverse=False)
print(a)
#32、用python删除文件和用linux命令删除文件方法
#python删除文件 os.remove()
#inux命令删除文件 rm
#33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”，顺便把星期的代码也贴上。
import datetime
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
now_week = datetime.datetime.now().isoweekday()
total_time = str(now_time) + ' 星期:' + str(now_week)
print(total_time)
#34、数据库优化查询方法
#35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
from matplotlib import pyplot
import pygal

link_x = [i for i in range(10)]
link_y = [2 * i - 1 for i in link_x]
pyplot.scatter(link_x, link_y, c='red', edgecolor='blue',s=10)
pyplot.show()

bar = pygal.Bar()
bar.x_labels = [1,2,3,4,5,6]
squres= [1,4,9,16,25,36]
bar.x_title = 'Result'
bar.y_title = 'Squres of Result'
bar.add('squres',squres)
bar.render_to_file('./squers.svg')

#36、写一段自定义异常代码

def fn(n):
    try:
        if n > 10:
            raise Exception('n > 10')
    except Exception as e:
        print(e)
    finally:
        pass
fn(11)



#37、正则表达式匹配中，（.*）和（.*?）匹配区别？
#（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配

#（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
import re
strs = '<p>hello</p><p>world</p>'
res = re.compile('<p>(.*)</p>')
res_0 = re.compile('<p>(.*?)</p>')
a = res.findall(strs)
a0 = res_0.findall(strs)
print(a)
print(a0)
#38、简述Django的orm
#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
print([j for i in a for j in i])
#40、x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
x="abc"
y="def"
z=["d","e","f"]
print(x.join(y))
print(x.join(z))
#41、举例说明异常模块中try except else finally的相关意义
#try...except...else...
#try...except...finaly...

try:
    a = 2/0
except Exception as e:
    print(e)
finally:
    print('over')

try:
    a = 2/10
except Exception as e:
    print(a)
else:
    print(a)
#42、python中交换两个数值
a = 3
b = 2
a, b = b, a
print(a)
print(b)
#43、举例说明zip()函数用法
# list, str, tuple,dict
a = [1,2,3]
b = 'xyz'
c = {'1': 'a', '2': 'b', '3': 'c'}
e = 'ab'
f = ('m','n')
print([i for i in zip(a,b,c.values())])
print([i for i in zip(a,c,e)])
print([i for i in zip(a,e,f)])

#44、a="张明 98分"，用re.sub，将98替换为100
a = "张明 98分"
re_a = re.compile(r'\d+')
re_b = re_a.sub('100', a)
print(re_b.strip())

#45、写5条常用sql语句
# create truancate drop grant revoke insert select upadate delete show
#46、a="hello"和b="你好"编码成bytes类型

a=b"hello"
b="你好"

print(a)
print(type(a))
print(b.encode())
print(type(b.encode()))

#47、[1,2,3]+[4,5,6]的结果是多少？

a = [1,2,3]+[4,5,6]
b = [1,2,3]
b.extend([4,5,6])
print(a)
print(b)
#48、提高python运行效率的方法
#49、简述mysql和redis区别
#50、遇到bug如何处理
#51、正则匹配，匹配日期2018-03-20

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

re_url = re.compile(r'dateRange=(.*?)%7C(.*?)&')
re_url_0 = re_url.findall(url)
print(re_url_0)

#52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
new_list = []
lists = [2, 3, 5, 4, 9, 6]
def get_min():
    values_min = min(lists)
    lists.remove(values_min)
    new_list.append(values_min)
    if len(lists) > 0:
        get_min()
    return new_list
print(get_min())


lists = [2, 3, 5, 4, 9, 6]
for i in range(-len(lists),-1,1):
    if lists[i] >= lists[i+1]:
        lists[i], lists[i+1] = lists[i+1], lists[i]
print(lists)


#53、写一个单列模式
class Sigletion(object):
    __instance = None
    def __new__(cls, age):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Sigletion(1)
b = Sigletion(2)
a.age = 3
print(id(a))
print(id(b))
print(b.age)

#54、保留两位小数
a="%.03f"%1.3335
print(type(a))
print(float(a))
print(round(float(a),2))
#55.求三个方法打印结果
def fn(k,v,dic={}):
    print(id(dic))
    dic[k]=v
    print(id(dic))
    print(dic)

fn("one",1)
fn("two",2)
fn("three",3,{})
#56、列出常见的状态码和意义
#57、分别从前端、后端、数据库阐述web项目的性能优化
#58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
dic={"name":"zs","age":18}
del dic["name"]
print(dic)

dic={"name":"zs","age":18}
dic.pop("name")
print(dic)

#59、列出常见MYSQL数据存储引擎
#60、计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3), ("d",4), ("e",5)]
A = zip(("a", "b", "c","d", "e"), (1, 2, 3, 4, 5))
A0 = dict(A)
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
print("A0", A0)
print([i for i in zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))])
print(A2)
print(A3)

s = dict([('a', 'b'), [1, 2], ['x', 9]])
print(s)

#61、简述同源策略
#62、简述cookie和session的区别
#63、简述多线程、多进程
#64、简述any()和all()方法
#any():只要迭代器中有一个元素为真就为真
#all():迭代器中所有的判断项返回都是真，结果才为真
a = ['abc ', '', 'xy']
print(any(a))
print(all(a))
#65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
#66、python中copy和deepcopy区别
import copy
a = 'xy'
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))

e = ['a', 'b', 'c']
f = copy.copy(e)
g = copy.deepcopy(e)
print(id(e))
print(id(f))
print(id(g))
g.append('d')
print(e)
print(f)
print(g)


h = ['a', 'b', 'c', ['m','n']]
i = copy.copy(h)
j = copy.deepcopy(h)
print(id(h))
print(id(i))
print(id(j))
h[-1].append('o')
print(h)
print(i)
print(j)
print(id(h))
print(id(i))
print(id(j))
#67、列出几种魔法方法并简要介绍用途

#68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
import sys
print(sys.argv)
#69、请将[i for i in range(3)]改成生成器
a = (i for i in range(3))
print(type(a))
#70、a = "  hehheh  ",去除收尾空格
a = "  hehheh  "
print(a.strip())
#71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
lists=[0,-1,3,-10,5,9]
new_list = sorted(lists, reverse=False)
print(new_list)
lists.sort(reverse=False)
print(lists)
#72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
new_foo = sorted(foo, key=lambda x:x ,reverse=False)
print(new_foo)
#73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小】
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
new_foo = sorted(foo, key=lambda x: (x< 0, abs(x)), reverse=False)
print(new_foo)
#74、列表嵌套字典的排序，分别根据年龄和姓名排序

foo = [{"name":"zs","age":19},{"name":"ll","age":54},

        {"name":"wa","age":17},{"name":"df","age":23}]
age_foo = sorted(foo, key=lambda x: x["age"], reverse= False)
print(age_foo)
name_foo = sorted(foo, key= lambda x:x["name"], reverse=False)
print(name_foo)

#75、列表嵌套元组，分别按字母和数字排序
foo = [["zs", 19], ["ll", 54], ["wa", 17], ["df", 23]]
num_foo = sorted(foo, key=lambda x:x[1], reverse=False)
str_foo = sorted(foo, key=lambda x:x[0], reverse=False)
print(num_foo)
print(str_foo)

#76、列表嵌套列表排序，年龄数字相同怎么办？
foo = [["zs", 19], ["ll", 54], ["wa", 19], ["df", 23]]
num_foo = sorted(foo, key=lambda x:(x[1],x[0]), reverse=False)
print(num_foo)

#77、foo="abicdfeboxyz",输出结果 "obecdfibaxyz
foo = "abicdfeboxyz"
new_foo = [i for i in foo]
begin = 0
end = len(new_foo)-1
while begin < end :
    while new_foo[begin] not in ['a', 'e', 'i', 'o', 'u']:
        begin += 1
    while new_foo[end] not in ['a', 'e', 'i', 'o', 'u']:
        end -= 1
    if begin < end:
        new_foo[begin], new_foo[end] = new_foo[end], new_foo[begin]
        begin += 1
        end -= 1
print(''.join(new_foo))
# 78.安装ssh, 接受ssh不同的可能性
# yum install sudo
# sudo yum install openssl-server
# systemctl status sshd
# systemctl start sshd
# IP  firewalld  selinux  process
# 79.九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i, j, i*j),end='\t')
    print()
#80 冒泡排序
lists = [2, 3, 5, 4, 9, 6]

for i in range(len(lists)-1):
    for j in range(len(lists)-i -1):
        if lists[j] > lists[j+1]:
            lists[j], lists[j+1] = lists[j+1], lists[j]
print(lists)

#81 根据键对字典排序
dic = {"name": "zs", "sex": "man", "city": "bj"}
new_list = sorted(dic.items(),key = lambda x:x[0], reverse=False)
new_dic = dict(new_list)
print(new_dic)
#82 根据键对字典排序
dic = {"name": "zs", "sex": "man", "city": "bj"}
new_list = [i for i in zip(dic.keys(),dic.values())]
new_dic = sorted(new_list, key = lambda x:x[0], reverse = False)
new_dic_re = dict(new_dic)
print(new_dic_re)

#83、列表推导式、字典推导式、生成器
list_a = [i for i in range(3)]
dict_a = {i:j for i,j in zip(new_dic_re.keys(),dic.values()) }
generator_a = (i for i in range(3))
print(list_a)
print(dict_a)
print(generator_a)
#84、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
s = ["a", "mnc", "wcez", "bx"]
new_s = sorted(s, key= lambda x:len(x), reverse=True)
s.sort(key=lambda x:len(x) , reverse=True)
print(new_s)
print(s)
#85、举例说明SQL注入和解决办法
#86、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
s="info:xiaoZhang 33 shandong"
new_s = re.split(r':| ', s)
print(new_s)
#87、正则匹配以163.com结尾的邮箱
email_list =["17602184275@163.com", "??@163.com", "1710448461@qq.com"]
for email in email_list:
    re_mail = re.match("[\w]{4,20}@163\.com$", email)
    if re_mail:
        print(email)
        print(re_mail.group())
#87、递归求和
def dg_sum(n):
    if n == 0 :
        sum = 0
    else:
        sum = n + dg_sum(n-1)
    return sum

print(dg_sum(10))

#88 python字典和json字符串相互转化方法
import json
dic = {"name": "zs", "sex": "man", "city": "bj"}
a0 = json.dumps(dic)
print(type(a0))
a1 = json.loads(a0)
print(type(a1))
#89、MyISAM 与 InnoDB 区别
#90、统计字符串中某字符出现次数
str ="xy x y a b a c"
count = Counter(str)
a_count = str.count("a")
print(count)
print(a_count)
#91.字符串转化大小写
str_str = 'abcDEF'
print(str_str.upper())
print(str_str.lower())
print(str_str.title())
#92.用两种方法去空格
mt = ' x y z '
list_mt = mt.split(' ')
new_mt = ''.join(list_mt)
print(new_mt)
mt = '  x y z '
list_mt = mt.replace(' ', '')
print(new_mt)
#93、正则匹配不是以4和7结尾的手机号
tels = ["17602184275", "10086", "15945538634", "15045504827"]
for tel in tels:
    re_tel = re.match('1[\d]{9}[0-3,5-6,8-9]', tel)
    if re_tel:
        print(tel)
        print(re_tel.group())
#94. 简述python引用计数机制
class Item():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __del__(self):
        print('del方法删除对象')
#创建一个Item对象，将之赋值给it变量
it = Item('鼠标',29.8)
x = it
#打印it所引用的Item对象
del x
print('----------')
del it
print('----------')

#94.int("1.4"),int(1.4)输出结果？
try:
    a = int("1.4")
except Exception as e:
    print(e)
finally:
    b = int(1.4)
    print(b)

#95.列举3条以上PEP8编码规范
#96、正则表达式匹配第一个URL
image = '<img src="https://timgsa.baidu.com/1.jpg" src="https://timgsa.baidu.com/2.jpg" src="https://timgsa.baidu.com/3.jpg" data-clicktime="1593572427791" >'
re_image = re.findall(r"https://.*?\.jpg", image)
print(re_image[0])
#97 正则匹配中文
tilte = "结果 PEP8 两行"
re_title = re.compile(r'[\u4E00-\u9FA5]+')
new_title = re_title.findall(tilte)
print(new_title)
#98、简述乐观锁和悲观锁
#99、r、r+、rb、rb+文件打开模式区别
#100、Linux命令重定向 > 和 >>
#101正则表达式匹配出<html><h1>www.itcast.cn</h1></html>

labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
re_labels = re.compile(r"<(.*?)><(.*?)>.*?</\2></\1>")
for lable in labels:
    new_label = re_labels.match(lable)
    if new_label:
        print(new_label.group(0))
#102 python传参数是传值还是传址？
#传址
def fn(n):
    n += n
    print(n)
    print(id(n))

s = 1
print(id(s))
fn(s)
print(s)
print(id(s))

c = [1, 2, 3]
print(id(c))
fn(c)
print(c)
print(id(c))
# 103 求两个列表的交集、差集、并集
a = [1, 2, 3, 4]
b = [3, 5, 3, 6]
intersection_a_b = list(set(a).intersection(set(b)))
union_a_b = list(set(a).union(set(b)))
diffrence_a_b = list(set(a).difference(set(b)))
diffrence_b_a = list(set(b).difference(set(a)))
print('{},{},{},{}'.format(intersection_a_b, union_a_b, diffrence_a_b, diffrence_b_a))
# 104生成0-100的随机数
from numpy.random import rand, randn, random, randint,choice

num_0 = rand(5) * 100
num_1 = randint(101, size=5)
num_2 = random(5)
print(num_0)
print(num_1)
print(num_2)
#105 lambda匿名函数好处
a = ["a", "b", "c" ,"", "x", "y", "z"]
res = list(map(lambda x:"hello" if x =="" else x, a))
print(res)
#106、常见的网络传输协议
# TCP UDP
#107 单引号、双引号、三引号用法
#108 HTTP请求中get和post区别
# python中读取Excel文件的方法
#xlsx
import openpyxl
book = openpyxl.load_workbook("/usr/local/sln-pro/my-world-git/element/elements.xlsx")
sheet_names = book.sheetnames
work_sheet = book[sheet_names[0]]
if work_sheet.rows:
    for row in work_sheet.rows:
        for cell in row:
            print(cell.value, '\t', end='')
        print()

#xls
import xlrd
book = xlrd.open_workbook("/usr/local/sln-pro/my-world-git/element/elements.xlsx")
sheet_names = book.sheet_names()
sheet = book.sheet_by_index(0)
m = sheet.nrows
n = sheet.ncols
for i in range(m):
    print(sheet.row_values(i))
#csv
import csv
file_object = open("./1.csv", 'r', encoding='gbk')
rows = csv.reader(file_object)
#rows = csv.DictReader(file_object)
for row in rows:
    print(row)
a = ["a", "b", "c", "d"]
#headers =[]
file_objects = open("./1.csv", 'a+', encoding='gbk')
new_rows = csv.writer(file_objects)
#new_rows = csv.DictWriter(file_objects, headers)
#new_rows.writeheader()
new_rows.writerow(a)

#109、简述多线程、多进程
#110、python正则中search和match
