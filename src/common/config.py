#!/usr/bin/env python
#-*-coding: utf-8-*-
## File name: common/config.py

import sys
import ConfigParser
import logging
import os

class Config(object):
    def __init__(self, conf_list):
        self.format_logging()

        self.config = ConfigParser.ConfigParser()
        self.conf_list = conf_list

        self.read_confs()

    def read_confs(self):
        global_conf = '../config/global.conf'
        if os.path.exists(global_conf):
            if global_conf not in self.conf_list:
                self.conf_list.append(global_conf)
        else:
            logging.debug('global conf file is not exist: %s' %(global_conf))

        for conf_file in self.conf_list:
            if os.path.exists(conf_file):
                self.config.readfp(open(conf_file),"wb")
            else:
                logging.debug('config file is not exist: %s' %(conf_file))

    def get_conf(self):
        return self.config

    def format_logging(self):
        logging.basicConfig(\
            level=logging.DEBUG,\
            format="%(asctime)s|%(levelname)s|%(filename)s at function:" + \
            "%(funcName)s[line:%(lineno)d]|%(message)s",\
            datefmt='%a, %d %b %Y %H:%M:%S',\
            stream=sys.stderr \
        )

#test
if __name__ == '__main__':
    conf_list = ['../config/test1.conf']
    config = Config(conf_list)
    conf = config.get_conf()
    print conf.get('Hbase', 'HadoopPath')
    print conf.get('Hadoop', 'HadoopPath')
