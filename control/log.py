import logging
import datetime
from pathlib import Path
import sys


def mkdir(p):
    path = Path('/usr/local/sln-pro/my-world-git/control/' + p)
    # 如果文件不存在 则创建
    if not path.is_dir():
        path.mkdir()


# 获得当前的时间
def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')


# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger()
# 指定logger输出格式
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(filename)s line:%(lineno)d: %(message)s')

# 创建log文件夹
mkdir('log')

# 文件日志
log_file = str(Path('/usr/local/sln-pro/my-world-git/control/log') / '{}.log'.format(today()))
file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8', delay=False)
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值
#console_handler.setFormatter(formatter)

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
# DEBUG，INFO，WARNING，ERROR，CRITICAL
logger.setLevel(logging.INFO)
