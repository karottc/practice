#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

a = 1234
print "a=@0x%d" % id(a)
print "1234=@0x%d" % id(1234)

b = 2345
print "b=@0x%d" % id(b)

a = 2345
print "a=@0x%d" % id(a)

l = [1,2,3]
print "l=@0x%d" % id(l)
l.append(4)
print "l=@0x%d" % id(l)

lt = l
print "lt=@0x%d" % id(lt)
lt.append(5)
print l


