#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 16:16

import os
from host_manage.dispatcher.disp_options import BaseParsing

class State(BaseParsing):

    #加载yml文件
    def load_state_files(self,state_filename):
        from yaml import load
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper

        state_file_path = "%s/%s" %(self.settings.SOURCE_CONF_FILE_DIR,state_filename)
        if os.path.isfile(state_file_path):
            with open(state_file_path) as f:
                data = load(f.read(), Loader=Loader)
                return data
        else:
            exit("%s is not a valid yaml config file" % state_filename)


    def apply(self):

        '''
        load the conf file
        parsing
        create a task ,sent it to rabbitMQ
        collect the result with task-callback id
        :return:
        '''

        if '-f' in self.sys_argvs:
            #将yml解析成字典
            yml_file_index = self.sys_argvs.index('-f')+1
            try:
                yml_filename = self.sys_argvs[yml_file_index]
                yml_read = self.load_state_files(yml_filename)
                # print("conf data :",yml_read)
                # 按照不同的操作,单独生成配置文件
                for os_type,os_type_data in self.config_data_dict.items():
                    #遍历yml文件
                    for main_key,main_value in yml_read.items():

                        for sec_key,sec_value in main_value.items():
                            base_mod_name = sec_key.split(".")[0]
                            mod_conf_path = "%s/%s.py" % (self.settings.MODULES_DIR,base_mod_name)
                            if os.path.isfile(mod_conf_path):

                                # 导入services模块
                                mod_conf = __import__("services.%s" % base_mod_name)
                                #自动实现系统类型和配置文件相匹配
                                comp_os_mod_name = "%s%s" % (os_type.capitalize(),base_mod_name.capitalize())
                                # 判断有没有根据操作系统的类型进行特殊解析的类，是否在文件中
                                # 导入模块
                                imp_mod = getattr(mod_conf, base_mod_name)
                                if hasattr(imp_mod,comp_os_mod_name):
                                    #导入私有类
                                    mod_inst = getattr(imp_mod,comp_os_mod_name)
                                else:
                                    #导入通用类
                                    mod_inst = getattr(imp_mod,base_mod_name.capitalize())
                                # 开始调用module进行解析
                                # 实例化mod_obj
                                mod_obj = mod_inst(self.sys_argvs,self.db_mod,self.settings)
                                mod_obj.syntax_check(main_key,sec_key,sec_value)#apache,user.present
                            else:
                                exit("modules[%s] is not exist" % base_mod_name)
                            #print("  ",sec_key)
                            #for branch_value in sec_value:
                            #    print("\t",branch_value)
            except IndexError as e:
                exit("yml file must be provided behind options")
        else:
            exit("apply options must be provided")






