from pathlib import Path

mail_dict = {'send_user': '1659935784@qq.com',  # 发件人
             'password': 'yknmfsvzoqsgdbcc',  # 授权码
             'receive_users': '1710448461@qq.com',  # 收件人地址
             'receive_list': [],  # 收件人list地址
             'subject': 'python自动化测试报告',  # 主题
             'email_text': 'This is a report, today',  # 邮件正文
             'server_address': 'smtp.qq.com',  # 服务器地址
             'mail_type': 1
             }

header = {
    '用例编号': 'id',
    '用例标题': 'title',
    '前置条件': 'condition',
    '测试功能点': 'testdot',
    '测试步骤': 'step',
    '操作': 'keyword',
    '页面': 'page',
    '元素': 'element',
    '测试数据': 'data',
    '预期结果': 'expected',
    '断言': 'assert',
    '设计者': 'designer',
    '步骤结果': 'score',
    '备注': 'remark',
}

report_header = {
    '用例编号': 'id',
    '用例标题': 'title',
    '测试功能点': 'testdot',
    '测试步骤': 'step',
    '操作': 'keyword',
    '页面': 'page',
    '元素': 'element',
    '测试数据': 'data',
    '输出数据': 'output',
    '预期结果': 'expected',
    '断言': 'assert',
    '设计者': 'designer',
    '步骤结果': 'score',
    '备注': 'remark',
}

header_custom = {'id': '用例编号', 'title': '用例标题', 'testdot': '测试功能点', 'step': '测试步骤',
                 'keyword': '操作', 'page': '页面', 'element': '元素', 'data': '测试数据', 'expected': '预期结果', 'assert': '断言',
                 'output': '输出数据',
                 'designer': '设计者', 'score': '步骤结果',
                 'remark': '备注'}

# case的文件的路径
file_case = str(Path('/usr/local/sln-pro/my-world-git/testcase')/('testcase.xlsx'))
# element的文件的路径
file_element = str(Path('/usr/local/sln-pro/my-world-git/element')/('element.xlsx'))
# junit测试报告的路径
file_junit = str(Path('/usr/local/sln-pro/my-world-git/control/junit')/('testcase'+'-'+'junit'+'.xml'))
# excel测试报告的路径
excel_report = str(Path('/usr/local/sln-pro/my-world-git/control/report')/('testcase-report.xlsx'))
# 生成xml的测试报告
file_xml = str(Path('/usr/local/sln-pro/my-world-git/control/report')/('testcase-xml-report.xlsx'))