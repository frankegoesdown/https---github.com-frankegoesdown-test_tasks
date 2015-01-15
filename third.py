# coding: utf-8

#create tables
#CREATE  TABLE "main"."users" ("UID" INTEGER PRIMARY KEY  NOT NULL  UNIQUE , "Name" VARCHAR DEFAULT 255)
#CREATE  TABLE "main"."messages" ("UID" INTEGER, "msg" TEXT check(typeof("msg") = 'text') )

#select data
#SELECT users.Name, count(messages.msg) from users LEFT JOIN messages ON users.UID = messages.UID group by users.Name;
#SELECT name, count(msg)  FROM users LEFT JOIN messages ON users.UID = messages.UID group by Name

import sqlite3

sqlite_file = 'test.sqlite'
table_users = 'users'
table_messages = 'messages'
column_name = 'Name'
column_uid = 'UID'
column_msg = 'msg'

users = ['Платон Щукин', 'Лера Страза', 'Георгий Атласов']
messages = [(1,"Привет, Платон!",), (3,"Срочно пришли карту.",), (3,"Жду на углу Невского и Тверской.",),(1,"Это снова я, пиши чаще",)]
conn = sqlite3.connect(r'test.sqlite')
c = conn.cursor()

for user in users:
	try:
		c.execute("INSERT INTO {tn} ({cn}) VALUES ('{val}')".\
			format(tn=table_users,  cn=column_name, val = user))
		print('user inserted')
	except sqlite3.IntegrityError:
		print('ERROR: ID already exists in PRIMARY KEY column ')


for (uid,msg) in messages:
	try:
		c.execute("INSERT INTO {tn} ({cu},{cm}) VALUES ({uid},'{msg}')".\
			format(tn=table_messages,  cu=column_uid, cm=column_msg, uid=uid,msg = msg))
		print('message inserted')
	except sqlite3.IntegrityError:
		print('ERROR: ID already exists in PRIMARY KEY column ')


conn.commit()
conn.close()


