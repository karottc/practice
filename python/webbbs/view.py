#coding=UTF-8

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()

import sqlite3
import main

import cgi, sys
form = cgi.FieldStorage()
id = form.getvalue('id')

print """
<html>
    <head>
        <title>View Message</title>
    </head>
    <body>
        <h1>View Message</h1>
"""

try:
    id = int(id)
except:
    print "Invalid message ID"
    sys.exit()
query = 'SELECT * FROM messages WHERE id = %i' % id
rows = main.messages.queryDBPart(query)

if not rows:
    print 'Unknow message ID'
    sys.exit()

row = rows[0]

print """
    <p><b>Subject:</b>%(subject)s<br />
    <b>Sender:</b>%(sender)s<br />
    <pre>%(text)s</pre>
    </p>
    <hr />
    <a href='main.py'>Back to the main page</a>
    | <a href="edit.py?reply_to=%(id)s">Reply</a>
  </body>
<html>
""" % row