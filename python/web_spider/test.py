#coding=UTF-8
__author__ = 'chenyang6'
import urllib
import urllib2
import json

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

headers = {"User-agent": user_agent}

url = "http://news-at.zhihu.com/api/4/story/4679479"
# url = "http://news-at.zhihu.com/api/4/section/2"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

content = json.loads(response.read())

print content['body']
print "======================================"
for val in content["recommenders"]:
    print val["avatar"]
print "======================================"
print content["section"]["thumbnail"]
print "======================================"
print content["image"]