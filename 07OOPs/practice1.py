"""Create a class to manage a bank account. The account should have attributes for the account holder's name and balance.
Include methods to deposit, withdraw, and display the account balance.
Note : set the min balance to 5000 and if you have less than that impose 500 fine, use conditional statements here"""

class Banking:
    bank_name = "SBI"
    min_balance = 5000
    fine = 500

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.__acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount diposited succefully. The updated balence is {self.balance}")
    
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("the balance will become less than the minimum balance of 5000, so you can't withdraw")
        else:
            self.balance -= amount
            print(f"Amount withdrawn succefully, The updated balance is {self.balance}")

    def display_balance(self):
        print(f"The available balance is {self.balance} on your account {self.__acc_no} ")
        print(f"")

    def add_to_Database(self):

        bank_db = {
            "name": self.name,
            "acc_no": self.__acc_no,
            "balance": self.balance
        }


c1 = Banking("Chenchu", 123451, 10000)
print(c1.name)

c1.deposit(1000)
c1.withdraw(500)
c1.withdraw(7000)