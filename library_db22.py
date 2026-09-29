import mysql.connector
class BookListRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="root",
                                         host="localhost",database="library_db22")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")

b=BookListRetrieveUpdateDelete
