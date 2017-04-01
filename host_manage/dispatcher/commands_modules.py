#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 16:37

import sys
from host_manage.modules.modules_dicts import modules_dicts
from host_manage.modules.help_handbook import handbook

class ArgvsReceiver(object):
    '''
    接收用户指令并分配到相应模块
    '''
    def __init__(self,argvs):
        self.argvs = argvs
        self.argvs_parse()

        #解析
    def argvs_parse(self):
        print(self.argvs)
        if len(self.argvs) <=2:
            handbook(self)
        module_name = self.argvs[1]
        if '.' in module_name:
            mod_name,mod_func = module_name.split('.')
            module_instance = modules_dicts.get(mod_name)
        if module_instance:
                module_instance(self.argvs)

        else:
            exit("invalid argument[module_name]")



