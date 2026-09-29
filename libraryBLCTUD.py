import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="root",host="localhost",database="library_db"
        )
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")