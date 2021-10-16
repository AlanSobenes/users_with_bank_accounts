class BankAccount:
    
    Bank_name = "BigBank"
    
    def __init__(self, int_rate = .02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if BankAccount.sufficient_funds(self.balance, amount):
            self.balance-=amount
            return self
        else:
            print("Insufficint Funds: Charging a $5 fee!") 
            self.balance -= 5
            return self
        


    def display_account_info(self):
        print(f"Account Balance:${self.balance}")
        return self
    
    def yield_interest(self):
        print(f"Interst Yielded: ${self.balance*self.int_rate}")
        return self
    
    @staticmethod
    def sufficient_funds(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


class User:
    
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname
        self.account = BankAccount(int_rate=.02, balance=0)

        
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print( f"{self.fname}'s balance is ${self.account.balance}")
        return self
    
    def make_a_transfer(self, receiver, amount):
        receiver = receiver
        self.account.balance -= amount
        receiver.account.balance += amount
        print(f"{self.fname} transfered ${amount} to {receiver.fname}") 
        print(f"{self.fname}'s new balance is ${self.account.balance} and {receiver.fname}'s new balance is ${receiver.account.balance}")   
        return self



alan = User( 'Alan', 'David')
joe = User('Joe', 'Dirt')
Mike = User('Mike', 'Tyson')



alan.make_deposit(1000).make_deposit(5000).make_deposit(2500).make_withdrawal(1500).display_user_balance().make_a_transfer(joe, 700)  


joe.make_deposit(300).make_deposit(200).make_withdrawal(10).make_withdrawal(10).display_user_balance()



Mike.make_deposit(10).make_withdrawal(15).make_withdrawal(20).make_withdrawal(20).display_user_balance()



