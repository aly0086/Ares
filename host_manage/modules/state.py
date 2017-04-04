#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:Aurora.R.L.Y
# Created on: 01/04/2017 16:16

from host_manage.dispatcher.pub_parsing import BaseParsing
import os

class State(BaseParsing):

    def load_state_files(self,state_filename):
        from yaml import load, dump
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
            yml_file_index = self.sys_argvs.index('-f')+1
            try:
                yml_filename = self.sys_argvs[yml_file_index]
                yml_read = self.load_state_files(yml_filename)
                #print("conf data :",yml_read)
                for main_key,main_value in yml_read.items():
                    print(main_key)
                    for sec_key,sec_value in main_value.items():
                        print("    -",sec_key)
                        for branch_value in sec_value:
                            print("\t",branch_value)



            except IndexError as e:
                exit("yml file must be provided behind options")
        else:
            exit("apply options must be provided")







