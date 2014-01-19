#!/usr/bin/env python

import sys
sys.path.append('../../../src/ub_model/mr')
from mr import Mr

class T(Mr):
  def __init__(self):
    pass

if __name__ == "__main__":
  t = T()
  print t.get_filename()
