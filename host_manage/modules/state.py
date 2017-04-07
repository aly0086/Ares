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
                            # 开始调用module进行解析
                            # 实例化mod_obj
                            mod_obj = self.get_mod_inst(base_mod_name=base_mod_name,os_type=os_type)
                            mod_parse_result = mod_obj.syntax_check(main_key,sec_key,sec_value,os_type)#apache,user.present
                            self.config_data_dict[os_type].append(mod_parse_result)
                           #代表上面的所有数据解析已经完成，接下来生成一个任务，并把任务交给客户端
                            print('config_data_dic'.center(60,'*'))
                            print(self.config_data_dict)
                            #print("  ",sec_key)
                            #for branch_value in sec_value:
                            #    print("\t",branch_value)
            except IndexError as e:
                exit("yml file must be provided behind options")
        else:
            exit("apply options must be provided")






