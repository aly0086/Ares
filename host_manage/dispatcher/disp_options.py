#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 17:56
import os

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

    def get_mod_inst(self,*args,**kwargs):
        base_mod_name = kwargs.get('base_mod_name')
        os_type = kwargs.get('os_type')
        mod_conf_path = "%s/%s.py" % (self.settings.MODULES_DIR, base_mod_name)
        if os.path.isfile(mod_conf_path):

            # 导入services模块
            mod_conf = __import__("services.%s" % base_mod_name)
            # 自动实现系统类型和配置文件相匹配
            comp_os_mod_name = "%s%s" % (os_type.capitalize(), base_mod_name.capitalize())
            # 判断有没有根据操作系统的类型进行特殊解析的类，是否在文件中
            # 导入模块
            imp_mod = getattr(mod_conf, base_mod_name)
            if hasattr(imp_mod, comp_os_mod_name):
                # 导入私有类
                mod_inst = getattr(imp_mod, comp_os_mod_name)
            else:
                # 导入通用类
                mod_inst = getattr(imp_mod, base_mod_name.capitalize())
            # 开始调用module进行解析
            # 实例化mod_obj
            mod_obj = mod_inst(self.sys_argvs, self.db_mod, self.settings)
            return mod_obj

        else:
            exit("modules[%s] is not exist" % base_mod_name)
            # print("  ",sec_key)
            # for branch_value in sec_value:
            #    print("\t",branch_value)


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





