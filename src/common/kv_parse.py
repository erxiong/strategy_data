#!/usr/bin/env python
#-*-coding: utf-8-*-

## File name: common/kv_parse.py

from parse import LogParse

class KvParse(LogParse):
  def __init__(self, productobj):
    Logparse.__init__(self, productobj)
    self.productobj = productobj
    self.dicts = None
  
  def parse2dict(self, val):
    pass

  def get_uid(self):
    uid = self.productobj.get_userid(self)

  def getbykey(self, keylist):
    pass

  def getcookie(self):
    pass

  def getts(self):
    pass

  def getdict(self):
    pass
