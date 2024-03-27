#!/usr/bin/env python
# @Time     : 2024-03-16 15:11
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm

import unittest
import HTMLTestRunnerNew
from datetime import datetime
from test_case.course_case import Course_Test
from test_case.teacher_case import Teacher_Test
# from test_case import http_request_course
# from test_case import http_request_teacher
from tools.project_path import *

current_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S_' + 'report')

suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))
# 执行用例
# runner = unittest.TextTestRunner()
# runner.run(suite)

load = unittest.TestLoader()
suite.addTest(load.loadTestsFromTestCase(Course_Test))
suite.addTest(load.loadTestsFromTestCase(Teacher_Test))

# 通过模块加载用例
# suite.addTest(load.loadTestsFromModule(http_request_course))
# suite.addTest(load.loadTestsFromModule(http_request_teacher))


with open(test_report_path + '{}.html'.format(current_time), 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                              title="python业务测试报告",
                                              # description="单元测试第二次报告",
                                              tester="小飞")
    runner.run(suite)


