#!/usr/local/bin/python
#coding=UTF-8

print
# find
subject = '$$$ Get rich now !!! $$$'
print subject.find('$$$')
print subject.find('$$$',1)
print subject.find('!!!',0,16)
print

# join
sep = '+'
seq = ['1','2','3','4','5']
print sep.join(seq)
print
dirs = '','usr','bin','env'
print '/'.join(dirs)
print

# lower
name = 'Gumby'
names = ['gumby','smith','jones']
if name.lower() in names: print 'Found it !'
print

# replace\split\strip
print '**** SPAM * for * everyone !!!!***'.strip('*!')
print

# translate
from string import maketrans
table = maketrans('cs','kz')
print len(table)
print table[97:123]
print 'This is an incrediable test'.translate(table)
