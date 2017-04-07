#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 04/04/2017 21:25
from host_manage.dispatcher.disp_options import BaseParsing

class File(BaseParsing):
    def user(self,*args,**kwargs):
        pass
    def sources(self,*args,**kwargs):
        pass
    def group(self,*args,**kwargs):
        pass
    def mode(self,*args,**kwargs):
        pass
    def recurse(self,*args,**kwargs):
        pass
    def source(self,*args,**kwargs):
        pass

    def managed(self,*args,**kwargs):
        pass
    def directory(self,*args,**kwargs):
        pass

    #生成命令集给客户端判断要不要执行
    def required_check(self, *args, **kwargs):
        file_path = args[1]
        cmd = "test -f %s;echo $?" % file_path
        return cmd
