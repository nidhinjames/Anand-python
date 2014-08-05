def make_account():
	return {'balance': 0}

def deposit(account, amount):
	account['balance']+= amount
	return account['balance']
def withdraw(account, amount):
	account['balance'] -= amount
	return account['balance']

a = make_account()
b = make_account()
a = deposit(a, 100)
####print "deposit a"
####print a
g = withdraw(a, 30)
print g

