#coding=UTF-8
__author__ = 'k'

# 抓取知乎每日吐槽
import urllib
import urllib2

# url1 = "http://news-at.zhihu.com/api/4/story/4674201"
listDebunkUrl = "http://news-at.zhihu.com/api/4/section/2"

#authorization = "earer lQ65zm3DSKOOuWPu2WqHfg"
#user_agent = "ZhihuApi/1.0.0-beta (Linux; Android 4.4.4; HM NOTE 1LTE Build/Xiaomi/dior/dior/KTU84P/zh_CN)"
user_agent = "ozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

headers = {"User-agent" : user_agent}

try:
    request = urllib2.Request(listDebunkUrl, headers=headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason