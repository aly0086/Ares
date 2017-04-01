#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 17:56


class BaseParsing(object):
    def __init__(self,sys_argvs,db_mod):
        self.db_mod = db_mod
        self.sys_argvs = sys_argvs
        self.fetching_hosts()

    def fetching_hosts(self):
        print('--fetching data from hosts--')

        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                host_index = self.sys_argvs.index('-h')+1
                if len(self.sys_argvs) <= host_index:
                    exit("no argument behind options")
                else:
                    host_str = self.sys_argvs[host_index]
                    host_str_list = host_str.split('.')
                    host_list += self.db_mod.Host.objects.filter(hostname__in = host_str_list)
                    #print("--host list:", host_list)

            if '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g')+1
                if len(self.sys_argvs) <= group_str_index:
                    exit("no argument behind options")
                else:
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split('.')
                    group_list = self.db_mod.HostGroup.objects.filter(name__in = group_str_list)
                    for group in group_list:
                        host_list += group.hosts.select_related()
            host_list = set(host_list)
            print("--host list:", host_list)

        else:
            exit("no options [-h] or [-g]")