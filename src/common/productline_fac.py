#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/productline_fac.py

import os
import sys
from productline import ProductLine
from productline_ihotel import ProductLineIhotel

class ProduceLineFac:
  def __init__(self):
    self.productline = None

  def get_productline(self, prodect_line):
    if product_line == ProductLine.ihotel:
      self.productline = ProductLineIhote()

    return self.productline
