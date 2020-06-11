import requests
from requests.utils import dict_from_cookiejar
res = requests.Session()
url = 'http://www.renren.com/ajaxLogin/login/'
data = {"captcha_type":"web_login",
"domain":"renren.com",
"email":"17602184275",
"f": "http%3A%2F%2Fwww.renren.com%2F974578049",
"icode":"",
"key_id": "1",
"origURL":"http://www.renren.com/home",
"password":"10d98194810bc3851ea2c4c534d5611c229f7180d0b5004a4ca5d1ce4e78b4ef",
"rkey":"b963b069bb667305dcf6142cf37c73b5"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
reseponse = res.post(url=url, headers=headers, data=data)
url_00 = 'http://www.renren.com/974578049/profile'
url_01 ='http://webpager.renren.com/api/ime.jsp'

reseponse_00 = res.get(url_01)
cookies = dict_from_cookiejar(reseponse.cookies)
print(cookies)

