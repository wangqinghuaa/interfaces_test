#!/usr/bin/env python
# @Time     : 2024-03-16 18:24
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : http_request_test.py
# @Software : PyCharm

import unittest
from tools.get_cookie import GetCookie
from tools.http_requests import http_request
from ddt import ddt, data
from tools.do_excel import *
from tools.project_path import *
from tools.do_env import start_end_env

test_data = get_data(test_data_path)
# test_data = get_data(teacher_data_path)


@ddt
class TestHttpRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        start_end_env()

    @data(*test_data)
    def test_api(self, item):
        global TestResult
        response = http_request(item['url'], item['method'], eval(item['data']), getattr(GetCookie, 'COOKIE'))
        print(item['title'] + '-获取到的结果是：{}'.format(response.json()))
        if response.cookies:
            setattr(GetCookie, 'COOKIE', response.cookies)
        try:
            self.assertEqual(item['expected'], response.json()["retcode"])
            TestResult = 'PASS'
        except Exception as e:
            TestResult = 'Fail'
            print("登录异常的结果是{}".format(e))
            raise e
        finally:
            write_back(test_data_path, item['sheet_name'], item['case_id']+1, str(response.json()), TestResult)

    @classmethod
    def tearDownClass(cls) -> None:
        start_end_env()


if __name__ == '__main__':
    unittest.main()
