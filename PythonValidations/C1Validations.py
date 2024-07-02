'''q: what is the implementation steps required to connect a python program to a database?'''
# 1. import the module
# 2. establish the connection
# 3. create a cursor object
# 4. execute the sql statement
# 5. commit the changes
# 6. close the connection
''''q: provide an example to connect to a database'''
# import sqlite3
# conn = sqlite3.connect('mydb.db')
# c = conn.cursor()
# c.execute('create table if not exists students (id integer primary key, name text, age integer)')
# c.execute('insert into students values (1, "john", 22)')
# conn.commit()
# conn.close()

