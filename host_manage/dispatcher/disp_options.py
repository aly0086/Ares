#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 17:56


class BaseParsing(object):
    #初始化方法，便于调用
    def __init__(self,sys_argvs,db_mod,settings):
        #其他的模块需要调用，在基类写好，可以直接导入
        self.settings = settings
        self.db_mod = db_mod
        self.sys_argvs = sys_argvs

    def argv_validation(self,key,val,data_type):
        if type(val) is not data_type:
        # data_type is in function set
            exit("[%s] data type is not valid" % key)



    def get_selected_os_types(self):
        #获取系统类型，为了以后存取配置文件
        os = {}
        for host in self.host_list:
            os[host.os_type] = []
        print('--> os type:', os)
        return os

    def process(self):
        #实例化可以进行调用
        self.fetching_hosts()
        #生成操作系统类型
        self.config_data_dict = self.get_selected_os_types()

    def require(self,*args,**kwargs):
        #print("require",args,kwargs)
        for item in args[0]:
            for op_key,op_val in item.items():
                pass #if hasattr()


    def fetching_hosts(self):
        print('--*--fetching data from hosts--*--')

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
                    # print("--host list:", host_list)

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
            self.host_list = set(host_list)
            #return True
            print("--> host list:",host_list)

        else:
            exit("no options [-h] or [-g]")

    #进行 yml  文件解析
    def syntax_check(self,main_key,sec_key,sec_value):#apache user.present
        print("-->parsing yml:\n"," ",main_key,"\n","   ",sec_key)
        #将单行参数与多参数进行分类
        self.single_argvs = []
        self.single_line_argvs = []
        for sec_key_v in sec_value:#选项
            print("\t",sec_key_v)

            for key,val in sec_key_v.items():
                if hasattr(self,key):
                    yml_func = getattr(self,key)
                    yml_func(val,section=main_key)

                else:
                    exit("module[%s] has no argument [%s]" %(sec_key,key))
        else:
           if '.' in sec_key:
               sec_key_front,sec_key_back = sec_key.split('.')

               if hasattr(self,sec_key_back):
                   sec_key_func = getattr(self,sec_key_back)
                   sec_key_func(section=main_key)
               else:
                   exit("[%s] has no method [%s]" %(sec_key,sec_key_back))
           else:
               exit("[%s] mod options must be supplied" % sec_key)





