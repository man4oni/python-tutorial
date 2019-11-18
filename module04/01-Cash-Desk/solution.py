
class Bill(object):
    def __init__(self,amount):
        self.amount = amount
        if amount < 0:
            raise ValueError('amount must be positive ')
        if type( amount ) != int:
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
    def __init__(self, Bills):
        #bills = [int(i) for i in Bills]
        self.batch = list( Bills )
    def __len__(self):
        return len(self.batch)

    def __getitem__(self, index):
        return self.batch[index]

    def total(self):
        res = 0
        num_bills = [int(i) for i in self.batch]
        for i in num_bills:
            res += i
        return res

class CashDesk(object):


    def __init__(self,res = None):
        self.balance = res
        if res == None:
            self.balance = 0
        self.desk = {5:0, 10:0, 15:0}
        self.bills = []
    def take_money(self, money):
        if isinstance(money, Bill):
            self.bills.append(int(money))
        if isinstance(money, BatchBill):
            for x in money:
                self.bills.append(int(x))

        return self.bills





    def total(self):
        for bill in self.bills:
            self.balance += bill
        return self.balance


    def inspect(self):
        for key in self.bills:
            if key in self.desk.keys():
                self.desk[key] = self.desk[key] + 1


        pr = (f'We have a total of {self.total()}$ in the desk\n'
            'We have the following count of bills, sorted in ascending order:')

        for key, value in self.desk.items():
            pr += ('\n'f'{key}$ bills - {value}')

        return  pr





