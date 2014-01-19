#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/utils.py

import os
import sys
import types

class Utils:
  def getinstanceffile(self, pf, father, param = None):
    obj = None
    
    if not os.path.exists(pf):
      logging.error('file is not exists:%s' %(pf))
      return obj
    
    try:
      module = __import__(pf)
      attlist = dir(module)
    
      for word in attlist:
        att = getattr(module, word)
        if type(att) == types.ClassType and issubclass(att, father):
          if param is not None:
            obj = att(param)
          else:
            obj = att()
          return obj
    except Exception as e:
      logging.error(e)
    
    return obj
