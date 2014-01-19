#!/usr/bin/env python
#-*-coding:utf-8-*-
## File name: ub_model/mr/its.py

from mr import Mr
import sys
sys.path.append('../../common/')
from config import Config
from time_op import TimeOp
from json_op import JsonOp
from parse import LogParse
from parse_fac import ParseFac
from productline_fac import ProduceLineFac 

class ItsMr(Mr):
  def __init__(self, productline):
    Mr.__init__(self, productline)

    config = Config([])
    self.conf = config.get_conf()
    self.itstime_mergin = int(self.conf.get('Its', 'time_margin_seconds'))
    self.timeop = TimeOp('yyyyMMdd')
    self.logparse = LogParse()
    self.parsefac = ParseFac()

    self.last_cookieid = ''
    self.last_ts = 0

    self.productline = productline
    plf = ProduceLineFac
    self.productobj= plf.get_productline(self.productline)


  def get_path_in(self):
    return self.productobj.get_itspath_in()

  def get_path_out(self):
    return self.productobj.get_itspath_out()

  def mapper(self, key, value):
    line = value.strip()
    log_type = self.logparse.get_log_type(value)
    logparse = self.parsefac.get_logparse(log_type)

    logparse.parse2dict(value)

    cookieid = logparse.getcookie()
    ts = logparse.getts()
    vals = jo.gen_json(logparse.getdict())

    outkey = '%s_%s' %(cookieid, ts)

    yield outkey, vals

  def reducer(self, key, values):
    pass

  def is_new_its(self, uid, ts, refer, qid):
    is_new = None

    if type(ts) is not types.IntType:
      return is_new
    if uid != self.last_cookieid:
      is_new = True
    elif ts - self.last_ts > self.itstime_mergin and refer.strip() == '' \
        and qid.strip() == '':
      is_new = True
    else:
      is_new = False

    return is_new

if __name__ == "__main__":
  mr = MergeMr()
  mr.run()
