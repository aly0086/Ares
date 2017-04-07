#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 05/04/2017 09:40

from host_manage.dispatcher.disp_options import BaseParsing

class Group(BaseParsing):
    def gid(self,*args,**kwargs):
        pass
    def present(self,*args,**kwargs):
        pass

    def required_check(self, *args, **kwargs):
        print('checking user required', args, kwargs)
        name = args[1]
        cmd = '''cat /etc/group |awk -F':''{print $1}' | grep -w %s -q;echo $?''' % name
        return cmd