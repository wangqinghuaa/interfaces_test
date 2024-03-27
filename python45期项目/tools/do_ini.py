#!/usr/bin/env python
# @Time     : 2024-03-16 21:15
# @Author   : 华
# @Email    : 867075698@qq.com
# @File     : do_ini.py
# @Software : PyCharm

import configparser

from tools.project_path import *


def read_config(file_name, section, option):
    cf = configparser.ConfigParser()
    cf.read(file_name, encoding="utf-8")
    return cf[section][option]


if __name__ == '__main__':
    res = read_config(case_config_path, "MODE", "mode")
    print(res)
