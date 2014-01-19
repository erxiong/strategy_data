#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/productline_ihotel.py


import os
import sys
import types
from time_op import TimeOp
from config import Config
from productline import ProductLine
from parse import Parse

class ProductLineIhotel(ProductLine):
  def __init__(self):
    self.conf = Config([])
    self.timeop = TimeOp()

  def get_userid(self, parse):
    if type(parse) == types.ClassType and insubclass(parse, Parse)
      cookieid = parse.getcookie()
      return cookieid
    else:
      logging.error('parse error: %s' parse)

  def get_itspath_in(self):
    yesterday = self.timeop.get_day()
    iis_log_path = '%s/%s/part-*' %(self.conf.get('DataPath', 'iis_log'), yesterday)
    web_log_path = '%s/%s/part-*' %(self.conf.get('DataPath', 'web_log'), yesterday)
    app_log_path = '%s/%s/part-*' %(self.conf.get('DataPath', 'app_log'), yesterday)

    path_in = '{%s,%s,%s}' %(iis_log_path, web_log_path, app_log_path)

    return path_in

  def get_itspath_out(self):
    yesterday = self.timeop.get_day()
    merge_log = '%s/%s' %(self.conf.get('DataPath', 'its_log'), yesterday)

    return merge_log

  def getcookie(self):
    pass

  def getts(self):
    pass

  def getdict(self):
    pass
