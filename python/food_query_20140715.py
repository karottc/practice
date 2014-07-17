#!/usr/local/bin/python
#coding=UTF-8

# 查询sqlite_20140717.py执行后的结果
import sqlite3,sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]
#query = 'SELECT * FROM food'
print query
curs.execute(query)
names = [f[0] for f in curs.description]
print names
total = 0;
#print curs.fetchall()
for row in curs.fetchall():
    total += 1
    for pair in zip(names, row):
        print '%s: %s' % pair
    print

print '共查询到 %d 条记录！' % total
conn.close()
