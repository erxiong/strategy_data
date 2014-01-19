#!/usr/bin/env python
#-*-coding: utf-8-*-

## File name: common/mapreduce.py

import sys
import logging
from config import * 
from hdfs import Hdfs
from utils import Utils
sys.path.append('../src/ub_model/mr')
from mr import Mr

class MapReduce(object):
  def __init__(self):
    config = Config([])
    self.conf = config.get_conf()
    self.hdfs = Hdfs()
    self.jobid = None
    self.stat_running = False
    self.stat_failed = False
    self.stat_success = False
    self.global_conf = False
    self.local_conf = False
    self.mrfile = ''
    self.run_param = ''

  def set_param(self, param_name, param_value): 
    self.run_param = '%s -%s %s' %(self.run_param, param_name, param_value)
  
  def set_params(self, path_in, path_out):
    hadoop_path = self.conf.get('Hadoop', 'HadoopHome')
    hadooplib_path = self.conf.get('Dumbo', 'HadoopLibHome')
    libjar_path = self.conf.get('Dumbo', 'LibJar')
    
    self.path_in = path_in
    self.path_out = path_out

    self.run_param = '%s -hadoop %s -input %s -output %s -hadooplib %s -libjar %s' \
      %(self.run_param, hadoop_path, path_in, path_out, hadooplib_path, libjar_path)

  def killjob(self):
    flag = True
    cmd = ("%s job -Dmapred.job.tracker=192.168.9.247:50030 -kill %s") \
            % (self.jobid)
    with os.popen(cmd) as ipf:
      result = ipf.readline()
    if -1 != result.find("Killed job"):
      flag = True
    else:
      flag = False
    self.stat_failed = True
    self.stat_success = False
    return flag

  def runmr(self):
    run_cmd = 'dumbo start %s %s' %(self.mrfile, self.run_param)

    if self.hdfs.check_file(self.path_out):
      logging.warn('output exists, begin to delete it: %s' %(self.path_out))
      self.hdfs.delete(self.path_out)

    logging.info("cmd is %s" %(run_cmd))

    with os.popen(run_cmd) as ipf:
      for line in ipf:
        logging.info(line)

        line = line.strip()
        if -1 != line.find("Running job:"):
          self.jobid = "%s%s" % ("job_", line.split("job_")[1])
          self.stat_running = True

  def execute(self, mr):
    self.mrfile = mr.get_filename()

    mr_pathin = mr.get_path_in()
    mr_pathout = mr.get_path_out()
    
    self.set_params(mr_pathin, mr_pathout)
    self.runmr()
    
