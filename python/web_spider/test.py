#coding=UTF-8
__author__ = 'chenyang6'
import urllib
import urllib2
import json
import copy

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

headers = {"User-agent": user_agent}

#url = "http://news-at.zhihu.com/api/4/story/4683248"
# url = "http://news-at.zhihu.com/api/4/section/2"
#url = "http://news-at.zhihu.com/api/4/story/4728744"
#url = "http://news-at.zhihu.com/api/4/section/2"

listDebunkUrl = "http://news-at.zhihu.com/api/4/section/2"
request = urllib2.Request(listDebunkUrl, headers=headers)
response = urllib2.urlopen(request)
content = json.loads(response.read())
endTime = content['timestamp'] + 30 * 60   # 延后半小时
startTime = endTime + (len(content['stories']) - 1) * 24 * 3600
print 'start=%d, end=%d' % (startTime,endTime)
print content['stories'][0]['id']
print content['stories'][0]['display_date']
print content['stories'][0]['date']
print content['stories'][0]['title']
testTemp = content['stories'][0]['images'][0]  # 小图
print testTemp

url = "http://news-at.zhihu.com/api/4/story/%s" % content["stories"][0]["id"]

url = 'http://news-at.zhihu.com/api/4/story/4742059'  #这种情况要特殊处理，这个是2015.05.18的吐槽形式
#url = "http://news-at.zhihu.com/api/4/story/4728744"
#url = "http://news-at.zhihu.com/api/4/story/4683248"
#url = "http://news-at.zhihu.com/api/4/story/4740087"   # 这一条插入数据看失败了，为什么吖。。。啊啊啊
#url = "http://news-at.zhihu.com/api/4/story/375"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

content = json.loads(response.read())
body = content['body'].replace('\r','')
#print body
bodylines = body.split('\n')

i = 0
flagAnswer = 0
listAnswer = []
dictAnswer = {}
answer = ""
for line in bodylines:
    if line.find('<h2 class="question-title">') != -1:
        title = line.replace('<h2 class="question-title">','')
        title = title.replace('</h2>','')
        #dictAnswer['title'] = title
        continue
    if line.find('<img class="avatar"') != -1:
        avatar = line.replace('<img class="avatar" src="','')
        avatar = avatar.replace('">','')
        dictAnswer['avatar'] = avatar
        continue
    if line.find('<span class="author">') != -1:
        tempList = line.split('span')
        author = tempList[1].replace(' class="author">','')
        # 区分有无个性签名的情况
        if line.find('bio') != -1:
            author = author.replace('，</','')
            bio = tempList[3].replace(' class="bio">','')
            bio = bio.replace('</','')
        else:
            author = author.replace('</','')
            bio = ""
        dictAnswer['author'] = author
        dictAnswer['bio'] = bio
    if line == '<div class="content">':
        flagAnswer = 1
    elif flagAnswer == 1 and line != '</div>':
        #str = "%s\n" % line
        line = line.replace('<p>','')
        line = line.replace('</p>','')
        line = line.replace('&hellip;', '...')
        if line.find('<img class="content-image"') != -1:
            tempList = line.split('"')
            line = '<img src="%s" />' % tempList[3]
        answer += "%s\n" % line
        #print line
    elif flagAnswer == 1 and line == '</div>':
        dictAnswer['answer'] = answer
        listAnswer.append(copy.deepcopy(dictAnswer))
        dictAnswer.clear()
        flagAnswer = 0
        answer = ""
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
        strAnswer = json.dumps(listAnswer, ensure_ascii=False)
        print 'answer:%s' % strAnswer
        l = json.loads(strAnswer)
        print '*****************************************************'
        print len(l)
        print '*****************************************************'
        for listan in l:
            print "Autor:%s (%s) - %s" % (listan['author'], listan['avatar'],listan['bio'])
            print "answer:%s" % listan['answer']
            print '*****************************************************'

        print "view-more: %s" % moreUrl
        print '------------------------------'
        answer = ""
        del listAnswer[:]


print "======================================"
# 2015.05.18 就没有recommender
if content.has_key('recommenders'):
    for val in content["recommenders"]:
        print val["avatar"]
print "======================================"
print content["section"]["thumbnail"]    # 小图
print "======================================"
print content["image"]     # 大图
