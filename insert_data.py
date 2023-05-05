import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='manju')
cur=mydb.cursor()
z='insert into employee(emp_id,emp_name,salary) values(%s,%s,%s)'
a=(102,'chandu',29000)
cur.execute(z,a)
mydb.commit()
print('data inserted succesfully')