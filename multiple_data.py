import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='manju')
cur=mydb.cursor()
z='insert into employee(emp_id,emp_name,salary) values(%s,%s,%s)'
a=[(103,'priya',40000),(105,'swapna',45000)]
cur.executemany(z,a)
mydb.commit()
print("inserted successfully")
