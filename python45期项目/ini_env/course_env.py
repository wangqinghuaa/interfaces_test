#!/usr/bin/env python
# @Time     : 2024-03-19 9:44
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : course_env.py
# @Software : PyCharm


from test_data.test_course_data import *
import requests
import time


class Course_Env:

    def __init__(self):
        self.cookies = requests.post(course_login_url, course_login_data, course_headers).cookies

    def test_env(self):
        try:
            response = requests.get(course_urls, list_course_data, headers=course_headers, cookies=self.cookies)
            ret_list = response.json()['retlist']
            ids_values = [res['id'] for res in ret_list]
            time.sleep(1)
            for ids in ids_values:
                if ids:
                    data = {"action": "delete_course", "id": ids}
                    requests.delete(course_urls, data=data, headers=course_headers, cookies=self.cookies)
                else:
                    print('删除课程请求报错啦')
        except Exception as f:
            print('初始化环境请求出错啦')
            raise f


if __name__ == '__main__':
    Course_Env().test_env()
