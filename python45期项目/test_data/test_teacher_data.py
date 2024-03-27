#!/usr/bin/env python
# @Time     : 2024-03-27 0:10
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : test_teacher_data.py
# @Software : PyCharm


# 登录
teacher_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
teacher_login_url = 'http://localhost:8087/api/mgr/loginReq'
teacher_login_data = {"username": "auto", "password": "sdfsdfsdf"}

# 增删改查url
teacher_urls = "http://localhost:8087/api/mgr/sq_mgr/"

# 添加老师
# add_data_teacher = {'action': 'add_teacher',
#                     'data': '''{"username":"Toy","password":"sq888","realname":"托尼","desc":"托尼老师",
#             "courses": [{"id": %s, "name": "初中地理"}],"display_idx":1}''' % ids}
# 列出老师
teacher_list_data = {'action': 'list_teacher', 'pagenum': 1, 'pagesize': 20}
# 修改老师
# put_teacher_data = {'action': 'modify_teacher', 'id': teacher_id,
#                     'newdata': '''{"username":"Tom","courses":[],"realname":"汤姆","desc":"汤姆老师","display_idx":1,
#             "password":"sq888"}'''}
# 删除老师
# del_teacher_data = {'action': 'delete_teacher', 'id': teacher_id}