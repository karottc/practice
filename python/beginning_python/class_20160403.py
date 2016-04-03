#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class CTestField(object):
    '''
    测试的结果，下面的成员变量并不是所有实例共享的静态成员变量
    '''
    m_name = "init name"
    m_age = 0
    m_length = 0


t1 = CTestField()
t1.m_name = "karottc"
t1.m_age = 1
t1.m_length = 5

t2 = CTestField()
t2.m_name = "test name"

print t2.m_name,t2.m_age,t2.m_length
print t1.m_name,t1.m_age,t1.m_length


