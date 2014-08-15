#!/usr/local/bin/python
#coding=UTF-8

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()

import psycopg
conn = psycopg.connect('dbname=foo user=bar')
curs = conn.cursur()

print """
<html>
    <head>
        <title>The FooBar Bulletin Board</title>
    </head>
    <body>
        <h1>The FooBar Bulletin Board</h1>
"""

cur.execute('SELECT * FROM messages')
names = [d[0] for d in curs.description]
row = [dict(zip(names, row)) for row in curs.fetchall()]

toplevel = []
children = {}

for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:
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
    print '<p>'

    for row in toplevel:
        format(row)

    print """
        </p>
    </body>
</html>
"""
