# -*- coding:utf-8 -*-
"""
@author:YCW
@file:login_process_request.py
@time:2020/10/814:10
"""
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent' : ua.random,
    'Referer' : 'https://processon.com'
}

s = requests.Session()

login_url = 'https://processon.com/login'
form_data = {
    'login_email' : '',
    'login_password' : ''
}

pre_login = 'https://processon.com/login?f=index'
pre_resp = s.get(pre_login, headers = headers)

respone = s.post(login_url, data=form_data, headers = headers, cookies=s.cookies)
print(respone.status_code)