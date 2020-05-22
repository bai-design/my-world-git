from control.log import logger
from control.data import repace, acquire
from control import httpcaps
import threading
import time


class TestCase(object):
    _instance_lock = threading.Lock()

    def __init__(self, junit):
        self.junit = junit

        # 记录多少用例没有通过
        self.step_fail = 0
        # 记录出错的用例
        self.step_error = 0
        # 出错用例的功能点
        self.errors_detail = ''

        # 上个步骤
        self.last_step = {}

    def __new__(cls, *args, **kwargs):
        """采用单例的设计模式,指向同一地址空间"""
        if not hasattr(TestCase, "_instance"):
            with TestCase._instance_lock:
                if not hasattr(TestCase, "_instance"):
                    TestCase._instance = object.__new__(cls)
        return TestCase._instance

    #  执行测试用例
    def run(self, case):
        # 当前执行的用例
        self.case = case
        # 记录执行的用例结果，新的用例来了，就清空了
        steps = []

        for index, step in enumerate(self.case['step']):

            try:
                # 上一个步骤不为空，则进行判断是否需要接口关联
                if self.last_step:
                    # 从上个接口提取到下个接口想要的数据
                    step['data'] = acquire(str(self.last_step['output']), str(step['data']), self.case)
                    # 查看上个测试数据里面有没有这个内容
                    # 如果里面有#号，则吧测试数据重组
                    # 将测试数据进行重组，调用自定义函数 计算出结果
                if step['data']:
                    step['data'] = repace(str(step['data']))
                if '#' in str(step['data']):
                    # 只切割最后一个#
                    data_list = str(step['data']).rsplit('#', 1)
                    step['data'] = data_list[0]
                    sleep_time = data_list[1].split('=')
                    logger.info('{}'.format(sleep_time[1]))
                    time.sleep(float(sleep_time[1]))
                self.last_step = getattr(httpcaps, 'http_requests')(step, self.junit)
                if self.last_step['score']!= 'Pass':
                    self.step_fail += 1
                steps.append(self.last_step)
            except Exception as excepetion:
                # 将此用例置为不通过
                step['score'] = 'Fail'
                step['_resultinfo'] = 'exception : %s' % excepetion
                self.step_error += 1
                logger.info((step))
                self.junit.failure(
                    'testdot:' + step['testdot'] + ' - ' + 'step:' + step['no'] + ' - ' + 'element:' + step[
                        '_element'] + ' - ' + 'error:%s' % excepetion)
                self.errors_detail += step['testdot'] + '--' + '{}'.format(excepetion)
                steps.append(step)
                logger.error('error: interface and element not found%s' % excepetion)
                logger.error('error:%s' % excepetion)
                logger.info('上一条用例: ' + str(self.last_step))
            # 记录生成的测试结果，生成测试报告excel版本
            self.case['steps'] = steps
        return self.case





