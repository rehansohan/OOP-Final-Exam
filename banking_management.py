class Bank:
    def __init__(self):
        self.users = {}
        self.loan_feature_enabled = True
        self.admin = None
        self.total_bank_balance = 0
        self.total_loan = 0  
    def create_account(self, username, initial_balance=0):
        if username not in self.users:
            user = User(self, username, initial_balance)
            self.users[username] = user
            self.total_bank_balance += initial_balance
            user.transaction_history.append(initial_balance)
            print(f'Welcome To  created Account in this Bank. Account name is: {username}')
        else:
            print(f'Account name {username} already exists in this bank')

    def create_admin_account(self, admin_name):
        if not self.admin:
            self.admin = Admin(self, admin_name)
            print(f'Account created for admin: {admin_name}')
        else:
            print(f'Admin account is already exists in this bank')

    def account_details(self, username):
        if username in self.users:
            user = self.users[username]
            print(f'Account details for {username} BELO:--')
            print(f'Balance: {user.balance}')
            print(f'Loan Amount: {user.user_loan_amouont}')
            print(f'Transaction History: {user.transaction_history}')
        else:
            print(f'Account for {username} does not exist in this bank')




class User(Bank):
    def __init__(self, bank, username, balance=0) -> None:
        self.bank = bank
        self.username = username
        self.balance = balance
        self.user_loan_amouont = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.bank.total_bank_balance += amount
        self.transaction_history.append(f'Deposit {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'You are not eligible for withdrawal , The bank is Bankrupt')
        else:
            self.balance -= amount
            self.bank.total_bank_balance -= amount
            self.transaction_history.append(f'Withdraw {amount}')

    def take_loan(self):
        if self.user_loan_amouont == 0 and self.bank.loan_feature_enabled:
            loan_amount = 2 * self.balance
            self.user_loan_amouont += loan_amount
            self.bank.total_bank_balance -= loan_amount
            self.bank.total_loan += loan_amount
            self.transaction_history.append(f'Took a loan: {self.user_loan_amouont}')
        else:
            print(f'You are not eligible for loan')

    def transfer(self, amount, receive_username):
        if amount <= 0:
            print("Invalid transfer amount,You don't have enough money")
            return

        if receive_username in self.bank.users:
            receive = self.bank.users[receive_username]

            if amount <= self.balance:
                self.balance -= amount
                receive.balance += amount

                self.transaction_history.append(f'Transferred {amount} to {receive_username}')
                receive.transaction_history.append(f'Received {amount} from {self.username}')
                print(f'Transfer successful: {amount} to {receive_username}')
            else:
                print("Insufficient balance for transfer.")
        else:
            print(f"Receiver account {receive_username} does not exist.")

            

 


class Admin(Bank):
    def __init__(self, bank, admin_name) -> None:
        self.bank = bank
        self.admin_name = admin_name

    def check_total_bank_details(self):
        print(f' Total available balance of the BANK BELO:--')
        print(f'Total bank balance is: {self.bank.total_bank_balance}')
        print(f'Total loan amount is: {self.bank.total_loan}')
        if self.bank.total_loan > self.bank.total_bank_balance:
            self.bank.loan_feature_enabled = False
            print('Loan featuer is OF')
        else:
            print(f'Loan feature is ON')

    def loan_feature_of_the_bank(self):
        if self.bank.total_bank_balance<self.bank.total_loan:
            self.loan_feature_enabled=False
            print(f'lona feature OF,you are note take a lone')
        else:
            self.loan_feature_enabled=True
            print(f'loan frature ON,Please wait:-')



bank = Bank()
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)
bank.create_account('Sohan', 4000)
bank.create_admin_account("MD.Hassan")
bank.users['Bob'].take_loan()
bank.users['Alice'].transfer(200, 'Bob')
bank.users['Bob'].withdraw(1000)
bank.account_details('Sohan')
bank.account_details('Bob')
bank.account_details('Alice')
bank.admin.check_total_bank_details()



