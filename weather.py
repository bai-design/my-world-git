import requests
from requests.utils import dict_from_cookiejar

def get_weath(url, parmars):
    weath = requests.Session()
    reponse = weath.post(url, parmars)
    if reponse.status_code == 200:
        print(reponse.json())
    else:
        print('acess fail')
    cookies = dict_from_cookiejar(reponse.cookies)
    return cookies

if __name__ == '__main__':
    url = 'https://apis.juhe.cn/mobile/Example/query.php'
    parmars = {'phoneNo': '15104594631'}
    cookies = get_weath(url, parmars)
    print(cookies)

