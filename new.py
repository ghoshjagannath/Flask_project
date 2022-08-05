import sqlite3

conn=sqlite3.connect(r'C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project\password.db')

cur=conn.cursor()


cur.execute('insert into user_list(name,pass) values(?,?)',('Jagannath ghosh','iamironman03'))

conn.commit()

x=cur.execute(
            'select * from user_list')

print(list(x))
conn.close()