#!/usr/bin/env python
# @Time     : 2024-03-19 10:20
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : teacher_env.py
# @Software : PyCharm

from test_data.test_teacher_data import *
from ini_env.course_env import Course_Env
import requests

import time


class Teacher_Env(Course_Env):

    Course_Env().test_env()

    def test_env(self):
        try:
            response = requests.get(teacher_urls, params=teacher_list_data, headers=teacher_headers,
                                    cookies=self.cookies)
            ret_list = response.json()['retlist']
            ids_values = [res['id'] for res in ret_list]
            time.sleep(1)
            for ids in ids_values:
                if ids:
                    data = {"action": "delete_teacher", "id": ids}
                    requests.delete(url=teacher_urls, data=data, headers=teacher_headers, cookies=self.cookies)
                else:
                    print('删除老师请求报错啦')
        except Exception as f:
            print('初始化环境请求出错啦')
            raise f


if __name__ == '__main__':
    Teacher_Env().test_env()
