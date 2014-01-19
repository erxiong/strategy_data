#!/usr/bin/env python
#-*-coding: utf-8-*-
## File name: ub_model/mr/mr.py

import sys
import os
from abc import ABCMeta, abstractmethod

class Mr(object):
  def __init__(self, productline):
    pass
    
  @abstractmethod
  def get_path_in(self):
    pass

  @abstractmethod
  def get_path_out(self):
    pass

  @abstractmethod
  def mapper(self, key, value):
    pass

  @abstractmethod
  def reducer(self, key, values):
    pass

  def get_filename(self):
    mypath = os.path.realpath(__file__)
    
    if mypath.endswith('c'):
      mypath = mypath[0:len(mypath) - 1]

    return mypath

  def run(self):
    import dumbo
    dumbo.run(self.mapper, self.reducer)
