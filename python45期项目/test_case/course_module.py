#!/usr/bin/env python
# @Time     : 2024-03-17 21:23
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : course_module.py
# @Software : PyCharm


import unittest
import requests


from tools.http_requests import http_request
from ddt import ddt, data
from tools.project_path import *
from ini_env.course_env import Course_Env
from do_excel.do_course_module import Do_Course


course_data = Do_Course.get_data(course_case_path)


@ddt
class Course_Test(unittest.TestCase):

    def __init__(self, methodName):
        super(Course_Test, self).__init__(methodName)
        self.url = "http://localhost:8087/api/mgr/loginReq"
        self.data = {"username": "auto", "password": "sdfsdfsdf"}
        self.response = requests.post(self.url, self.data).cookies

    @classmethod
    def setUpClass(cls) -> None:
        Course_Env().env()

    @data(*course_data)
    def test_course(self, item):
        global TestResult
        response = http_request(item['url'], item['method'], eval(item['data']), cookie=self.response)
        print(item['title'] + '-获取到的结果是：{}'.format(response.json()))
        # if response.json()["id"] > 100:
        #     print('OK')
        try:
            self.assertEqual(item['expected'], response.json()["retcode"])
            TestResult = 'PASS'
        except Exception as e:
            TestResult = 'Fail'
            print("登录异常的结果是{}".format(e))
            raise e
        finally:
            Do_Course.write_back(course_case_path, item['sheet_name'], item['case_id']+1, str(response.json()), TestResult)

    @classmethod
    def tearDownClass(cls) -> None:
        Course_Env().env()


if __name__ == '__main__':
    unittest.main()
