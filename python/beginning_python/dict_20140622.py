#!/usr/local/bin/python
#coding=UTF-8

print

# dict函数
items = [('name','Gumby'),('age',42)]
d = dict(items)
print d
print

d = dict(name='Gumby',age=42)
print d
print

x = {}
x[42] = 'Foobar'
print x
print

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

# 针对电话号码和地址使用描述性标签，输出的时候会用到
labels = {
        'phone': 'phone number',
        'addr': 'address'
        }

name = raw_input('Name: ')
# 查找电话号码还是地址？使用正确的键
request = raw_input('Phone number(p) or address(a)? ')
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# 名字是字典中有效信息就输出
if name in people: print "%s's %s is %s. " % \
        (name, labels[key], people[name][key])
