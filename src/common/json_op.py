#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/json_op.py


import os
import sys

class JsonOp(object):
  def gen_json(self, ds):
    j = None
    try:
      j = json.dumps(ds)
    except Exception:
      j = None
    return j

  def parse_json(self, j): 
    ds = None
    try:
      ds = json.loads(j)
    except Exception:
      ds = None
    return ds
