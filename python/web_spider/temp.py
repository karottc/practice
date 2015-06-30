#coding=UTF-8
__author__ = 'chenyang6'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

a = [u'速度',u'',u'',u'斯蒂芬森',u'哈哈哈哈']
print a


str = ""
line = u"中午"
str += "%s," % line
line = u'难道是中文的问题'
str += "%s," % line
print str


line = '<div class="content">'
ret = line.find('<div class="content">',0)
if ret != -1:
    print 'pass'

print ret

