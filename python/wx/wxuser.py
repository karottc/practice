#!/usr/bin/env python
# coding=utf-8

__author__ = 'k'

import os
import urllib, urllib2
import re
import cookielib
import time
import xml.dom.minidom
import json
import sys

QRImagePath = os.getcwd() + '/qrcode.jpg'
ICONPath = os.getcwd() + "/wxicon/"
g_UUID = ""
g_tip = 0    # 未扫描tip 为0，扫描之后为1
g_base_uri = ""
g_redirect_uri = ""
g_skey = ""
g_wxsid = ""
g_wxuin = ""
g_pass_ticket = ""
g_deviceId = "e000000000000000"
g_BaseRequest = {}
g_ContactList = []
g_My = {}


def getUUID():
    global g_UUID
    url = 'https://login.weixin.qq.com/jslogin'
    params = {
        'appid': 'wx782c26e4c19acffb',                 # 这个appid好像是固定的一个
        'fun': 'new',
        'lang': 'zh_CN',
        '_': int(time.time()),
    }
    request = urllib2.Request(url = url, data = urllib.urlencode(params))
    response = urllib2.urlopen(request)
    data = response.read()
    # print data
    # window.QRLogin.code = 200; window.QRLogin.uuid = "oZwt_bFfRg==";
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
    pm = re.search(regx, data)
    code = pm.group(1)
    g_UUID = pm.group(2)
    print "uuid: %s" % g_UUID
    if code == '200':
        return True
    return False

def showQRImage():
    global g_tip
    url = 'https://login.weixin.qq.com/qrcode/' + g_UUID
    params = {
        't': 'webwx',
        '_': int(time.time()),
    }
    request = urllib2.Request(url = url, data = urllib.urlencode(params))
    response = urllib2.urlopen(request)
    respContent = response.read()  # 此处获取的就是二进制图片流
    g_tip = 1
    f = open(QRImagePath, 'wb')
    f.write(respContent)
    f.close()
    #print respContent
    if sys.platform == 'win32':
        os.system('call %s' % QRImagePath)
    else:
        os.system('open %s' % QRImagePath)
    print '请使用微信扫描二维码以登录，%s' % QRImagePath

def waitForLogin():
    global g_tip, g_base_uri, g_redirect_uri
    url = 'https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s' % (g_tip, g_UUID, int(time.time()))
    request = urllib2.Request(url = url)
    response = urllib2.urlopen(request)
    data = response.read()
    # print data
    # window.code=500;
    regx = r'window.code=(\d+);'
    pm = re.search(regx, data)
    code = pm.group(1)
    if code == '201': #已扫描
        print '成功扫描,请在手机上点击确认以登录'
        g_tip = 0
    elif code == '200': #已登录
        print '正在登录...'
        regx = r'window.redirect_uri="(\S+?)";'
        print "data:%s" % data
        pm = re.search(regx, data)
        g_redirect_uri = pm.group(1) + '&fun=new'
        g_base_uri = g_redirect_uri[:g_redirect_uri.rfind('/')]
        print "redirect_uri: %s" % g_redirect_uri
    elif code == '408': #超时
        pass
    # elif code == '400' or code == '500':
    return code

def getLoginStatus():
    global g_skey, g_wxsid, g_wxuin, g_pass_ticket, g_BaseRequest
    request = urllib2.Request(url = g_redirect_uri)
    response = urllib2.urlopen(request)
    data = response.read()
    print "getLoginStatus data: \n%s" % data

    doc = xml.dom.minidom.parseString(data)
    root = doc.documentElement
    for node in root.childNodes:
        if node.nodeName == 'skey':
            g_skey = node.childNodes[0].data
        elif node.nodeName == 'wxsid':
            g_wxsid = node.childNodes[0].data
        elif node.nodeName == 'wxuin':
            g_wxuin = node.childNodes[0].data
        elif node.nodeName == 'pass_ticket':
            g_pass_ticket = node.childNodes[0].data
    print 'skey: %s, wxsid: %s, wxuin: %s, pass_ticket: %s' % (g_skey, g_wxsid, g_wxuin, g_pass_ticket)
    if g_skey == '' or g_wxsid == '' or g_wxuin == '' or g_pass_ticket == '':
        return False
    g_BaseRequest = {
        'Uin': int(g_wxuin),
        'Sid': g_wxsid,
        'Skey': g_skey,
        'DeviceID': g_deviceId,
    }
    return True

def initWXWeb():
    url = g_base_uri + '/webwxinit?pass_ticket=%s&skey=%s&r=%s' % (g_pass_ticket, g_skey, int(time.time()))
    params = {
        'BaseRequest': g_BaseRequest
    }
    request = urllib2.Request(url = url, data = json.dumps(params))
    request.add_header('ContentType', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    data = response.read()
    #f = open(os.getcwd() + '/webwxinit.json', 'wb')
    #f.write(data)
    #f.close()
    # print data
    global g_ContactList, g_My
    dic = json.loads(data)
    #print dic
    g_ContactList = dic['ContactList']
    g_My = dic['User']
    print g_My
    ErrMsg = dic['BaseResponse']['ErrMsg']
    if len(ErrMsg) > 0:
        print ErrMsg
    Ret = dic['BaseResponse']['Ret']
    if Ret != 0:
        return False
    return True

def getWXContact():
    url = g_base_uri + '/webwxgetcontact?pass_ticket=%s&skey=%s&r=%s' % (g_pass_ticket, g_skey, int(time.time()))
    request = urllib2.Request(url = url)
    request.add_header('ContentType', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    data = response.read()
    #f = open(os.getcwd() + '/webwxgetcontact.json', 'wb')
    #f.write(data)
    #f.close()
    # print data
    dic = json.loads(data)
    MemberList = dic['MemberList']
    # 倒序遍历,不然删除的时候出问题..
    num1 = 0
    SpecialUsers = ['newsapp', 'fmessage', 'filehelper', 'weibo', 'qqmail', 'fmessage', 'tmessage', 'qmessage', 'qqsync', 'floatbottle', 'lbsapp', 'shakeapp', 'medianote', 'qqfriend', 'readerapp', 'blogapp', 'facebookapp', 'masssendapp', 'meishiapp', 'feedsapp', 'voip', 'blogappweixin', 'weixin', 'brandsessionholder', 'weixinreminder', 'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c', 'officialaccounts', 'notification_messages', 'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c', 'wxitil', 'userexperience_alarm', 'notification_messages']
    for i in xrange(len(MemberList) - 1, -1, -1):
        Member = MemberList[i]
        if Member['VerifyFlag'] & 8 != 0: # 公众号/服务号
            num1 += 1
            MemberList.remove(Member)
        elif Member['UserName'] in SpecialUsers: # 特殊账号
            MemberList.remove(Member)
        elif Member['UserName'].find('@@') != -1: # 群聊
            MemberList.remove(Member)
        elif Member['UserName'] == g_My['UserName']: # 自己
            MemberList.remove(Member)
    print "公众号数量: %d" % num1
    return MemberList

def analysisSnsFlag(memberList):
    dictFlag = {}
    for member in memberList:
        if dictFlag.has_key(member["SnsFlag"]) == True:
            dictFlag[member["SnsFlag"]].add(member["NickName"])
        else:
            setName = set()
            setName.add(member["NickName"])
            dictFlag[member["SnsFlag"]] = setName

    for (flag, nameList) in dictFlag.items():
        print "\t snsflag:%s" % flag
        strName = ""
        for name in nameList:
           strName += name + "|"
        print strName
        print "**********************************************************"

def analysisContactFlag(memberList):
    dictFlag = {}
    dictIcon = {}
    for member in memberList:
        if dictFlag.has_key(member["ContactFlag"]) == True:
            dictFlag[member["ContactFlag"]].add(member["NickName"])
            dictIcon[member["ContactFlag"]].add(member["UserName"])
        else:
            setName = set()
            setName.add(member["NickName"])
            dictFlag[member["ContactFlag"]] = setName
            setIcon = set()
            setIcon.add(member["UserName"])
            dictIcon[member["ContactFlag"]] = setIcon

    for (flag, nameList) in dictFlag.items():
        print "\t ContactFlag:%s" % flag
        strName = ""
        for name in nameList:
           strName += name + "|"
        print strName
        print "**********************************************************"

    i = 0
    f = open(os.getcwd() + '/contactFlag.html', 'wb')
    data = "<html><head><title>users</title></head><body>"
    for (flag, iconList) in dictIcon.items():
        data += "<br/><h2>ContactFlag: %s</h2><br />" % flag
        for icon in iconList:
            i += 1
            data += '''<img id='image%d' src='wxicon/%s.jpg' </img>''' % (i, icon)
    data += "</body>"
    f.write(data)
    f.close()

def getAllIcon(memberList):
    baseIconurl = "https://wx.qq.com"
    for member in memberList:
        url = baseIconurl + member["HeadImgUrl"]
        request = urllib2.Request(url = url)
        response = urllib2.urlopen(request)
        respContent = response.read()  # 此处获取的就是二进制图片流
        fileName = ICONPath + member["UserName"] + ".jpg"
        f = open(fileName, 'wb')
        f.write(respContent)
        f.close()

def getAllUserIcon(memberList):
    i = 0
    f = open(os.getcwd() + '/WXALLUser.html', 'wb')
    data = "<html><head><title>users</title></head><body>"
    for member in memberList:
        i += 1
        data += '''<img id='image%d' src='wxicon/%s.jpg' </img>''' % (i, member["UserName"])
    data += "</body>"
    f.write(data)
    f.close()


def main():
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    if getUUID() == False:
        print "获取 UUID 失败"
        return
    showQRImage()
    while waitForLogin() != '200':
        pass
    os.remove(QRImagePath)    # 删除登录的二维码
    if getLoginStatus() == False:
        print "登录失败"
        return
    if initWXWeb() == False:
        print "初始化微信好友列表失败"
        return
    memberList = getWXContact()
    print "共有 %d 位好友" % len(memberList)
    getAllIcon(memberList)
    #analysisSnsFlag(memberList)
    #analysisContactFlag(memberList)
    getAllUserIcon(memberList)





# 获取微信用户画像
if __name__ == '__main__' :
    main()