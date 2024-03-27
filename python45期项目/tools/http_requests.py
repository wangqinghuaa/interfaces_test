#!/usr/bin/env python
# @Time     : 2024-03-15 17:34
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : http_requests.py
# @Software : PyCharm


import requests

# 登录
# loging_url = "http://localhost:8087/api/mgr/loginReq"
# login_data = {"username": "auto", "password": "sdfsdfsdf"}

# 列出课程
# list_url = "http://localhost:8087/api/mgr/sq_mgr/?"
# list_data = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}

# 第一种
# s = requests.session()
# login_response = s.post(url=loging_url, data=login_data)
# list_response = s.get(url=list_url, params=list_data)
# print(login_response.json())
# print(list_response.json())

# 第二种
# response_01 = requests.post(loging_url, login_data)
# print('json解析的结果是：{}'.format(response_01.json()))

# 列出课程  必选传一个cookies并且参数不能乱写
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
# response_02 = requests.get(list_url, list_data, cookies=response_01.cookies, headers=headers)
# print('text解析的结果是：{}'.format(response_02.text))  # text可以解析任意返回结果，json只能解析返回json格式
# print('json解析的结果是：{}'.format(response_02.json()))
# print('response_02的请求头是：{}'.format(response_02.request.headers))
# print(response_02.headers)
# print(response_02.status_code)

# session和cookies、token作用


def http_request(url, method, data, header=None, cookie=None):
    response = {}
    try:
        if method == 'get':
            response = requests.get(url, data, cookies=cookie)
        elif method == 'post':
            response = requests.post(url, data, cookies=cookie)
        elif method == 'delete':
            response = requests.delete(url, data, headers=header, cookies=cookie)
        elif method == 'put':
            response = requests.put(url, data, cookies=cookie)
        else:
            print('http_request方法请求参数出错了')
    except Exception as e:
        print('http_request请求报错{}'.format(e))
        raise e

    return response


if __name__ == '__main__':
    # 登录
    loging_url = "http://localhost:8087/api/mgr/loginReq"
    login_data = {"username": "auto", "password": "sdfsdfsdf"}

    # 列出课程
    list_url = "http://localhost:8087/api/mgr/sq_mgr/?"
    list_data = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}

    login01_response = http_request(loging_url, 'post', login_data)
    list01_response = http_request(list_url, 'get', list_data, cookie=login01_response.cookies)

    print(login01_response.json())
    print(list01_response.json())
