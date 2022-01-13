# Please extend the Account, Bank and Customer classes
# deposit and charge methods including a validation that will prevent any misuse of those functions (unsafe operations that can influence the balance of the account
# implementation of transfer(...) in Bank. As you do that please also include validation of input parameters.
# Please note that you might need to first find the "from" and "to" accounts in the list based on the ids provided as input.

class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount
        print('Amount deposited successfully. Current balance : {}'.format(self._balance))

    def charge(self, amount):
        if ( self._balance >= amount):
            self._balance -= amount
            print('Amount charged successfully. Current balance : {}'.format(self._balance))
            return 1
        else:
            print('Insufficient funds. Current balance : {}'.format(self._balance))
            return 0

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    pass


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer, is_savings=False):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_acc_id, to_acc_id, amount):
        from_acc_ind =0
        to_acc_ind = 0
        charged_ind = 0
        #includes basic validations
        if from_acc_id != to_acc_id & (amount > 0): #from and to cant be same
            for account in self.account_list:
                if account.id == from_acc_id: #check for existence
                    from_acc_ind = 1
                    from_account = account
                if account.id == to_acc_id: #check for existence
                    to_acc_ind = 1
                    to_account = account
            if (from_acc_ind == 1 ) & (to_acc_ind == 1):
                    charged_ind = from_account.charge(amount)
                    if charged_ind == 1: #check for successful debit, if yes deposit
                        to_account.deposit(amount)

    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)

#Creating data
b = Bank()
c = b.create_customer('Anne', 'Smith')
a1 = b.create_account(c)

c2 = b.create_customer('John', 'Brown')
a2 = b.create_account(c2, is_savings=True)

print('Before any transactions')
print(b)

#Transaction1 - Deposit 1000 to Account 1
print('Transaction1 - Deposit 1000 to Account 1')
a1.deposit(1000)
print('Transaction2 - Charging 100 to Account 1')
#Transaction2 - Charging 100 to Account 1
a1.charge(1)

print('After Transaction 1 & 2')
print(b)

print('Transaction3 - Overcharging attempt - Account 1 - Revert back')
#Transaction3 - Overcharging attempt - Account 1 - Revert back
a1.charge(10000)
print('After Transaction 3')
print(b)

print('\nTransaction4,5 - Credit, Debit of Account 2')
#Transaction4 - Deposit 50 to Account 2
a2.deposit(200)
#Transaction5 - Charging 5 to Account 2
a2.charge(100)
print(b)

print('\n#Transaction6 - Transferring 200 to Account 2')
#Transaction6 - Transferring 200 to Account 2
b.transfer(1,2,200)
print(b)

print('Transaction7 - Overcharging attempt during transfer - Account 2 - Revert back')
#Transaction7 - Overcharging attempt during transfer - Account 2 - Revert back
b.transfer(2,1,500)
print(b)

print('Validation failure samples - No net change')
b.transfer(3,1,500)
b.transfer(2,3,500)
b.transfer(2,1,-500)
print(b)