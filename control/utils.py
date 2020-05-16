import xlrd
import xlsxwriter
from pathlib import Path
import requests


# 操作Excel的工具类
class Excel(object):
    # 初始化方法 参数type：为r是读取excel，为w是写入excel获取不同的实例，参数file_name是将要读取的文件
    def __init__(self, type, file_name):
        # 读取excel
        if type == "r":
            # 打开文件
            self.workbook = xlrd.open_workbook(file_name)
            # 获取到所有的sheet_names,sheet1,sheet2获取到所有，获取到的是一个list
            self.sheet_names = self.workbook.sheet_names()
            # 装载所有数据的list
            self.list_data = []

        elif type == "w":
            # 获得写入excel的实例
            self.workbook = xlsxwriter.workbook(file_name)

    def read(self):
        # 根据sheet_name去读取用例，并获取文件的总行数获取到每行的内容
        for sheet_name in self.sheet_names:
            # 通过每个sheetname获取到每个页的内容
            sheet = self.workbook.sheet_by_name(sheet_name)
            # 获取总行数
            rosw = sheet.nrows
            # 根据总行数进行读取
            for i in range(0, rosw):
                revalues = sheet.row_values(i)
                # 讲每一行的内容添加进去
                self.list_data.append(revalues)
        # 将得到的excel数据返回进行处理
        return self.list_data


# 将元素和链接表处理为json格式方便进行查询
def element_to_json(element):
    elements = {}
    # 讲元素和接口等信息组成key和value的形式方便进行查询
    for e in element:
        elements[e[0]] = {"type": e[1], "url": e[2]}
    return elements


def data_to_dict(data):
    """
    1.讲excel头部替换成英文的
    2.处理成json格式
    """
    header = {
        "用例编号": "id",
        "用例标题": "title",
        "前置条件": "condition",
        "测试功能点": "testdot",
        "测试步骤": "step",
        "操作": "keyword",
        "页面": "page",
        "元素": "element",
        "测试数据": "data",
        "预期结果": "expected",
        "断言": "assert",
        "设计者": "designer",
        "步骤结果": "score",
        "备注": "remark",
    }

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
            # 取出的是测试步骤第一步第二步
        step = {}
        # 步骤里面添加control字段
        step["control"] = ""
        # 步骤
        step["no"] = str(d["step"])
        #     去除这些对应的内容放入step里面
        for key in ("testdot", "keyword", "element", "data", "expected", "output", "score", "remark"):
            # 获取用例内容字段进行拼接
            step[key] = d.get(key, "")
            # 仅作为测试结果输出时，保持原样
            # 进行的操作
        step["_keyword"] = d["keyword"]
        # 对应的key取值
        step["_element"] = d["element"]
        # 测试数据
        step["_data"] = d["data"]
        # 预期结果
        step["_expected"] = d.get("expected", "")
        # 输出结果
        step["_output"] = ""
        # 测试结果信息
        step["_resultinfo"] = ""
        # 添加测试步骤
        testcase["steps"].append(step)
    testsuite.append(testcase)
    # 返回处理好的值
    return testsuite


# 判断当前目录是否存在
def mkdir(p):
    path = Path(p)
    # 如果文件不存在 则创建
    if not path.is_dir():
        path.mkdir()


if __name__ == "__main__":

# file_name = "/usr/local/sln-pro/my-world-git/testcase/testcase.xlsx"
#    e = Excel("r", file_name)
#    list_read = e.read()
#    data = element_to_json(list_read)
#    print(data)

# test_case = "/usr/local/sln-pro/my-world-git/testcase/testcase.xlsx"
# e_case = Excel("r", test_case)
# re = e_case.read()
# data = data_to_dict(re)
# testsuite = suite_format(data)
# print(testsuite)
