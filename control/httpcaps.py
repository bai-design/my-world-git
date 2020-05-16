import requests
from control.log import logger
from control.utils import iscompare_json, writetoken


def http_requests(step, junit, sort='get'):
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
    pass


def datatating():
    pass
