import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE user(
    uid integer PRIMARY KEY AUTOINCREMENT,
    FirstName text,
    LastName text,
    Moblie_Number integer,
    email text,
    password text,
    city text,
    state text)""")

c.execute("INSERT INTO user(FirstName, LastName, Moblie_Number, email, password, city, state) VALUES ('Vaibhav', 'Gupta', 17546545645, 'dsfs@gmail.com', 'vai12345','lucknow', 'Uttar Pradesh')")
c.execute("INSERT INTO user(FirstName, LastName, Moblie_Number, email, password, city, state) VALUES ('Aatmsaat', 'Gupta', 17546545645, 'dsfs@gmail.com', 'aat12345', 'kanpur', 'Uttar Pradesh')")
c.execute("INSERT INTO user(FirstName, LastName, Moblie_Number, email, password, city, state) VALUES ('bittu', 'singh', 17546545645, 'dsfs@gmail.com', 'bit12345','alahabaad', 'Uttar Pradesh')")
conn.commit()

# Function to create a new user account
def signup():
    print("\nPlease enter the following detail")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    mob = int(input("Enter mobile number: "))
    email = input("Enter email: ")
    pasw = input("Enter password: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    var_insert = []
    var_insert.append(fname)
    var_insert.append(lname)
    var_insert.append(mob)
    var_insert.append(email)
    var_insert.append(pasw)
    var_insert.append(city)
    var_insert.append(state)
    with sqlite3.connect(':memory:') as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO user(FirstName, LastName, Moblie_Number, email, password, city, state) VALUES (?,?,?,?,?,?,?);", var_insert)
        print("Inserted")
        db.commit()


# Function for login system
def login():
    print("Please enter the login detail\n")
    email = input("Email: ")
    pasw = input("Password: ")
    var_select = []
    var_select.append(email)
    var_select.append(pasw)
    with sqlite3.connect(':memory:') as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM user WHERE email = ? AND passsword = ?';
        cursor.execute(sql, var_select)
        result = cursor.fetchall()
        for row in result:
            print(str(row))

# Startup of program to execute
while True:
    print("User Login consol\n1.Signup\n2.Login\n3.Exit")
    n = int(input())
    if(n==1):
        signup()
    elif(n==2):
        login()
    elif(n==3):
        break
    else:
        print("Wrong Input")




    
