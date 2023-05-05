import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='manju')
cur=mydb.cursor()
f='select * from employee'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)