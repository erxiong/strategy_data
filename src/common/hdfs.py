#!/usr/bin/env python
#-*-coding:utf-8-*-
## File name: common/hdfs.py


class Hdfs:
  def check_file(self, input_path):
    flag = False
    cmd = "hadoop fs -ls %s" % (input_path)
    import subprocess
    result = subprocess.Popen( \
              [cmd], stderr=subprocess.PIPE, shell=True).communicate()[1]
    if -1 == result.find("No such file or directory"):
      flag = True
    return flag

  def replace_path(self, path, date, data_type):
    new_path = path
    if "" != date:
      new_path = new_path.replace("{Date}", date)
    if "" != data_type:
      new_path = new_path.replace("{DataType}", data_type)
    return new_path

  def delete(self, rm_dir):
    cmd = ("hadoop fs -rm -r %s") % (rm_dir)
    os.system(cmd)
