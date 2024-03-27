#!/usr/bin/env python
# @Time     : 2024-03-27 0:10
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : test_course_data.py
# @Software : PyCharm

# 登录
course_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
course_login_url = 'http://localhost:8087/api/mgr/loginReq'
course_login_data = {"username": "auto", "password": "sdfsdfsdf"}

# 增删改查url
course_urls = "http://localhost:8087/api/mgr/sq_mgr/"

# 添加课程
add_course_data = {'action': 'add_course', 'data': '''{"name":"初中地理","desc":"初中地理课程","display_idx":1}'''}
add_course_data2 = {'action': 'add_course', 'data': '''{"name":"初中几何","desc":"初中几何课程","display_idx":2}'''}
# 列出课程
list_course_data = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}
# 修改课程
# put_course_data = {'action': 'modify_course', 'id': ids,
#                    'newdata': '''{"name":"初中化学","desc":"初中化学课程","display_idx":1}'''}
# 删除课程
# del_course_data = {'action': 'delete_course', 'id': ids}
