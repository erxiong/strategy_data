#!/usr/bin/env python
#-*-coding:utf-8-*-

## File name: common/time_op.py

class TimeOp(object):
  def __init__(self, time_format):
    self.time_format = time_format

  def cal_costTime(self, endTime, startTime):
    try:
      cost_time = time.mktime(time.strptime(endTime, self.time_format)) - \
            time.mktime(time.strptime(startTime, self.time_format))
    except Exception, e:
      logging.warn(str(e))
      cost_time = None
    return cost_time

  def get_day(self, n):
    ## get n-1 days before yesterday.
    date = None
    try:
      if int != type(n):
        raise Exception
      timestamp = time.time() - 24*60*60*n
      date = time.strftime('%Y%m%d', time.localtime(timestamp))
    except Exception, e:
        logging.warning(str(e))
    return date

  def get_all_days(self, n):
    list_days = []
    try:
      if int != type(n):
        raise Exception
      if n < 0:
        for i in xrange(1, -n + 1): ## from tomorrow to n-1 days after tomorrow.
          d = self.get_day(-i)
          if not d:
            logging.warning("Can't get a day!")
          else:
            list_days.append(d)
      else:
        for i in xrange(0, n): ## from n-1 days before yesterday to yesterday.
          d = self.get_day(n - i)
          if not d:
            logging.warning("Can't get a day!")
          else:
            list_days.append(d)
    except Exception, e:
      logging.warning(str(e))
    return list_days

  def time_granularity(self, time_stamp, g):
    '''
    g: y, m, d, h
    '''
    time_g = None
    try:
      seg = time_stamp.split('_')
      time_g = seg[0]
      index = 0
      if 'y' == g:
        index = 0
      elif 'm' == g:
        index = 1
      elif 'd' == g:
        index = 2
      elif 'h' == g:
        index = 3
      for i in xrange(1, index + 1):
        time_g += '_' + seg[i]
    except Exception, e:
      logging.warn("Time stamp error.|%s\n" % str(e))
    return time_g

  def get_next_day(self, ts, fmt):
    return self.get_n_days_later(ts, fmt, 1)

  def get_former_day(self, ts, fmt):
    return self.get_n_days_before(ts, fmt, 1)

  def get_n_days_later(self, ts, fmt, n):
    locat_time = time.mktime(time.strptime(ts, fmt)) + 60*60*24*n
    return time.strftime(fmt, time.localtime(locat_time))

  def get_n_days_before(self, ts, fmt, n):
    locat_time = time.mktime(time.strptime(ts, fmt)) - 60*60*24*n
    return time.strftime(fmt, time.localtime(locat_time))


