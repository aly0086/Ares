#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 04/04/2017 21:55
from host_manage.services.user import User

class UbuntuUser(User):
    #重写公用类设定
    def home(self):
        print("in ubuntu home")

