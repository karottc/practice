#coding=UTF-8
__author__ = 'k'

# 抓取知乎每日吐槽
import urllib
import urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# url1 = "http://news-at.zhihu.com/api/4/story/4674201"
listDebunkUrl = "http://news-at.zhihu.com/api/4/section/2"

# authorization = "earer lQ65zm3DSKOOuWPu2WqHfg"
# user_agent = "ZhihuApi/1.0.0-beta (Linux; Android 4.4.4; HM NOTE 1LTE Build/Xiaomi/dior/dior/KTU84P/zh_CN)"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

headers = {"User-agent": user_agent}

try:
    request = urllib2.Request(listDebunkUrl, headers=headers)
    response = urllib2.urlopen(request)
    content = json.loads(response.read())
    #print content
    print "start time: %s" % content["timestamp"]
    # print content["stories"][0]["images"]
    storyUrl = "http://news-at.zhihu.com/api/4/story/%s" % content["stories"][0]["id"]
    print storyUrl
    storyRequest = urllib2.Request(storyUrl, headers=headers)
    storyResponse = urllib2.urlopen(storyRequest)
    print storyResponse.read()
    '''
    for val in content["stories"]:
        #print val["id"]
        #print "日期：%s, http://news-at.zhihu.com/api/4/story/%s" % (val["display_date"],val["id"])
        storyUrl = "http://news-at.zhihu.com/api/4/story/%s" % val["id"]
        storyRequest = urllib2.Request(storyUrl,headers=headers)
        storyResponse = urllib2.urlopen(storyRequest)
        print storyResponse.read()
        print "==================================================="
    '''
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason