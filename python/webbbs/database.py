#coding=UTF-8

import sqlite3

# 建立电子公告板的数据库
# 数据库的名字：message

"""
id: 用于标识唯一的消息;
subject: 包括消息主题;
reply_to: 如果消息是回复其他消息，那么这个字段就包括那个消息id(否则字段是空的);
sender：包括发送者名字、Email地址或者其他信息的字符串;
text: 包括消息内容的字符串。
"""
db = '''
    CREATE TABLE message(
    id        integer primary key autoincrement,
    subject   text not null,
    sender    text not null,
    reply_to  text not null,
    text      text not null
    )
    '''
dbName = 'message.db'

def createDB():
    conn = sqlite3.connect(dbName)
    curs = conn.cursor()

    curs.execute(db)

    # 往数据库里面灌水，这样可以读出一些数据
    temp = [
        ('test','test','test','test'),
        ('test2','test2','test2','test2'),
        ('test3','test3','test3','test3'),
        ('test4','test4','test4','test4'),
        ('test5','test5','test5','test5'),
        ('test6','test6','test6','test6'),
        ('test7','test7','test7','test7'),
        ('test8','test8','test8','test8')
        ]
    #insert = 'INSERT INTO message VALUES (?, ?, ?, ?)'  ### 这种语句是错误的，虽然第一个字段ID是自增加的，但也需要使用下面的形式。
    insert = 'INSERT INTO message(subject, sender, reply_to, text) VALUES (?, ?, ?, ?)'

    for value in temp:
        conn.execute(insert,value)

    conn.commit()
    conn.close()

def insertDB(msg):
    conn = sqlite3.connect(dbName)
    curs = conn.cursor()

    if msg['reply_to']:
        query = """
        INSERT INTO message(reply_to, sender, subject, text) VALUES(%s, %s, %s, %s)
        """ % (msg['reply_to'], msg['sender'], msg['subject'], msg['text'])
    else:
        query = """
        INSERT INTO message(sender, subject, text) VALUES(%s, %s, %s)
        """ % (msg['sender'], msg['subject'], msg['text'])

    curs.execute(query)
    curs.commit()
    curs.close()

def deleteDB():
    pass

def test():
    conn = sqlite3.connect(dbName)
    curs = conn.cursor()

    query = 'SELECT * FROM message'

    curs.execute(query)

    names = [d[0] for d in curs.description]
    rows = [dict(zip(names, row)) for row in curs.fetchall()]
    print   '-------------------------------------------'
    for row in rows:
        print 'id:', row['id']
        print 'subject:', row['subject']
        print 'sender:', row['sender']
        print 'reply_to:', row['reply_to']
        print 'text:', row['text']
        print '-------------------------------------------'

    #conn.commit()   查询数据库，这句好像没什么用
    conn.close()

test()

#if __name__ == '__main__':
#    createDB()