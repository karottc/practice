#!/usr/local/bin/python
# coding=UTF-8

# 检查用户名和PIN码

database = [
        ['albert', '1234'],
        ['dilbert', '4142'],
        ['simth', '7524'],
        ['jones', '9843']
    ]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database: print 'Access granted ! '
