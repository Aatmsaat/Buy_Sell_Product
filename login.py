import sqlite3
import re

conn = sqlite3.connect('my_database.db')

c = conn.cursor()

# Function to create a new user account
def signup():
    print("\nPlease enter the following detail")
    
    fname, lname, mob, email, pasw, city, state = [None]*7
    
    # validation and inputs
    
    while True:
        fname = input("Enter first name: ")
        if fname.strip().count(' ') == 0:
            break
        print('Enter only your first name!')
        
    while True:
        lname = input("Enter last name: ")
        if lname.strip().count(' ') == 0:
            break
        print('Enter only your last name!')
    
    while True:
        mob = input("Enter mobile number: ")
        mob_len = len(mob)
        if mob_len == 10:
            mob = int(mob)
            break
        print('mobile number must be of only 10 digits')
            
    while True:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email = input("Enter email: ")
        if(re.search(regex,email)):
            c.execute('SELECT uid FROM user WHERE email = "{email}"')
            if c.fetchone():
                print('This Email has already account!')
            else:
                break
        else:
            print('invalid email!')
        
    while True:
        print('For password')
        print('length should be at least 6')
        print('length should be not be greater than 20')
        print('Password should have at least one numeral') 
        print('Password should have at least one uppercase letter') 
        print('Password should have at least one lowercase letter') 
        print('Password should have at least one of the symbols $@#')
        pasw = input("Enter password: ")
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg) 
        if re.search(pat, pasw):
            break
        print('Invalid password!')
    
    state = input("Enter full name of state: ").upper()
    city = input("Enter full name of city: ").upper()
    
    c.execute("INSERT INTO user(FirstName, LastName, Mobile_Number, email, password, state, city) VALUES (?, ?, ?, ?, ?, ?, ?)", (fname, lname, mob, email, pasw, state, city))
    conn.commit()
    print('Welcome ', fname, lname)
    c.execute(f"SELECT uid FROM user WHERE email = '{email}'")
    (uid, ) = c.fetchone()
    return uid
   
# Function for login system

def login():
    print("Please enter the login detail\n")
    while True:
        email = input("Email: ")
        pasw = input("Password: ")
        var_select = []
        var_select.append(email)
        var_select.append(pasw)
        sql = 'SELECT uid, FirstName, LastName FROM user WHERE email = ? AND password = ?'
        c.execute(sql, var_select)
        result = c.fetchone()
        if result:
            uid, fname, lname = result
            print('Welcome', fname, lname)
            return uid
        else:
            print('Either invalid email/password ')

# testing functions
    
if __name__ == '__main__':
    print(signup())
    print(login())
