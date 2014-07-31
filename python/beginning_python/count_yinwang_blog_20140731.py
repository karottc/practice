#!/usr/local/bin/python
#coding=UTF-8

from urllib import urlopen

import re

p = re.compile('<a href="http://yinwang\\.org/(.*?)">(.*?)</a>')
website = 'http://www.yinwang.org/'
text = urlopen(website).read()

"""
print
print '======================================================'

# 输出对应的每篇的blog标题和URL。
for url, name in p.findall(text):
	print 'name =', name
	print 'url = http://yinwang.org/%s' % url
	print
	print

print '======================================================'
"""
print
count = len(p.findall(text))
print 'total count: %d pieces blog !' % count 

### 20140731: total count: 54 pieces !