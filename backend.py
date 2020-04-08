# import the sqlite3 module, to work with local .db files
import sqlite3

# database class
class Database:
    # constructor
    # create table, and initialize cursor 
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cursor= self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
        self.conn.commit()

    # insert record
    def insert_record(self,title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
    # view all records
    def view_all(self):
        self.cursor.execute("SELECT * FROM books")
        data = self.cursor.fetchall()
        return data

    # search for a record
    def search_records(self,title="",author="",year="",isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?)",(title,author,year,isbn))
        data = self.cursor.fetchall()
        return data
    # delete records
    def delete_records(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?",(id,))
        self.cursor.commit()
    # update records
    def update_records(self, id,title,author,year,isbn):
        self.cursor.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.cursor.commit()
    # when object is destroyed
    # close DB connection
    def __del__(self): # __del__ is system name, just like __init__
        self.conn.close()