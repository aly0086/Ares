#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 17:41

from host_manage.modules.modules_dicts import modules_dicts

def handbook(self):
    print("Avaliable modules:")
    for reg_mod in modules_dicts:
        print("\t%s" % reg_mod)
    exit()