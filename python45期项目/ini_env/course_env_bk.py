#!/usr/bin/env python
# @Time     : 2024-03-19 9:44
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : course_env.py
# @Software : PyCharm
import unittest

from test_data.test_course_data import *
import requests
import time


class Course_Env:

    def __init__(self):
        self.url = "http://localhost:8087/api/mgr/loginReq"
        self.data = {"username": "auto", "password": "sdfsdfsdf"}
        self.list_del = 'http://localhost:8087/api/mgr/sq_mgr/'
        # 公司一般都会加一些校验机制-比如请求头、Referer等等
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                        'Content-Type': 'application/x-www-form-urlencoded'}

    def test_env(self):
        try:
            cookies = requests.post(url=self.url, data=self.data, headers=self.headers).cookies
            params = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}
            list_response = requests.get(url=self.list_del, params=params, cookies=cookies)
            response = list_response.json()['retlist']
            ids_values = [res['id'] for res in response]
            time.sleep(2)
            for ids in ids_values:
                if ids:
                    data = {"action": "delete_course", "id": {ids}}
                    requests.delete(self.list_del, data=data, cookies=cookies)
                else:
                    print('删除课程请求报错啦')
        except Exception as f:
            print('初始化环境请求出错啦')
            raise f
        time.sleep(1)


if __name__ == '__main__':
    Course_Env().test_env()
