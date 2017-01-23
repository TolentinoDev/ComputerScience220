'''
Ryan Tolentino
Python 3
Credit Cards
'''
class CreditCard:
    # A customers credit card


    def __init__(self,customer,bank,account,limit):
        """ Create a new credit card instance

    The inital balance = 0

    customer = the name of the customer (e.g., 'John doe')
    bank = the name of the bank(e.g., 'BOA')
    account = the account id (e.g., '1234 0345 1234 1233')
    limit = credit limit(in dollars)
    """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        # Return name of the customer
        return self._customer

    def get_bank(self):
        # Return name of the bank
        return self._bank
    
    def get_account(self):
        # Return name of the customer
        return self._account
    
    def get_limit(self):
        # Return name of the customer
        return self._limit
    
    def get_balance(self):
        # Return name of the customer
        return self._balance
    
    def charge(self,price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self,amount):
        self._balance -=amount



    """ TESTING"""

if __name__ == '__main__':
        wallet = []
        wallet.append(CreditCard('John Bowman','California Savings',
                                  '5691 0375 9376 4509',2500))
        wallet.append(CreditCard('John Bowman','California Federal',
                                  '5444 0375 9376 4509',3500))
        wallet.append(CreditCard('John Bowman','California Finance',
                                  '6689 0375 9376 4509',5000))
for val in range(1,17):
            wallet[0].charge(val)
            wallet[1].charge(val*2)
            wallet[2].charge(val*3)

for c in range(3):
            print('Customer =',wallet[c].get_customer())
            print('Bank =',wallet[c].get_bank())
            print('Account =',wallet[c].get_account())
            print('Limit =',wallet[c].get_limit())
            print('Balance =',wallet[c].get_balance())
            while wallet[c].get_balance( )>100:
                wallet[c].make_payment(100)
                print('New balance = ',wallet[c].get_balance())
            print()
