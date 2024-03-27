#!/usr/bin/env python
# @Time     : 2024-03-17 12:56
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : a_01.py
# @Software : PyCharm


# import requests
# import time
#
#
# def start_end_env():
#     # 老师模块
#     login_url = "http://localhost:8087/api/mgr/loginReq"
#     login_data = {"username": "auto", "password": "sdfsdfsdf"}
#     login_response = requests.post(url=login_url, data=login_data)
#
#     teacher_payload = {'action': 'list_teacher', 'pagenum': 1, 'pagesize': 20}
#     list_teacher = "http://localhost:8087/api/mgr/sq_mgr/?"
#     list_teacher_response = requests.get(url=list_teacher, params=teacher_payload, cookies=login_response.cookies)
#     course_response = list_teacher_response.json()['retlist']
#     # print(course_response)
#     ids_values = []
#     for d in course_response:
#         ids_values.append(d['id'])
#     # print(ids_values)
#     time.sleep(1)
#     for ids in ids_values:
#         if ids:
#             payload = {"action": "delete_teacher", "id": {ids}}
#             requests.delete('http://localhost:8087/api/mgr/sq_mgr/', data=payload, cookies=login_response.cookies)
#         else:
#             print('删除课程请求报错啦')
#     time.sleep(1)
#
#
# time.sleep(1)
#
# if __name__ == '__main__':
#     start_end_env()


# print(res.values())


import requests

# url = "http://localhost:8087/api/mgr/loginReq"
# data = {"username": "auto", "password": "sdfsdfsdf"}
# res = requests.post(url, data).cookies
#
# del_res = 'http://localhost:8087/api/mgr/sq_mgr/'
# params = {'action': 'delete_course', 'id': 1170}
# headers = {'Content-Type':'application/x-www-form-urlencoded'}
# response = requests.delete(del_res, data=params, headers=headers, cookies=res)
# print(response.json())


# ids = 1234
# courser = [{"id": ids, "name": "初中地理"}]
# print(courser)
# add_data = {"action": "add_teacher",
#             "data": {"username": "Toy", "password": "sq888", "realname": "托尼", "desc": "托尼老师",
#                      "courses": [{"id": ids, "name": "初中代数"}], "display_idx": "1"}}
#
# print(add_data)
# add_data['data'] = {'action': 'add_teacher',
#                     'data': f'''{"username":"Toy","password":"sq888","realname":"托尼","desc":"托尼老师","display_idx":"1"}'''}
# print(add_data)


headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = "http://localhost:8087/api/mgr/loginReq"
data = {"username": "auto", "password": "sdfsdfsdf"}
cookies = requests.post(url, data, headers=headers).cookies

# ids = 1239
# urls = "http://localhost:8087/api/mgr/sq_mgr/"
# adds = {'action': 'add_teacher', 'data': '''{"username":"Toy","password":"sq888","realname":"托尼","desc":"托尼老师","courses": [{"id": %s, "name": "初中地理"}],"display_idx":1}'''% ids}
#
#
# response = requests.post(url=urls, data=adds, headers=headers, cookies=cookies)
# print(response.json())

# ids = 1239
# add_data = {'action': 'add_teacher', 'data': '''{"username":"Toy","password":"sq888","realname":"托尼","desc":"托尼老师","courses": [{"id": %s}, "name": "初中地理"}],"display_idx":1}'''%(ids)}
#
# print(add_data)

# 修改
# urls = "http://localhost:8087/api/mgr/sq_mgr/"
# put_data = {'action': 'modify_teacher', 'id': 274,
#             'newdata': '''{"username":"Tom","courses":[],"realname":"Tom","desc":"Toms","display_idx":1,"password":"sq888"}'''}
# put_res = requests.put(url=urls, data=put_data, headers=headers, cookies=cookies)
# print('修改老师-获取到的结果是：{}'.format(put_res.json()))




