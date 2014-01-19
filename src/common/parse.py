#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/parse.py

import os
import sys
from abc import ABCMeta, abstractmethod

class LogParse:
  def __init__(self, productobj):
    pass

  def get_log_type(self, line):
    pass
  
  @abstractmethod
  def parse2dict(self, val):
    pass
  
  @abstractmethod
  def getbykey(self, keylist):
    pass

  @abstractmethod
  def getcookie(self):
    pass

  @abstractmethod
  def getts(self):
    pass

  @abstractmethod
  def getdict(self):
    pass
