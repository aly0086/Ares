#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 04/04/2017 21:44

from host_manage.dispatcher.disp_options import BaseParsing

class User(BaseParsing):
    def uid(self,*args,**kwargs):
        #基本类型检测
        self.argv_validation('uid',args[0],int)
        cmd = "-u %s" % args[0]
        self.single_argvs.append(cmd)
        return cmd
    def gid(self,*args,**kwargs):
        self.argv_validation('gid', args[0], int)
        cmd = "-g %s" % args[0]
        self.single_argvs.append(cmd)
        return cmd
    def home(self,*args,**kwargs):
        self.argv_validation('home', args[0], str)
        cmd = "-h %s" % args[0]
        self.single_argvs.append(cmd)
        return cmd
    def fullname(self,*args,**kwargs):
        self.argv_validation('fullname', args[0], str)
        cmd = "-f %s" % args[0]
        self.single_argvs.append(cmd)
        return cmd
    def password(self,*args,**kwargs):
        self.argv_validation('password', args[0], str)
        cmd = "-p %s" % args[0]
        self.single_argvs.append(cmd)
        return cmd
    def shell(self,*args,**kwargs):
        self.argv_validation('shell', args[0], str)
        cmd = "-s %s" % args[0]
        self.single_argvs.append(cmd)
        return cmd

    def present(self,*args,**kwargs):
        options_list = []
        username = kwargs.get('section')
        #print("single argv :",self.single_argvs)
        self.single_argvs.insert(0,"useradd %s" % username)
        options_list.append(' '.join(self.single_argvs))
        options_list.extend(self.single_line_argvs)
        return options_list
        #print("single line argv:",self.single_line_argvs)
        #print("option list:",options_list)

    # 检测自身选项
    def required_check(self,*args,**kwargs):
        print('checking user required',args,kwargs)
        name = args[1]
        cmd ='''cat /etc/group |awk -F':''{print $1}' | grep -w %s -q;echo $?''' % name
        return cmd


# 特殊设定 便于修改不同的参数
class UbuntuUser(User):
    # 重写公用类设定
    # def home(self,*args,**kwargs):
        # print("in ubuntu home")

    def password(self,*args,**kwargs):
        # 传入用户名参数通过kwargs
        username = kwargs.get('section')
        password = args[0]
        cmd = '''echo "%s:%s" | sudo chpasswd''' %(username,password)
        self.single_line_argvs.append(cmd)


class WindowsUser(User):
    #重写公用类设定
    def home(self,*args,**kwargs):
        print("in windows home")

class RedhatUser(User):
    #重写公用类设定
    def home(self,*args,**kwargs):
        print("in redhat home")