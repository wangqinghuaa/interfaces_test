#!/usr/bin/env python
# @Time     : 2024-03-16 19:15
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : project_path.py
# @Software : PyCharm

import os
"""专门来读取路径的值"""

path = os.path.relpath(__file__)
# print(path)  # 获取当前文件的绝对路径

# 获取顶级绝对路径
pr_paths = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试报告的路径
test_report_path = os.path.join(pr_paths, "test_result", "report\\")
# print(test_report_path)
# 日志路径
test_config_log = os.path.join(pr_paths, "test_result", "logs", "logs")
