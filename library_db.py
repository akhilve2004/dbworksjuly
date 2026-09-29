import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")

        self.cursor=self.con.cursor()

    def list(self,request):

        pass

    def create(self,request):

        pass

    def retrielibrary_db.pylibrary_db.pyve(self,request, id):

        pass

    def update(self,request,id):

        pass

    def delete(self,request,id):

        pass

    book_instance=BookListCreateRetrieveUpdateDelete()

    book_instance.list()




