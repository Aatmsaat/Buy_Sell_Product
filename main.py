import login
import buy
import sell

def home(uid):
    while True:
        print('Home Page')
        print('-'*13)
        option = int(input('\n1 Sell Page\n2 Buy Page\n3 Logout\n\n'))
        if option == 2:
            buy.main_buy(uid)
        elif option == 1:
            sell.main_sell(uid)
        else:
            return
    
    
def site():
    print('\nWelcome to our console based Buy/Sell project\n')
    while True:
        option = int(input('\n1 Login\n2 Signup\n3 Exit\n\n'))
        if option == 1:
            home(login.login())
        elif option == 2:
            home(login.signup())
        else:
            print('Thanks for visiting !')
            return
            
if __name__ == '__main__':
    site()