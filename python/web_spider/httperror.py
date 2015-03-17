#coding=UTF-8
__author__ = 'k'

import urllib2

# HTTP error 示例1
req = urllib2.Request('http://blog.csdn.net/karotte')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"


# HTTP error 示例2
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
else:
    print "OK"