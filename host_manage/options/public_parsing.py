#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 17:56

class BaseParsing(object):
    def __init__(self,sys_argvs):
        self.sys_argvs = sys_argvs
        self.fetching_hosts()

    def fetching_hosts(self):
        print('--fetching data from hosts--')