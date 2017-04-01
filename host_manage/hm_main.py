#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 16:07

import os,sys

if __name__ == "__main__":
    #添加app host_manage 的层级环境变量
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    #all modules in module_dict
    from host_manage.modules.modules_dicts import modules_dicts
    from host_manage.dispatcher.commands_modules import ArgvsReceiver
    obj = ArgvsReceiver(sys.argv)