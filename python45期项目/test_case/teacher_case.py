#!/usr/bin/env python
# @Time     : 2024-03-19 17:48
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : course_case.py
# @Software : PyCharm
import unittest
import requests
from ini_env.teacher_env import Teacher_Env
from test_data.test_teacher_data import *
from test_data.test_course_data import *
from tools.my_logs import MyLogging
my_logger = MyLogging()

teacher_id = None


class Teacher_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.cookies = requests.post(teacher_login_url, teacher_login_data, teacher_headers).cookies
        self.course_response = requests.post(course_urls, add_course_data, headers=course_headers, cookies=self.cookies)
        self.list_response = requests.get(course_urls, list_course_data, headers=course_headers, cookies=self.cookies)
        self.ids = self.list_response.json()['retlist'][0]['id']

    @classmethod
    def setUpClass(cls) -> None:
        Teacher_Env().env_teacher()

    def test_01_add_teacher(self):
        add_data_teacher = {'action': 'add_teacher',
                            'data': '''{"username":"Toy","password":"sq888","realname":"托尼","desc":"托尼老师",
                    "courses": [{"id": %s, "name": "初中地理"}],"display_idx":1}''' % self.ids}
        response = requests.post(teacher_urls, add_data_teacher, headers=teacher_headers, cookies=self.cookies)
        print('添加老师-获取到的结果是：{}'.format(response.json()))
        my_logger.info('添加老师-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
            self.assertLess(250, response.json()['id'])
        except Exception as e:
            my_logger.info('添加老师程异常的结果是：{}'.format(e))
            raise e

    def test_02_list_teacher(self):
        global teacher_id
        response = requests.get(teacher_urls, list_teacher_data, headers=teacher_headers, cookies=self.cookies)
        teacher_id = response.json()['retlist'][0]['id']
        print('列出老师-获取到的结果是：{}'.format(response.json()))
        my_logger.info('列出老师-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
            self.assertIn('托尼', response.json()['retlist'][0]['realname'])
        except Exception as e:
            my_logger.info('列出老师程异常的结果是：{}'.format(e))
            raise e

    def test_03_put_teacher(self):
        global teacher_id
        put_data = {'action': 'modify_teacher', 'id': teacher_id,
                    'newdata': '''{"username":"Tom","courses":[],"realname":"汤姆","desc":"汤姆老师","display_idx":1,
                    "password":"sq888"}'''}
        response = requests.put(teacher_urls, put_data, headers=teacher_headers, cookies=self.cookies)
        print('修改老师-获取到的结果是：{}'.format(response.json()))
        my_logger.info('修改老师-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
        except Exception as e:
            my_logger.info('修改老师程异常的结果是：{}'.format(e))
            raise e

    def test_04_del_teacher(self):
        global teacher_id
        data = {'action': 'delete_teacher', 'id': teacher_id}
        response = requests.delete(url=teacher_urls, data=data, headers=teacher_headers, cookies=self.cookies)
        print('删除老师-获取到的结果是：{}'.format(response.json()))
        my_logger.info('删除老师-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
        except Exception as e:
            my_logger.info('删除老师程异常的结果是：{}'.format(e))
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        Teacher_Env().env_teacher()


if __name__ == '__main__':
    unittest.main()
