#!/usr/local/bin/python
#coding=UTF-8

# 不要下面这两句也是可以执行的
#import sys
#sys.path.append('/Users/k/projects/practice/python')

import hello_20140710

hello_20140710.hello()

print hello_20140710.__name__


## time
import time
start = time.time()

print 'localtime =', time.localtime()
print 'gobaltime =', time.gmtime()
# output: 
#localtime = time.struct_time(tm_year=2014, tm_mon=7, tm_mday=12, tm_hour=8, tm_min=21, tm_sec=18, tm_wday=5, tm_yday=193, tm_isdst=0)
#gobaltime = time.struct_time(tm_year=2014, tm_mon=7, tm_mday=12, tm_hour=0, tm_min=21, tm_sec=18, tm_wday=5, tm_yday=193, tm_isdst=0)

print 'mktime =', time.mktime(time.gmtime())
# output: mktime = 1405095855.0

time.sleep(5)   # 解释器等待指定秒数

print 'total time =', time.time() - start


