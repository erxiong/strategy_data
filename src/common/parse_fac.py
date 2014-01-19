#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/parse_fac.py

import os
import sys
import types
sys.path.append('../config')
from parse import LogParse
from logtype import LogType
from json_parse import JsonParse
from kv_parse import KvParse
from iis_parse import IisParse
from productline import ProductLine

class ParseFac:
  def __init__(self):
    self.parse = None

  def get_logparse(self, log_type, productobj = None):
    if log_type == LogType.iislog:
      if productobj != None and type(productobj) == types.ClassType and issubclass(productobj, ProductLine):
        self.parse = IisParse(productobj)
      else:
        self.parse = IisParse()

    if log_type == LogType.weblog or log_type == LogType.applog:
      if productobj != None and type(productobj) == types.ClassType and issubclass(productobj, ProductLine):
        self.parse = KvParse(productobj)
      else:
        self.parse = KvParse()

    return self.parse
