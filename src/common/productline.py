#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/productline.py

import os
import sys
from abc import ABCMeta, abstractmethod

class ProductLine:
  ihotel = 'ihotel'

  @abstractmethod
  def get_itspath_in(self):
    pass

  @abstractmethod
  def get_itspath_out(self):
    pass

  @abstractmethod
  def get_userid(self, parse):
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
