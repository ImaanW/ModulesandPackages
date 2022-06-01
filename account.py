class Account:
    numCreated = 0

    def __init__(self, initial):
        self._balance = initial
        Account.numCreated += 1
        self._description = "n/a"


    def deposit(self, amt):
        self._balance += amt
        return

    def withdraw(self, amt):
        self._balance -= amt
        return
#getter
    def getbalance(self):
        return self._balance

#setter
    def set_holder_name(self, name):
       return self._holder_name = name

    def __str__(self):
        return "bank account with balance of " + str(self.getbalance())

    def __add__(self, other):
        return self.getbalance() + other.getbalance()


    #def description(self, description):
   #     self._description(self, description)