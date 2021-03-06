from control.autotest import Autotest
import os
from datetime import datetime
# 开始时间
start_se_time = datetime.now()
# 兼容后期格式，是接口自动化还是web自动化app自动化，数据库，小程序 h5等自动化测试，以接口为主
desired_caps = {'genre': 'api'}
autotest = Autotest(desired_caps)
# 执行测试
autotest.play()
# dd报警
# autotest.alarm()

# 生成allure测试报告
# 参考资料 生成xml报告形式：https://llg.cubic.org/docs/junit/
try:
    os.system('mv /usr/local/sln-pro/my-world-git/control/junit/*.xml /usr/local/sln-pro/jenkins/workspace/my-world-git/allure-results/')
except BaseException:
    print('allure测试报告没有在指定目录生成')
# 发送测试报告到邮箱
autotest.sendmail()
# 结束时间
end_se_time = datetime.now()
# 执行时间
print(end_se_time - start_se_time)
