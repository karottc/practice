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

url = "http://news-at.zhihu.com/api/4/story/4683248"
# url = "http://news-at.zhihu.com/api/4/section/2"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

content = json.loads(response.read())

bodylines = content['body'].split('\n')
print content
i = 0
flagAnswer = 0
answer = ""
#print len(bodylines)
print bodylines

for line in bodylines:
    if line.find('<h2 class="question-title">',0,-1) != -1:
        title = line.replace('<h2 class="question-title">','')
        title = title.replace('</h2>','')
        #print 'title:%s' % title
        continue

    if line == '<div class="content">':
        flagAnswer = 1
    elif flagAnswer == 1 and line != '</div>':
        #str = "%s\n" % line
        line = line.replace('<p>','')
        line = line.replace('</p>','')
        line = line.replace('\r','')
        answer += "%s," % line
        #print line
    elif flagAnswer == 1 and line == '</div>':
        flagAnswer = 0
        print "title:%s" % title
        print "answer:%s" % answer
        print '------------------------------'
        answer = ""

print "======================================"
for val in content["recommenders"]:
    print val["avatar"]
print "======================================"
print content["section"]["thumbnail"]
print "======================================"
print content["image"]