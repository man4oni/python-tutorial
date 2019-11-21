class BankAccount(object):

    def __init__(self,name,balance,currency):
        self.name = name
        self._balance = balance
        self.currency = currency
        if balance < 0:
            raise ValueError('balance cant be negative')
        self._history=['Account was created']


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be + ')
        self._balance += amount
        self._history.append("Deposited "+str(amount)+self.currency)
        return self._balance




    def withdraw(self,amount):
        if amount >0:
            if amount <= self._balance:
                self._balance -= amount
                self._history.append(str(amount)+self.currency+" was withdrawn")
                print( True )
            else:
                print( False)
        return self._balance



    def balance(self):
        self._history.append("Balance check -> "+str(self._balance)+self.currency)
        return self._balance

    def history(self):
        return self._history



    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name,self._balance,self.currency)

    def __int__(self):
        self._history.append("__int__ check -> "+str(self._balance)+self.currency )
        return self._balance

    def transfer_to(self,account, amount):
        self.acc=account
        self.money=amount
        if self.currency==account.currency:
            if amount <= self._balance:
                self._balance -= amount
                account._balance += amount
                self._history.append("Transfer to "+account.name+" for "+str(self.money)+self.currency)
                return account.balance()
            else:
                raise TypeError('choose the correct currency')

