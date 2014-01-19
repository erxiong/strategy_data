#!/usr/bin/env python
#-*-coding:utf-8-*-
## author: meng.liu@corp.elong.com
## File name: common/time_op_test.py


import os
import sys
import time
sys.path.append('../../src/common')
from time_op import TimeOp

class TimeOpTest():
  
  def test_get_day(self):
    to = TimeOp('%Y%m%d')   
    print to.get_day(1)



if __name__ == '__main__':
  tot = TimeOpTest()
  tot.test_get_day()
