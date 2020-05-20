import requests
from control.log import logger
from control.data import *
import base64
from control.data import element_tojson


def http_requests(step, junit):
    # 获取到配置的头部文件数据
    element = file_element
    # 读取链接和元素表格全部内容
    excel_element = Excel('r', file_element)
    # 元素和接口转换为json，切片是为了去除表格的第一行
    e = excel_element.read()[2:3]
    elements = element_tojson(e)

    data = step['data'].replace("\n", "")
    http_type, parmars = datatating(data)
    # 记录为何不通过
    content = ''
    # 记录是否通过
    list_record = []
    if http_type == 'headers':
        httrequst = getattr(requests, sort)(step['element'], headers=eval(parmars))
    else:
        httrequst = getattr(requests, sort)(step['element'], eval(parmars))

    status = httrequst.status_code

    # 1.接口不等于200，不进行验证和断言
    if status != 200:
        logger.error('接口出错了%s' % status)
        return
    # 获得接口的返回值
    response = httrequst.json()
    expected = step['expected']
    testdot = step['testdot']

    # 如果是登录的接口，将登录的token写入文本
    if testdot in ('登录接口验证'):
        logger.info(response['data']['token'])
        writetoken(response['data']['token'])

    # 2.验证断言内容 断言只有在预期结果写了#('xxx','xxx')这种才会进行
    if '#' in step['expected']:
        # 1预期结果 2需要断言的内容 是元祖类型 ,返回：断言通过 返回'' ，反之返回不通过的字段
        is_as_pass = asset_content(expected, response)
        # 通过
        if is_as_pass == '':
            content += '断言通过'
        # 不通过
        else:
            list_record.append(1)
            content += '断言不通过%s' % is_as_pass
    # 3.验证返回值json格式
    result = iscompare_json(eval(expected), response)
    if result == 'Pass':
        content += '对比格式通过'
    else:
        list_record.append(1)
        content += 'json对比格式不通过'
    if len(list_record) >= 1:
        step['score'] = 'Fail'
        junit.failure('testdot:' + step['testdot'] + '-' + 'step:' + step['no'] + '-' + 'element:' + step[
            'element'] + '-' + ', %s' % content)
    else:
        step['score'] = 'Pass'
    step['_resultinfo'] = content
    step['output'] = response
    logger.info(step['element'])
    logger.info(response)
    return step


# 处理json类型和参数
def datatating(data):
    if data.strip():
        http_info = data.split('=', 1)
        # 获得类型
        http_type = http_info[0]
        # 获得请求的参数
        parmars = http_info[1]
    else:
        # 获得类型
        http_type = 'parmars'
        # 获得请求的参数
        parmars = "{' ': ' '}"
    return http_type, parmars


def affirm(expected):
    # 返回的是list
    ex_list = expected.split('#')
    # 0代表是预期结果，1是代表是断言的内容
    # eval处理是元祖类型
    return ex_list[0], eval(ex_list[1])
    pass


def asset_content(expected, response):
    # 处理预期结果的内容，切割出来断言
    # 1.是预期结果 2.是需要断言的内容 元祖类型
    expected, astent = affirm(expected)
    fail_tent = ''
    for t in astent:
        if t not in str(response):
            fail_tent += '接口没有此值：%s,' % t
    return fail_tent


