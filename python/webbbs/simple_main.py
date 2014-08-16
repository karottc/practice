#!/usr/local/bin/python
#coding=UTF-8

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()
import sqlite3

# 做这步操作前保证已经存在了message.db数据库
dbName = 'message.db'
conn = sqlite3.connect(dbName)
curs = conn.cursor()

print """
<html>
    <head>
        <title>The FooBar Bulletin Board</title>
    </head>
    <body>
        <h1>The FooBar Bulletin Board</h1>
"""

curs.execute('SELECT * FROM message')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

toplevel = []
children = {}

for row in rows:
    parent_id = row['reply_to']
    #if parent_id is None:
    if parent_id:
        toplevel.append(row)
    else:
        children.setdefault(parent_id, []).append(row)

def format(row):
    print row['subject']
    try:
        kids = children[row['id']]
    except KeyError:
        pass
    else:
        print '<blockquote>'
        for kid in kids:
            format(kid)
        print '</blockquote>'

print '     <p>'

for row in toplevel:
    format(row)

print """
    </p>
</body>
</html>
"""
