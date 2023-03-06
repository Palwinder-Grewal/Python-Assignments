import random
from datetime import datetime
from abc import ABC, abstractmethod
import re

class Bank(ABC):
    _accounts = []
    _transactions = {}
    _min_balance = 0
    bank_name = 'XYZ Bank'


    def __init__(self):
        self.account_num = self._genreate_acc_no()
        self.name = self.get_name()
        self.initial_deposit = self.initial_deposit()


    def get_name(self):
        self.name = input('Enter your full name: ')
        if len(self.name) == 0:
            print('Name field cant be empty!')
            self.get_name()
        elif re.match('^[A-Za-z]+$', self.name):
            return self.name
        else:
            print('Name should contain alphabets only: ')
            self.get_name()


    def initial_deposit(self):
        self.initial_deposit = None
        while type(self.initial_deposit) != int:
            try:
                self.initial_deposit = int(input("Enter initial deposit (atleast 1500): "))
            except ValueError:
                print('enter numeric value only: ')
        self.mylist = []
        self._transactions[self.account_num] = self.mylist
        count = 1
        while self.initial_deposit < 1500 or self.initial_deposit % 100 != 0 and count <= 3:
            self.initial_deposit = int(input("Initial deposit should be in hundreds and atleast 1500 \nEnter initial deposit again: "))
            count += 1
        self.balance = self.initial_deposit
        self.mylist.append(f'Account created with account number: {self.account_num} and {self.initial_deposit} has been deposited at {datetime.now().strftime("%H:%M:%S")}')


    def _genreate_acc_no(self):
        acc_num = ""
        for i in range(10):
            acc_num += str(random.randint(0, 9))
        while int(acc_num) in self._accounts:
            acc_num = self.genreate_acc_no()
        self._accounts.append(int(acc_num))
        return int(acc_num)

    
    @abstractmethod
    def withdraw(self):
        pass


    def deposit(self):
        deposit_ammount = None
        count = 1
        try:
            deposit_ammount = int(input('Enter deposit ammount: '))
        except ValueError:
            print('Non numeric input \nTry again \n')
            return
        while deposit_ammount < 100 or deposit_ammount % 100 != 0:
            if count == 3:
                return
            try:
                deposit_ammount = int(input('Deopsit ammount should be in hundreds: '))
                count += 1
            except ValueError:
                print('Non numeric input \nTry again \n')
                return

        if count <= 3:
            self.balance += deposit_ammount
            self.mylist.append(f'{deposit_ammount} has been deposited at {datetime.now().strftime("%H:%M:%S")}')
            print(f'{deposit_ammount} has been credited in your account. Current balance is: {self.balance}')


    def show_balance(self):
        print(f'Current balance: {self.balance}')


    def mini_statement(self):
        print('\nMINI STATEMENT:\n')
        if len(self._transactions[self.account_num]) >= 5:
            count = 1
            for i in self._transactions[self.account_num][-5::]:
                print(f'{count}: {i}')
                count += 1
        else:
            for i in range (0, len(self._transactions[self.account_num])):
                print(f'{i + 1}: {self._transactions[self.account_num][i]}')
    

    def showtrs(self):
        print('\nALL TRANSACTION: \n')
        for i in range (0, len(self._transactions[self.account_num])):
            print(f'{i + 1}: {self._transactions[self.account_num][i]}')


    @abstractmethod
    def __str__(self):
        pass


class SavingAccount(Bank):

    def withdraw(self):
        if self.balance == self._min_balance:
            print("Low balance! can't withdraw")
            return
        count = 1
        withdraw_ammount = None
        try:
            withdraw_ammount = int(input('Enter withdraw ammount(it should be in hundreds): '))
        except ValueError:
            print('Non numeric input \nTry again \n')
            return

        while (withdraw_ammount < 100 or self.balance < withdraw_ammount) or withdraw_ammount % 100 != 0:
            if count == 3:
                return
            try:
                if withdraw_ammount <= 0:
                    count += 1
                    withdraw_ammount = int(input("Withdraw ammount can't be negative or zero: "))
                elif withdraw_ammount % 100 != 0:
                    count += 1
                    withdraw_ammount = int(input('Withdraw ammount should be in hundreds \nEnter ammount again: '))
                elif withdraw_ammount > self.balance:
                    count += 1
                    withdraw_ammount = int(input('Insuffucuent balance \nEnter ammount again: '))
            except ValueError:
                print('Non numeric input \nTry again \n')
                return

        if count <= 3:
            self.balance -= withdraw_ammount
            self.mylist.append(f'{withdraw_ammount} has been withdrawn at {datetime.now().strftime("%H:%M:%S")}')
            print(f'{withdraw_ammount} debited from your account. Current balance is: {self.balance}')


    def __str__(self):
        print('\n ACCOUNT INFO: \n')
        return f"Savings Account \nAccount number: {self.account_num} \nName: {self.name} \nBalance: {self.balance}"


class CurrentAccount(Bank):
    _min_balance = -150000

    def __init__(self):
        self.account_num = self._genreate_acc_no()
        self.name = input('Enter company name: ')
        self.initial_deposit = self.initial_ammount()


    def initial_ammount(self):
        self.initial_deposit = None
        while type(self.initial_deposit) != int:
            try:
                self.initial_deposit = int(input("Enter initial deposit (atleast 2500): "))
            except ValueError:
                print('enter numeric value only: ')
        self.mylist = []
        self._transactions[self.account_num] = self.mylist
        count = 1
        while self.initial_deposit < 2500 or self.initial_deposit % 100 != 0 and count <= 3:
            self.initial_deposit = int(input("Initial ammount should be in hundreds and atleast 2500: "))
            count += 1
        self.balance = self.initial_deposit
        self.mylist.append(f'Current Account created with account number: {self.account_num} and {self.initial_deposit} has been deposited at {datetime.now().strftime("%H:%M:%S")}')
        return self.initial_deposit


    def withdraw(self):
        if self.balance == -150000:
            print("low balance can't withdraw money!")
            return
        count = 1
        withdraw_ammount = None
        try:
            withdraw_ammount = int(input('Enter withdraw ammount: '))
        except ValueError:
            print('Non numeric input \nTry again \n')
            return
        while (withdraw_ammount < 100 or self.balance + abs(self._min_balance) < withdraw_ammount) or withdraw_ammount % 100 != 0 and count <= 3:
            if count == 3:
                return
            try:
                if withdraw_ammount <= 0:
                    count += 1
                    withdraw_ammount = int(input("Withdraw ammount can't be negative or zero: "))
                elif withdraw_ammount % 100 != 0:
                    count += 1
                    withdraw_ammount = int(input('Withdraw ammount should be in hundreds \nEnter ammount again: '))
                elif withdraw_ammount > self.balance:
                    count += 1
                    withdraw_ammount = int(input('Insuffucuent balance \nEnter ammount again: '))
            except ValueError:
                print('Non numeric input \nTry again \n')
                return

        if count <= 3:
            self.balance -= withdraw_ammount
            self.mylist.append(f'{withdraw_ammount} has been withdrawn at {datetime.now().strftime("%H:%M:%S")}')
            print(f'{withdraw_ammount} debited from your account. Current balance is: {self.balance}')


    def __str__(self):
        print('\n ACCOUNT INFO: \n')
        return f"Current Account \nAccount Number: {self.account_num} \nCompany Name: {self.name} \nBalance: {self.balance}"


#########################################################################################################################################


print(f'Welcome to {Bank.bank_name}')
choice = input('Enter "s" to open savings account \nEnter "c" to open current account:\n ')
count = 1
v = True
while v and count < 3:
    if choice.lower() == 's':
        account1 = SavingAccount()
        v = False
    elif choice.lower() == 'c':
        account1 = CurrentAccount()
        v = False
    else:
        print('Enter valid input')
        choice = input('Enter "s" to open savings account \nEnter "c" to open current account:\n ')
        count += 1

if count < 3:
    action = input('\nEnter 1 for Withdraw \nEnter 2 for Deposit \nEnter 3 to Check Balance \nEnter 4 to check Mini Statement \nEnter 5 for all transactions \nEnter 6 for Account info \nEnter 7 to exit \nEnter choice: ')
    chances = 1
    while chances < 3:
        match action:
            case '1':
                account1.withdraw()
            case '2':
                account1.deposit()
            case '3':
                account1.show_balance()
            case '4':
                account1.mini_statement()
            case '5':
                account1.showtrs()
            case '6':
                print(account1)
            case '7':
                print(f"Thank you for using {Bank.bank_name} services. Have a nice day!")
                exit()
            case _:
                print('Invalid choice!')
                chances += 1

        action = input('Enter choice: ')

if count == 3 or chances == 3:
    print('\nYou have reached maximum invalid inputs \nTry again')