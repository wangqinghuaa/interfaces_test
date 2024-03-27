#!/usr/bin/env python
# @Time     : 2024-03-14 10:30
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : my_logs.py
# @Software : PyCharm

import logging
from tools.project_path import *


class MyLogging:

    def my_log(self, msg, level):

        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger("python")

        # 设定级别
        my_logger.setLevel("DEBUG")

        # 设定日志输出方式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 创建我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("ERROR")
        ch.setFormatter(formatter)

        fh = logging.FileHandler(test_config_log, encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        # 两者对接-指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)
        # 关闭日志收集-关闭渠道-不然会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, "DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

    def error(self, msg):
        self.my_log(msg, "ERROR")

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")

"""
日志的默认级别是 warning
debug    详细信息，常用于调试                           info  程序正常运行过程中产生的一些信息
warning  警告用户，虽然程序还在正常工作，但有可能发生错误    error 由于更严重的问题，程序已经不能执行一些功能了
critical 严重错误，程序已经不能继续运行
"""
if __name__ == '__main__':
    pass
    MyLogging().my_log("stone 今天有点萌萌达", "ERROR")
    MyLogging().my_log("stone 今天有点萌萌达2", "ERROR")
    my_logger = MyLogging()
    my_logger.debug("多云")
    my_logger.info("晴天")
    my_logger.warning("阴")
    my_logger.error("下雨")
    my_logger.critical("暴雨")

