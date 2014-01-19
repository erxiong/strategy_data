#!/usr/bin/env python
#-*-coding: utf-8-*-
## File name: ub_model/mr/mr_fac.py

import os
import sys
import logging
sys.append('../../common')
from mr import Mr
from utils import Utils

class MrFac:
  def __init__(self):
    self.mr = None

  def getmr(self, mrname, productline):
    abspath = self.getmr_abspath(mrname)
    self.mr = Utils.getinstanceffile(abspath, Mr, productline)

    return self.mr

  def getmr_abspath(self, mrname):
    if mrname != None and not mrname.endswith('.py'):
      mrname = '%s.py' %(mrname)
    
    abspath = ''
    files = os.listdir('.')

    for f in files:
      if f == mrname:
        abspath = os.path.abspath('./%s' %(mrname))

    if abspath == '':
      logging.error("can't find mr file: %s" %(mrname))
    return abspath
