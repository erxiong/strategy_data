#!/usr/bin/env python
#-*-coding: utf-8-*-
## File name: main.py

import sys
sys.path.append('common')
sys.path.append('ub_model/mr')
from mapreduce import MapReduce
from mr_fac import MrFac
from productline_fac import ProductLineFac

if __name__ == '__main__':
  productline = sys.argv[1]
  mrname = sys.argv[2]
  
  mrfac = MrFac()
  mr = mrfac.getmr(mrname, productline)

  mrrunner = MapReduce()
  mrrunner.execute(mr)
