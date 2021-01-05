import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()


c.execute("""CREATE TABLE user(
    uid integer PRIMARY KEY AUTOINCREMENT,
    FirstName text,
    LastName text,
    Mobile_Number integer,
    email text,
    state text,
    city text,
    password text,
    buy_list text DEFAULT '-1')""")
    #buy_list (pid) :- the products which user wants to buy
  
c.execute("""CREATE TABLE product(
    pid integer PRIMARY KEY AUTOINCREMENT,
    uid integer,
    Product_Title text,
    dop text,
    Product_Desc text,
    buyer_list text DEFAULT '-1',
    mrp real,
    sp real)""")
    #buyer_list (uid) :- users who want to buy this product

c.execute("INSERT INTO user(FirstName, LastName, Mobile_Number, email, password, city, state) VALUES ('Vaibhav', 'Gupta', 17546545645, 'vaibh@gmail.com', 'Vaibh321@', 'LUCKNOW', 'UTTAR PRADESH')")
c.execute("INSERT INTO user(FirstName, LastName, Mobile_Number, email, password, city, state) VALUES ('Aatmsaat', 'Gupta', 17546545645, 'aatm@gmail.com', 'Vaib12$', 'KANPUR', 'UTTAR PRADESH')")
c.execute("INSERT INTO user(FirstName, LastName, Mobile_Number, email, password, city, state) VALUES ('bittu', 'singh', 17546545645, 'bittu@gmail.com', 'Bittu786@', 'PRAYAGRAJ', 'UTTAR PRADESH')")
conn.commit()
c.execute("INSERT INTO product(uid, Product_Title, dop, Product_Desc, mrp, sp) VALUES (2, 'Smart Phone', '2017-03-05', 'This mobile works absolutely fine', 5000, 1300.50)")
c.execute("INSERT INTO product(uid, Product_Title, dop, Product_Desc, mrp, sp) VALUES (2, 'bicycle', '2010-03-05', 'This bicycle good for fitness', 4000, 895)")

conn.commit()
conn.close()
print('DataBase Created!')