import sqlite3
conn=sqlite3.connect('my_database.db')
import datetime

    # function to insert all the input given by the user

def insert():
    A=int(input("Enter the uid  "))
    B=input("Enter the product_title  ")
    date_entry = input('Enter a date in YYYY-MM-DD format  ')
    year, month, day = map(int, date_entry.split('-'))
    date = datetime.date(year, month, day)
    C = input("Enter the dop  ")
    D = int(input("Enter the mrp  "))
    E = float(input("Enter the sp  "))
    c = conn.cursor()
    c.execute("INSERT INTO product(  uid,  Product_Title,  dop,  Product_Desc,  mrp,  sp) VALUES ( ?, ?, ?, ?, ?, ?)",(  A,  B,  date,  C ,  D,  E))
    c.execute("SELECT*FROM product")
    print(*c.fetchall(),sep='\n')
conn.commit()

insert()

   #function to delete an item that is no longer required

def delete():
     c=conn.cursor()
     c.execute("DELETE* FROM product")
conn.commit()
del()

  #confirmation of data insertion

print('Data inserted..')
    #c.execute("SELECT*FROM product")
    #print(*c.fetchall(),sep='\n')
#conn.commit()
conn.close()
