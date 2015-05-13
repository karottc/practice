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

#url = "http://news-at.zhihu.com/api/4/story/4683248"
# url = "http://news-at.zhihu.com/api/4/section/2"
url = "http://news-at.zhihu.com/api/4/story/4728744"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

content = json.loads(response.read())
body = content['body'].replace('\r','')

bodylines = body.split('\n')

i = 0
flagAnswer = 0
answer = ""
for line in bodylines:
    if line.find('<h2 class="question-title">') != -1:
        title = line.replace('<h2 class="question-title">','')
        title = title.replace('</h2>','')
        continue
    if line.find('<img class="avatar"') != -1:
        avatar = line.replace('<img class="avatar" src="','')
        avatar = avatar.replace('">','')
        continue
    if line.find('<span class="author">') != -1:
        tempList = line.split('span')
        author = tempList[1].replace(' class="author">','')
        author = author.replace('，</','')
        bio = tempList[3].replace(' class="bio">','')
        bio = bio.replace('</','')
    if line == '<div class="content">':
        flagAnswer = 1
    elif flagAnswer == 1 and line != '</div>':
        #str = "%s\n" % line
        line = line.replace('<p>','')
        line = line.replace('</p>','')
        if line.find('<img class="content-image"') != -1:
            tempList = line.split('"')
            line = '<img src="%s" />' % tempList[3]
        answer += "%s\n" % line
        #print line
    elif flagAnswer == 1 and line == '</div>':
        flagAnswer = 0
        '''
        print "title:%s" % title
        print "Autor:%s (%s) - %s" % (author, avatar,bio)
        print "answer:%s" % answer
        print '------------------------------'
        answer = ""
        '''
        continue
    if line.find('<div class="view-more">') != -1:
        tempList = line.split('"')
        moreUrl = tempList[3]
        print "title:%s" % title
        print "Autor:%s (%s) - %s" % (author, avatar,bio)
        print "answer:%s" % answer
        print "view-more: %s" % moreUrl
        print '------------------------------'
        answer = ""


print "======================================"
for val in content["recommenders"]:
    print val["avatar"]
print "======================================"
print content["section"]["thumbnail"]
print "======================================"
print content["image"]