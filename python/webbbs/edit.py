#coding=UTF-8

print 'Content-type: text/html\n'

import cgitb;cgitb.enable()

import sqlite3
import main

import cgi,sys
form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')

print """
<html>
    <head>
        <title>Compose Message</title>
    </head>
    <body>
        <h1>Compose Message</h1>

        <form action='save.py' method='POST'>
"""

subject = ''
if reply_to is not None:
    print '<input type="hidden" name"reply_to" value="%s"/>' % reply_to
    query = 'SELECT subject FROM messages WHERE id = %s' % reply_to
    subject = main.messages.queryDBPart(query)[0]
    if not subject.startvith('Re: '):
        subject = 'Re: ' + subject

print """
    <b>Subject:</b><br />
    <input type='text' size='40' name='subject' value='%s' /><br />
    <b>Sender:</b><br />
    <input type='text' size='40' name='sender' /><br />
    <b>Message:</b><br />
    <textarea name='text' cols='40' rows='20'></textarea><br />
    <input type='sbumit' value='Save' />
    </form>
    <hr />
    <a href='main.py'>Back to the main page</a>
  </body>
</html>
""" % subject