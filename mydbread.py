import mysql.connector

con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db1")

print(con)

c=con.cursor()

query="select * from student"

c.execute(query)

records=c.fetchall()

if records:
    for row in records:
        print(row)

else:
    print("no record found")

c.close()

con.close()
