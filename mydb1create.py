import mysql.connector

# #establish connection between mysql server and python code
# con=mysql.connector.connect(user="root",password="root",host="localhost")
#
# #it returns connection objects
# print(con)
#
# #cursor object -- for executing sql queries
# c=con.cursor()
#
# query="create database school_db1"
# c.execute(query)
#
# print("database file created")
# c.close()
# con.close()


#creating table
# con=mysql.connector.connect(user="root",
#                              password="root",
#                              host="localhost",
#                              database="school_db1")
# c=con.cursor()
#
# query="""create table student(
#                             roll_no int not null primary key,
#                             name varchar(20),
#                             age int,
#                             place varchar(20),
#                             phone varchar(20),
#                             total_mark int  )""";
#
# c.execute(query)
# print("table created")

#create new record/insert data into database table student
import mysql.connector

con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db1")

print(con)
c=con.cursor()
#insert into tablename(col1,col2,.....)values(val1,val2,....)

query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"

data=(101,"arun",11,"ekm","5757848438",145)

c.execute(query,data)

con.commit() # permantantly save data into database

print("inserted data successfully ")

c.close()
con.close()

















