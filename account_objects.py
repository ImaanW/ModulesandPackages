from account import Account

lisa_account = Account(500.00)
lisa_balance = lisa_account.getbalance()
print(lisa_balance)

bart_account = Account(100.00)
bart_balance = bart_account.getbalance()
print(bart_balance)

lisa_account.deposit(250.00)
bart_account.withdraw(50.00)

print('lisa balance :',lisa_account.getbalance(), 'bart balance:', bart_account.getbalance())
#deposit is a method/behaviour
# get balance = getter - special case beahviour method allow us to read or retrieve data restored inside of an object
# setter set,chnage/updatethe value thats being called

# classes give us the ability to store and the functionality to store, change
print(lisa_account)

total_balance = lisa_account.getbalance() + bart_account.getbalance()
print(total_balance)

lisa_account.set
