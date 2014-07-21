#!/usr/local/bin/python
#coding=UTF-8

print

# clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d
returned_value = d.clear()
print d
print returned_value
print

# 使用get()的简单数据库
people = {
        'Alice': {
            'phone': '2341',
            'addr': 'Foo drive 23'
            },
        'Beth': {
            'phone': '3158',
            'addr': 'Bar street 42'
            },
        'Cecil': {
            'phone': '9102',
            'addr': 'Baz avenue 90'
            }
        }

labels = {
        'phone': 'phone number',
        'addr': 'address'
        }

name = raw_input('Name: ')

request = raw_input('Phone number(p) or address(a)? ')

key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# 使用get提供默认值
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')

print "%s's %s is %s." % (name,label,result)
print

# update
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2008'
    }
print d
x = {'title': 'Python language Website'}
d.update(x)
print d
print
