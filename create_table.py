import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='manju')
cur=mydb.cursor()
t='create table employee(emp_id integer(4),emp_name varchar(30),salary integer(10))'
cur.execute(t)