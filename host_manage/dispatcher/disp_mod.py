#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 16:37
import django
django.setup()
from Ares import settings
import sys
from host_manage.modules.modules_dicts import modules_dicts
from host_manage.modules.help_handbook import handbook
from host_manage import models

class ArgvsReceiver(object):
    '''
    接收用户指令并分配到相应模块
    '''
    def __init__(self,argvs):
        self.argvs = argvs
        self.argvs_parse()

        #解析
    def argvs_parse(self):
        #print(self.argvs)

        if len(self.argvs) <2:
            handbook(self)
        module_name = self.argvs[1]
        if '.' in module_name:
            mod_name,mod_func = module_name.split('.')
            mod_instance = modules_dicts.get(mod_name)
            if mod_instance:
                #拾取参数，调用模块
                #后面的三个参数，表示所有模块，都可以调用这三个参数
                mod_obj = mod_instance(self.argvs,models,settings)
                #解析任务，发送到队列，获取任务结果
                mod_obj.process()
                #判断是否存在
                if hasattr(mod_obj,mod_func):
                    mod_func_obj = getattr(mod_obj,mod_func)
                    #执行，并必须要传参数，因为前面已经传入了
                    #调用指定的方法
                    mod_func_obj()
                else:
                    exit("function[%s] is not in modules[%s]" % (mod_func,mod_name))

        else:
            exit("invalid argument[module_name]")



