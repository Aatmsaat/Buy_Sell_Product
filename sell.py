import sqlite3
conn=sqlite3.connect('my_database.db')
import datetime
c = conn.cursor()

    # function to insert all the input given by the user

def insert(uid):
    print('\nEnter details for the product\n')
    Prod_Title =input("Enter the Product Title: ")
    Prod_Desc = input("Enter Product Description: ")
    dop = None,
    
    #validate Date
    
    while True:
        dop = input('Enter a date of purchase in YYYY-MM-DD format: ')
        flag = False
        try:
            datetime.datetime.strptime(dop, '%Y-%m-%d')
            flag = True
        except ValueError:
            print('Incorrect Format/Date!')
        if flag:
            break
   
    mrp = float(input("Enter the Marked Price in $: "))
    sp = float(input("Enter the Selling Price in $: "))
    c.execute("INSERT INTO product( uid,  Product_Title,  dop,  Product_Desc,  mrp,  sp) VALUES ( ?, ?, ?, ?, ?, ?)",(uid, Prod_Title, dop, Prod_Desc, mrp, sp))
    conn.commit()
    print("Your product is added to selling list Successfully!")
    
def sell_list(uid):
    while True:
        c.execute(f"SELECT pid, Product_Title, Product_Desc, dop, mrp, sp FROM product WHERE uid = {uid}")
        products = c.fetchall()
        if not products:
            print('You have not placed any product for sale yet')
            return
        for i, product in enumerate(products):
            _, Product_Title, Product_Desc, dop, mrp, sp = product
            print('\nProduct',i+1)
            print('-'*10)
            print(f"""Product\t\t\t{Product_Title}
                \nDescription\t\t{Product_Desc}
                \nPurchased Date\t\t{dop}
                \nMarked Price\t\t{mrp}
                \nSelling Price\t\t{sp}
            """)
        
            
        opt = int(input('\n\nChoose one option\n\n1 See people interested in your product\n2 Delete any product if already sold out\n3 Sell Page\n\n'))
        
        if opt == 1:
            productindex = int(input('\nEnter the Product no. to see interested people for that product : '))-1
            pid = products[productindex][0]
            c.execute(f"SELECT buyer_list FROM product WHERE pid = {pid}")
            fet = c.fetchone()
            (buyer_list, ) = fet
            byspl = buyer_list.split(',')
            if fet and not (len(byspl)==1 and byspl[0] == '-1'):
                buyer_change = []
                print("\nContacts of people interested in your product")
                print("-"*86)
                for uid_buy in buyer_list.split(','):
                    c.execute(f"SELECT FirstName, LastName, email, Mobile_Number FROM user WHERE uid = {int(uid_buy)}")
                    temp = c.fetchone()
                    if temp:
                        buyer_change.append(uid_buy)
                        fname, lname, email, MobNo = temp
                        print(f"""\nBuyer Name\t\t{fname} {lname}
                                \nMobile Number\t\t{MobNo}
                                \nEmail\t\t\t{email}""")
                if buyer_change:
                    buyer_change.append('-1')
                    buyer_list = ','.join(buyer_change)
                    
                    # updating buyer_list
                    
                    c.execute(f"UPDATE product SET buyer_list = '{buyer_list}' WHERE pid = {pid}")
                    conn.commit()
                else:
                    print('Unfortunately there is no one interested')
            else:
                print('Unfortunately there is no one interested')
        
        #if user wants to delete any product
        
        elif opt == 2:
            productindex = int(input('\nEnter the Product no. which you want to delete : '))-1
            pid = products[productindex][0]
            c.execute(f'DELETE FROM product WHERE pid = {pid}')
            conn.commit()
            print("Product", (productindex+1), 'is deleted !\nCongrats on selling your product ^_^!' )
            
        else:
            return
            
        if not int(input('\n\n1 Continue\n2 Sell Page\n\n')) == 1:
            return
            

def main_sell(uid):
    while True:
        print('\nSell Page')
        print('-'*13)
        inp = int(input('\n1 sell product\n2 View your selling products\n3 Home Page\n\n'))
        if inp == 1:
            insert(uid)
        elif inp == 2:
            sell_list(uid)
        else:
            return
        
#testing function

if __name__ == '__main__':
    main_sell(2)

