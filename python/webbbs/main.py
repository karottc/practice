#coding=UTF-8
print 'Content-type: text/html\n'

import cgitb; cgitb.enable()

import sqlite3

__metaclass__=type

#dbName = "messages.db"
#conn = sqlite3.connect(dbName)

db = '''
    CREATE TABLE messages(
    id        integer primary key autoincrement,
    subject   text not null,
    sender    text not null,
    reply_to  text not null,
    text      text not null
    )
    '''

class Database:
    def __init__(self):
        self.dbName = "messages.db"
        self.conn = sqlite3.connect(self.dbName)
        curs = self.conn.cursor()

        curs.execute(db)

        self.conn.commit()
        curs.close()

    def insertDB(self,msg):
        curs = self.conn.cursor()

        if msg['reply_to']:
            query = """
            INSERT INTO message(reply_to, sender, subject, text) VALUES(%s, %s, %s, %s)
            """ % (msg['reply_to'], msg['sender'], msg['subject'], msg['text'])
        else:
            query = """
            INSERT INTO message(sender, subject, text) VALUES(%s, %s, %s)
            """ % (msg['sender'], msg['subject'], msg['text'])

        curs.execute(query)

        self.conn.commit()
        curs.close()

    def queryDBPart(self, query):
        curs = self.conn.cursor()
        curs.execute(query)
        names = [d[0] for d in curs.description]
        rows = [dict(zip(names, row)) for row in curs.fetchall()]

        return rows

    def queryDBAll(self):
        curs = self.conn.cursor()
        query = 'SELECT * FROM messages'
        curs.execute(query)
        names = [d[0] for d in curs.description]
        rows = [dict(zip(names,row)) for row in curs.fetchall()]

        return rows

    def __del__(self):
        self.conn.close()

messages = Database()
toplevel = []
children = {}

def htmlHead():
    print """
    <html>
        <head>
            <title>The FooBar Bulletin Board</title>
        </head>
        <body>
            <h1>The FooBar Bulletin Board</h1>
    """
    rows = messages.queryDBAll()

    for row in rows:
        parent_id = row['reply_to']
        if parent_id is None:
            toplevel.append(row)
        else:
            children.setdefault(parent_id,[]).append(row)

def format(row):
    print '<p><a href="view.py?id=%(id)i">%(subject)s</a></p>' % row
    try:
        kids = children[row['id']]
    except KeyError:
        pass
    else:
        print '<blockquote>'
        for kid in kids:
            format(kid)
        print '</blockquote>'

def htmlRoot():
    print '<p>'
    for row in toplevel:
        format(row)
    print """
        </p>
        <hr />
        <p><a href="edit.py">Post message</a></p>
    </body>
    </html>
    """