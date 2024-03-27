#!/usr/bin/env python
# @Time     : 2024-03-19 17:48
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : course_case.py
# @Software : PyCharm
import time
import unittest
import requests
from ini_env.teacher_env import Teacher_Env

ids = None
teacher_id = None


class Teacher_Test(unittest.TestCase):

    def __init__(self, methodName):
        super(Teacher_Test, self).__init__(methodName)
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.url = "http://localhost:8087/api/mgr/loginReq"
        self.data = {"username": "auto", "password": "sdfsdfsdf"}
        self.cookies = requests.post(self.url, self.data, self.headers).cookies
        self.urls = "http://localhost:8087/api/mgr/sq_mgr/"



    @classmethod
    def setUpClass(cls) -> None:
        Teacher_Env().env_teacher()

    def test_01_add_course(self):
        add_data = {'action': 'add_course', 'data': '''{"name":"初中地理","desc":"初中地理课程","display_idx":1}'''}
        add_datas = {'action': 'add_course', 'data': '''{"name":"初中几何","desc":"初中几何课程","display_idx":2}'''}
        add_res = requests.post(url=self.urls, data=add_data, headers=self.headers, cookies=self.cookies)
        add_res_01 = requests.post(url=self.urls, data=add_datas, headers=self.headers, cookies=self.cookies)
        print('添加课程-获取到的结果是：{}'.format(add_res.json()))
        print('添加课程-获取到的结果是：{}'.format(add_res_01.json()))
        try:
            self.assertEqual(0, add_res.json()["retcode"])
            self.assertEqual(0, add_res_01.json()["retcode"])
        except Exception as e:
            print("添加课程异常的结果是{}".format(e))
            raise e

    def test_02_list_course(self):
        global ids
        list_data = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}
        list_res = requests.get(url=self.urls, params=list_data, headers=self.headers, cookies=self.cookies)
        print('列出课程-获取到的结果是：{}'.format(list_res.json()))
        ids = list_res.json()['retlist'][0]['id']
        try:
            self.assertEqual(0, list_res.json()["retcode"])
            self.assertIn('初中地理', list_res.json()['retlist'][0].values())
            self.assertLess(1180, list_res.json()['retlist'][0]['id'])
        except Exception as e:
            print("列出课程异常的结果是{}".format(e))
            raise e

    def test_03_add(self):
        global ids
        add_data = {'action': 'add_teacher',
                    'data': '''{"username":"Toy","password":"sq888","realname":"托尼","desc":"托尼老师","courses": [{"id": %s, "name": "初中地理"}],"display_idx":1}''' % ids}
        # print(add_data)
        time.sleep(1)
        add_teacher = requests.post(url=self.urls, data=add_data, headers=self.headers, cookies=self.cookies)
        print('添加老师-获取到的结果是：{}'.format(add_teacher.json()))
        try:
            self.assertEqual(0, add_teacher.json()["retcode"])
            self.assertLess(250, add_teacher.json()['id'])
        except Exception as e:
            print("添加老师异常的结果是{}".format(e))
            raise e

    def test_04_list(self):
        global teacher_id
        list_data = {'action': 'list_teacher', 'pagenum': 1, 'pagesize': 20}
        list_teacher = requests.get(url=self.urls, params=list_data, headers=self.headers, cookies=self.cookies)
        print('列出老师-获取到的结果是：{}'.format(list_teacher.json()))
        teacher_id = list_teacher.json()['retlist'][0]['id']
        try:
            self.assertEqual(0, list_teacher.json()["retcode"])
            self.assertIn('托尼', list_teacher.json()['retlist'][0]['realname'])
        except Exception as e:
            print("列出老师异常的结果是{}".format(e))
            raise e

    def test_05_put(self):
        global teacher_id
        put_data = {'action': 'modify_teacher', 'id': teacher_id,
                    'newdata': '''{"username":"Tom","courses":[],"realname":"汤姆","desc":"汤姆老师","display_idx":1,"password":"sq888"}'''}
        put_res = requests.put(url=self.urls, data=put_data, headers=self.headers, cookies=self.cookies)
        print('修改老师-获取到的结果是：{}'.format(put_res.json()))
        try:
            self.assertEqual(0, put_res.json()["retcode"])
        except Exception as e:
            print("修改老师异常的结果是{}".format(e))
            raise e
    time.sleep(1)

    def test_06_del(self):
        global teacher_id
        params = {'action': 'delete_teacher', 'id': teacher_id}
        response = requests.delete(url=self.urls, data=params, headers=self.headers, cookies=self.cookies)
        print('删除老师-获取到的结果是：{}'.format(response.json()))
        try:
            self.assertEqual(0, response.json()["retcode"])
        except Exception as e:
            print("删除老师异常的结果是{}".format(e))
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        Teacher_Env().env_teacher()


if __name__ == '__main__':
    unittest.main()
