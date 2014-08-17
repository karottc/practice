#coding=UTF-8

print 'Content-type: text/html\n'

import cgitb;cgitb.enable()

def quote(string):
    if string:
        return string.replace("'", "\\'")
    else:
        return string

import sqlite3
import main

import cgi,sys
form = cgi.FieldStorage()

sender = quote(form.getvalue('sender'))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue('text'))
reply_to = quote(form.getvalue('reply_to'))

if not (sender and subject and text):
    print 'Please supply sender, subject, and text'
    sys.exit()

msg = {}
msg['sender'] = sender
msg['subject'] = subject
msg['text'] = text
if reply_to is not None:
    msg['reply_to'] = reply_to
else:
    msg['reply_to'] = None

main.messages.insertDB(msg)

print """
<html>
    <head>
        <title>Message Saved</title>
    </head>
    <body>
        <h1>Message saved</h1>
        <hr />
        <a href='main.py'>Back to the main page</a>
    </body>
</html>s
"""