import re
import time
from control.config import header, report_header, header_custom, file_element
from control.lib import *
from control.log import logger
from control.utils import Excel
from pathlib import Path
import re
import operator

var = []


# 这个方法是将自定义函数计算出来,eval函数可以用过字符的方法计算出结果内容，函数嵌套函数也是可以的
def repace(data):
    # 正则匹配出 data 中所有  中的变量，返回列表 不包含这些内容则返回空
    keys = re.findall(r'<(.*?)>', data)
    print(keys)
    # 返回是个list，采用替换的方法进行数据重组
    for r in keys:
        # 第一个参数是原来的值，第二个是参数是计算出来之后得到的值
        data = data.replace('<' + r + '>', eval(r))
    data = data.replace("\n", "")
    return data


def suite2data(data):
    """进行测试报告同步头部标题和内容对应"""
    result = [[header_custom[key.lower()]] for key in report_header.values()]
    for d in data:
        s = d['step'][0]
        testcase = [d.get('id', 'id'), d.get('title', 'title'), d.get('testdot', 'testdot'), s.get('no', 'no'),
                    s.get('_keyword', '_keyword'), s.get('page', 'page'), s.get('_element', '_element'),
                    s.get('data', 'data'),
                    s.get('output', 'output'),
                    s.get('expected', 'expected'), s.get('assert', 'assert'), d.get('designer', 'designer'),
                    s.get('score', 'score'),
                    s.get('_resultinfo', '')]
        result.append(testcase)

        for s in d['step'][1:]:
            step = ['', '', s.get('testdot', 'testdot'), s.get('no', 'no'), s.get('_keyword', '_keyword'),
                    s.get('page', 'page'), s.get('_element', '_element'), s.get('data', 'data'),
                    s.get('output', 'output'),
                    s.get('expected', 'expected'), s.get('assert', 'assert'),
                    d.get('designer', 'designer'), s.get('score', 'score'), s.get('_resultinfo', '_resultinfo')]
            result.append(step)
    return result


def gettime():
    nowtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    return nowtime


# 处理json类型和参数
def datatating(data):
    d = {}
    if str(data).strip():
        http_ifo = data.split("..", 1)
        for h in http_ifo:
            s = str(h).split("==")
            d[str(s[0])] = s[1]
    return d


# 断言校验
def asset_content(ec_assert, response):
    fail_tent = ''
    for t in eval(ec_assert):
        if t in str(response):
            fail_tent += '接口没有此值：%s,' % t
    return fail_tent


def datatodict(data):
    head = []
    list_dict_data = []
    for d in data[1]:
        # 获取到英文的头部内容如果为中文，则替换成英文 进行改成一个k
        # 传入两个参数的作用是 查到则返回查到的数据查不到则返回传入的原数据
        d = header.get(d, d)
        # 将去除的头部英文装进list中
        head.append(d)
    # 获取到数据进行切片处理，0坐标为标题，1坐标是头部
    for b in data[2:]:
        # 头部和内容拼接为json串
        dict_data = {}
        for i in range(len(head)):
            # 之所以判断类型，如果不进行判断会出现str的错误，strip去除空格也有转str的用法
            if isinstance(b[i], str):
                dict_data[head[i]] = b[i].strip()
            else:
                dict_data[head[i]] = b[i]
        # list里面是字典格式
        list_dict_data.append(dict_data)
    return list_dict_data


# dict格式的数据处理为测试套件格式
def suite_format(data):
    element = file_element
    # 读取链接和元素表格全部内容
    excel_element = Excel('r', element)
    # 元素和接口转换为json，切片是为了去除表格的第一行
    elements = element_tojson(excel_element.read()[2:])
    # 用例套件list
    testsuite = []
    # 每个用例的testcase
    testcase = {}
    # 得到用例的所有数据
    # 循环遍历判断里面是不是一组用例生成用例集
    for d in data:
        # 判断用例有没有标题，没有标题则认为是统一用例，有标题则认为是第二条第三条用例依次类推
        if d["id"].strip():
            # 判断是否为空 true false
            if testcase:
                # 不为空则只认为用例直接添加到list里面
                testsuite.append(testcase)
                # 讲testcase置空
                testcase = {}
            # 这里生成了用例的标题行，里面没有step
            for key in ("id", "title", "condition", "testdot", "designer", "remark"):
                # test[key] 为id等值，d[key]为内容值
                testcase[key] = d[key]
            # 添加steps字段，并设置为list
            testcase["steps"] = []
        no = str(d["step"]).strip()
        # 查看是否存在步骤
        if no:
            step = {}
            # 等于当前步骤
            step['no'] = str(int(d['step']))
            #     去除这些对应的内容放入step里面
            for key in ('testdot', 'keyword', 'element', 'data', 'expected', 'assert', 'output', 'score', 'remark'):
                # 是element直接添加类型
                if key == 'element':
                    # 里面装载 请求的类型 和url 字典格式
                    step[key] = {'type': elements[d.get(key, "")]["type"],
                                 "url": elements["baseurl"]["url"] + elements[d.get(key, "")]["url"]}
                else:
                    # 获取用例内容字段进行拼接
                    step[key] = d.get(key, "")

            # 仅作为测试结果输出时，保持原样
            for v in ('keyword', 'element', 'data', 'expected', 'assert'):
                step["_{}".format(v)] = d[v]

            step["resultinfo"] = ""
        # 添加测试步骤
        testcase['steps'].append(step)
    # 将最后一条用例加入测试套件
    if testcase:
        testsuite.append(testcase)
    # 打印日志
    logger.info(testsuite)
    return testsuite


# 将元素和链接表处理为json格式方便进行查询
def element_tojson(element):
    # 推导式写法
    return {str(e[0]).replace("\n", ""): {"type": e[1], "url": e[2]} for e in element}


# 写入token
def writetoken(token):
    path = Path('/usr/local/sln-pro/my-world-git/control/book') / ('txt_final.txt')
    # 方法可以写入token和普通常量
    f = open(path, 'a')
    f.write(token)
    f.close()


# 获取接口返回值的格式，在httpcaps.py中进行调用
def compare_key_value(json_p):
    list_key = []

    def getkey_value_all(input_json={}):
        # 函数来判断一个对象是否是一个已知的类型
        if isinstance(input_json, dict):
            # keys() 函数以列表返回一个字典所有的键。
            for key in input_json.keys():
                # get() 函数返回指定键的值，如果值不在字典中返回默认值。
                key_value = input_json.get(key)
                # dict字典
                if isinstance(key_value, dict):

                    getkey_value_all(key_value)

                elif isinstance(key_value, list):

                    for json_array in key_value:
                        getkey_value_all(json_array)
                else:
                    # 对象下面的key
                    list_key.append(str(key))
                    pass
            # 对象类型的key
            list_key.append(str(key))
        elif isinstance(input_json, list):
            for input_json_array in input_json:
                getkey_value_all(input_json_array)

    getkey_value_all(json_p)
    return list_key


# 对比两个json的函数

def iscompare_json(sub, parent):
    # 将json内容传入获取key值
    a1 = compare_key_value(sub)
    print(a1)
    a2 = compare_key_value(parent)
    print(a2)
    # 两个key值进行对比
    flag = operator.eq(a1, a2)
    # 一致则通过
    if flag == True:
        return 'Pass'
    # 不通过
    else:
        return 'Fail'


def rplaceto_tf(e, r):
    e = eval(str(e).replace("true", "True").replace("fail", "Fail").replace("null", "None"))
    r = eval(str(r).replace("true", "True").replace("fail", "Fail").replace("null", "None"))
    return e, r


def acquire(last_content, this_content, all_content):
    """ 第一个参数：上个接口的返回值
        第二个参数：当前接口的请求测试数据
        用来替换测试数据，关联上一个步骤
        如果当前content里面没有^这个符号，则直接返回不走下面的方法

        从上个接口里面去拿值，拿不到就去整个用例里面去拿 """

    # 使用正则去里面寻找带^特殊符号开头的内容
    pattern = re.compile(r"'\^([\s\S]+?)'")
    # 拿到匹配的内容 是上个接口的key值
    keys = re.findall(pattern, str(this_content))
    if len(keys) == 0:
        return this_content
    # 承载当前匹配出来的内容
    present = []
    # 拿着这个key 去上个接口里面得到想要的内容
    for key in keys:
        regex = r"'%s': '([\s\S]+?)'" % key
        # last_content是上个接口的内容 进行提取出来想要的内容
        match_obj = re.findall(regex, str(last_content))
        # 每次匹配出来内容都进行遍历装进list中
        for m in match_obj:
            present.append(m)
    # 从index 0开始  根据原值内容 直接进行替换，然后直接返回
    for i in range(0,len(present)):
        # keys[i]是原来的值  present是获取的值 最后将特殊符号处理掉
        this_content = str(this_content).replace(keys[i], present[i]).replace("^", "")
    return this_content


