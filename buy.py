import sqlite3
conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# function to change users city

def change_city(uid, buyercity, buyerstate):
    print("\nchoose one of cities products available for your state", buyerstate)
    print("-"*86)
    c.execute(f"SELECT user.city FROM user INNER JOIN product on product.uid = user.uid WHERE state = '{buyerstate}' AND city != '{buyercity}'")
    cities = set(c.fetchall())
    cities = [*cities]
    if not cities:
        print('\nUnfortunately there no products except in your city\n')
        return (True, buyercity)
    
    # printing Number of cities
    
    for i,(city, ) in enumerate(cities):
        print(i+1, city)
    cityindex = int(input('\nEnter the city no. : '))-1
    (buyercity, ) = cities[cityindex]
    return (True, buyercity)
    
# main function of buy

def buy(uid):
    c.execute(f"SELECT city, state, buy_list FROM user WHERE uid = {uid}")
    buyercity, buyerstate, buy_list = c.fetchone()
    old_buyercity = buyercity
    
    #checking if buyer's city has any products
    
    c.execute(f"SELECT pid from product WHERE uid = (SELECT uid FROM user WHERE city = '{buyercity}' AND uid != {uid})")
    flag1 = not c.fetchone() == None
    
    if not flag1:
        print('nothing to sell in your city yet!\n')
    
    #until user satisfied loop keeps on repeating
    
    while True:
        print('\nCurrently your city is', buyercity)
        changecity = input('If you want to change your city then type "Yes" otherwise type "No" : ')
        if changecity[0] in 'yY':
            flag, buyercity = change_city(uid, buyercity, buyerstate)
         
        #Products available for his home state
        
        print(flag, flag1, buyercity, old_buyercity)
        
        if flag and not (not flag1 and buyercity == old_buyercity):
            print('\nproducts for city', buyercity)
            c.execute(f"SELECT user.uid, product.pid, product.Product_Title, product.Product_Desc, product.dop, product.mrp, product.sp FROM user INNER JOIN product on user.uid = product.uid WHERE user.city = '{buyercity}'")
            products = c.fetchall()
            for i, product in enumerate(products):
                _, _, Product_Title, Product_Desc, dop, mrp, sp = product
                print('\nProduct',i+1)
                print('-'*10)
                print(f"""Product\t\t\t{Product_Title}
                    \nDescription\t\t{Product_Desc}
                    \nPurchased Date\t\t{dop}
                    \nMarked Price\t\t{mrp}
                    \nSelling Price\t\t{sp}
                """)
                
            #if user wants to purchase product
            
            productPurchase = input('\n\nif you want to purchase any product type "Yes" else "No" : ')
            if productPurchase[0] in 'yY':
                productindex = int(input('\nEnter the Product no. which you want to buy : '))-1
                uid_sell, pid = products[productindex][0:2]
                
                #Seller's information
                
                c.execute(f"SELECT FirstName, LastName, email, Mobile_Number FROM user WHERE uid = {uid_sell}")
                fname, lname, email, MobNo = c.fetchone()
                print("\nContact the seller to purchase the product and paying process")
                print("-"*86)
                print(f"""\nSeller Name\t\t{fname} {lname}
                        \nMobile Number\t\t{MobNo}
                        \nEmail\t\t\t{email}""")
                
                # updating users who wants to purchase this product in the buyer list
                
                c.execute(f"SELECT buyer_list FROM product WHERE pid = {pid}")
                (buyer_list, ) = c.fetchone()
                buyer_list_changed = ','.join(set(buyer_list.split(',')+[str(uid)]))
                c.execute(f"UPDATE product SET buyer_list = '{buyer_list_changed}' WHERE pid = {pid}")
                
                # updating buyer's buy list which product buyer wants to purchase
                
                buy_list_changed = ','.join(set(buy_list.split(',')+[str(pid)]))
                c.execute(f"UPDATE user SET buy_list = '{buy_list_changed}' WHERE uid = {uid}")
                
                #commit changes
                conn.commit()
        else:
            print(f'\ncity {buyercity} has no products to sell')
        if not int(input('\n1 Continue\n2 Buy Page\n\n')) == 1:
            return
    
#functions interested products

def interest_list(uid):
    while True:
        c.execute(f"SELECT buy_list FROM user WHERE uid = {uid}")
        fet = c.fetchone()
        (buy_list, ) = fet
        byspl = buy_list.split(',')
        if not fet or (len(byspl) == 1 and byspl[0] == '-1'):
            print('\nYou have not selected any products to buy yet\n')
            return
        buy_change = []
        print('Products you want to buy are: ')
        print("-"*86)
        for pid_buy in byspl:
            c.execute(f"SELECT uid, pid, Product_Title, Product_Desc, dop, mrp, sp FROM product WHERE pid = {int(pid_buy)}")
            temp = c.fetchone()
            if temp:
                buy_change.append(pid_buy)
                _, _, Product_Title, Product_Desc, dop, mrp, sp = temp
                print('\nProduct',len(buy_change))
                print('-'*10)
                print(f"""Product\t\t\t{Product_Title}
                    \nDescription\t\t{Product_Desc}
                    \nPurchased Date\t\t{dop}
                    \nMarked Price\t\t{mrp}
                    \nSelling Price\t\t{sp}
                """)
            
        if buy_change:
            buy_change.append(str(-1))
            buy_list = ','.join(buy_change)
                    
            # updating buyer_list
                    
            c.execute(f"UPDATE user SET buy_list = '{buy_list}' WHERE uid = {uid}")
            conn.commit()
        
        else:
            print('you have not selected any products to buy')
            return
            
        opt = int(input('\n1 See Contact list of any product\n2 Delete any product if not interested\n3 Buy Page\n\n'))
        
        if opt == 1:
            productindex = int(input('\nEnter the Product no. to see contact details : '))-1
            pid_buy = buy_change[productindex]
            
            #Seller's information
                
            c.execute(f"SELECT FirstName, LastName, email, Mobile_Number FROM user WHERE uid = (SELECT uid FROM product WHERE pid = {pid_buy})")
            fname, lname, email, MobNo = c.fetchone()
            print("\nseller's details")
            print("-"*86)
            print(f"""\nSeller Name\t\t{fname} {lname}
                    \nMobile Number\t\t{MobNo}
                    \nEmail\t\t\t{email}""")
            
            # delete uninterested product 
            
        elif opt == 2:
            productindex = int(input('\nEnter the Product no. to delete the product you are not interested in : '))-1
            pid_buy = buy_change[productindex]
            buy_change.remove(str(pid_buy))
            buy_list = ','.join(buy_change)
            c.execute(f"UPDATE user SET buy_list = '{buy_list}' WHERE uid = {uid}")
            
            #Also need to update the buyer_list
            
            c.execute(f"SELECT buyer_list FROM product WHERE pid = {pid_buy}")
            (buyer_list, ) = c.fetchone()
            bl = buyer_list.split(',')
            bl.remove(str(uid))
            buyer_list_changed = ','.join(bl)
            c.execute(f"UPDATE product SET buyer_list = '{buyer_list_changed}' WHERE pid = {pid_buy}")
            
            conn.commit()
            
        else:
            return
            
        if not int(input('\n1 Continue\n2 Buy Page\n\n')) == 1:
            return
            
            

        
 
def main_buy(uid):
    while True:
        print('\nBuy Page')
        print('-'*13)
        inp = int(input('\n1 Buy product\n2 View products which you want to buy\n3 Home Page\n\n'))
        if inp == 1:
            buy(uid)
        elif inp == 2:
            interest_list(uid)
        else:
            return

#Testing funcitons

if __name__ == '__main__':
    main_buy(1)
    #buy(1)
