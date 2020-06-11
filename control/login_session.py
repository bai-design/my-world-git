from control.config import longin_paramers, login_url, login_headers, login_status
import requests



def login_sess():
    # 保持会话
    if login_status:
        session = requests.Session()
        try:
            session.post(login_url, longin_paramers, login_headers)
        except Exception:
            print('模拟登录失败,继续执行用例')
            return
        return session
    else:
        sessions = ''
        return sessions
