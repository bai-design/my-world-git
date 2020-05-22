import xlrd
import xlsxwriter
from pathlib import Path
import os


# 操作Excel的工具类
class Excel(object):
    # 初始化方法 参数type：为r是读取excel，为w是写入excel获取不同的实例，参数file_name是将要读取的文件
    def __init__(self, type, file_name):
        # 读取excel
        if type == 'r':
            # 打开文件
            self.workbook = xlrd.open_workbook(file_name)
            # 获取到所有的sheet_names,sheet1,sheet2获取到所有，获取到的是一个list
            self.sheet_names = self.workbook.sheet_names()
            # 装载所有数据的list
            self.list_data = []
            # 将测试数据内调用的方法，改编成自定义里面的变量
            self.dict_data = {}
        # 写入excel
        elif type == 'w':
            # 获得写入excel的实例
            self.workbook = xlsxwriter.Workbook(file_name)

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

    def write(self, data, sheet_name):
        # 设置报告格式
        sheet = self.workbook.add_worksheet(sheet_name)
        # 设置列宽
        sheet.set_column('A:Q', 15)

        cell_format = self.workbook.add_format({'blod': True})
        sheet.set_row(0, 20, cell_format)
        # 红色
        red = self.workbook.add_format({'bg_color': 'red', 'color': 'white'})
        # 绿色
        green = self.workbook.add_format({'bg_color': 'green', 'color': 'white'})

        for i in range(len(data)):
            for j in range(len(data[i])):
                # 进行用例结果的背景颜色更改 不同状态的用例 不同颜色
                if str(data[i][j]) == 'Fail':
                    sheet.write(i, j, str(data[i][j]), red)
                elif str(data[i][j]) == 'Pass':
                    sheet.write(i, j, str(data[i][j]), green)
                else:
                    sheet.write(i, j, str(data[i][j]))

    def close(self):
        self.workbook.close()



# 判断当前目录是否存在
def mkdir(p):
    path = Path(p)
    # 如果文件不存在 则创建
    if not path.is_dir():
        path.mkdir()


# 创建必备的文件夹
def creation_files():
    # 切换工作目录
    os.chdir('/usr/local/sln-pro/my-world-git/control')
    # 创建文件
    files = ('report', 'junit', 'book', 'file_pic', 'file')
    for file in files:
        mkdir(file)
    txt_path = str(Path('/usr/local/sln-pro/my-world-git/control/book') / ('txt_final.txt'))
    txt = open(txt_path, 'w')
    # seek() 方法用于移动文件读取指针到指定位置。
    txt.seek(0)
    # truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
    txt.truncate()
    txt.close()
