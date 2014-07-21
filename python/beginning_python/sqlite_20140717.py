#!/usr/local/bin/python
#coding=UTF-8

# 一般流程示例
import sqlite3
"""
conn = sqlite3.connect('somedatabase.db')
curs = conn.cursor()
conn.commit()
conn.close()
"""

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food(
    id          TEXT        PRIMARY KEY,
    desc        TEXT,
    walter      TEXT,
    kcal        FLOAT,
    protein     FLOAT,
    fat         FLOAT,
    ash         FLOAT,
    carbs       FLOAT,
    fiber       FLOAT,
    sugar       FLOAT
)
''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

field_count = 10

for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    #print vals
    curs.execute(query,vals)

conn.commit()
conn.close()
