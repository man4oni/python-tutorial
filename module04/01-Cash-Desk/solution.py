class Bill(object):
    def __init__(self,amount):
        self.amount=amount
        if amount < 0:
            raise ValueError('amount must be positive ')
        if type(amount) != int:
            raise TypeError('amount must be INT')

    def __str__(self):
        return ("A {}$ bill").format(self.amount)
    def __int__(self):
        return int(self.amount)
    def __hash__(self):
        return hash(self.amount)
    def __repr__(self):
        return f'Bill({self.amount})'
    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.amount == other.amount
        )

class BatchBill():
    def __init__(self,Bills):
        #bills = [int(i) for i in Bills]
        self.batch=list(Bills)
    def __len__(self):
        return len(self.batch)

    def __getitem__(self, index):
        return self.batch[index]

    def total(self):
        res=0
        num_bills=[int(i) for i in self.batch]
        for i in num_bills:
            res += i
        return res

class CashDesk(object):


    def __init__(self,res=None):
        self.t=res
        if res==None:
            self.t=0


    def take_money(self, money):

        if isinstance(money, Bill):
            self.m = int(money)
        elif isinstance(money, BatchBill) :
            self.m= [int(x) for x in money]
        if type(self.m)==int:
            self.t+=self.m
        if type(self.m)==list:
            for x in self.m:
                self.t+=x
        return self.t

    def total(self):
        return self.t

    def inspect(self):
        pass


