#!/usr/bin/env python
# @Time     : 2024-03-19 17:48
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : course_case.py
# @Software : PyCharm
import unittest
import requests
from ini_env.course_env import Course_Env
from test_data.test_course_data import *
from tools.my_logs import MyLogging
my_logger = MyLogging()
ids = None


class Course_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.cookies = requests.post(course_login_url, course_login_data, course_headers).cookies

    @classmethod
    def setUpClass(cls) -> None:
        Course_Env().env()

    def test_01_add_course(self):
        response = requests.post(course_urls, add_course_data, course_headers, cookies=self.cookies)
        print('添加课程-获取到的结果是：{}'.format(response.json()))
        my_logger.info('添加课程-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
        except Exception as e:
            my_logger.info('添加课程异常的结果是：{}'.format(e))
            raise e

    def test_02_list_course(self):
        global ids
        response = requests.get(course_urls, list_course_data, headers=course_headers, cookies=self.cookies)
        print('列出课程-获取到的结果是：{}'.format(response.json()))
        my_logger.info('列出课程-获取到的结果是：{}'.format(response.json()))
        ids = response.json()['retlist'][0]['id']
        try:
            self.assertEqual(0, response.json()["retcode"])
            self.assertIn('初中地理', response.json()['retlist'][0].values())
            self.assertLess(1180, response.json()['retlist'][0]['id'])
        except Exception as e:
            my_logger.info('列出课程异常的结果是：{}'.format(e))
            raise e
        return ids

    def test_03_put_course(self):
        global ids
        put_course_data = {'action': 'modify_course', 'id': ids, 'newdata': '''{"name":"初中化学","desc":"初中化学课程","display_idx":1}'''}
        response = requests.put(course_urls, put_course_data, headers=course_headers, cookies=self.cookies)
        print('修改课程-获取到的结果是：{}'.format(response.json()))
        my_logger.info('修改课程-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
        except Exception as e:
            my_logger.info('修改课程异常的结果是：{}'.format(e))
            raise e

    def test_04_del_course(self):
        global ids
        del_course_data = {'action': 'delete_course', 'id': ids}
        response = requests.delete(url=course_urls, data=del_course_data, headers=course_headers, cookies=self.cookies)
        print('删除课程-获取到的结果是：{}'.format(response.json()))
        my_logger.info('删除课程-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
        except Exception as e:
            my_logger.info('删除课程异常的结果是：{}'.format(e))
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        Course_Env().env()


if __name__ == '__main__':
    unittest.main()
