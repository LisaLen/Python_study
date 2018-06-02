import json
import sqlite3

conn = sqlite3.connect('rosterDB.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE);

CREATE TABLE Course (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE);

CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY(user_id,course_id))
''')

fn = input('Enter JSON file name: ')
if len(fn) < 1: fn = 'roster_data.json'
fhand = open(fn).read()
info = json.loads(fhand)

for entry in info:
    name = entry[0]
    course = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    cur.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(course,))
    cur.execute('SELECT id FROM Course WHERE title =?',(course,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role)
                VALUES (?,?,?)''',(user_id,course_id,role))

    conn.commit()
